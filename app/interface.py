import asyncio
from functools import partial
import types
from typing import Any, Callable, Dict, Optional, Tuple


class Pipeline:
    """
    Pipeline Base 클래스
    상속하여 구체적인 파이프라인 클래스를 정의하는데 사용한다.
    """

    def add_pipe(self, f: Callable, args: Optional[Tuple] = None, kwargs: Optional[Dict] = None):
        """
        파이프라인에 필요한 주요 task(callable)을 구성하는 메서드
        Args:
            f (Callable): 파이프라인을 구성하는 task 객체
        """
        if args is None:
            args = ()

        if kwargs is None:
            kwargs = {}

        if getattr(self, "_processes", None) is None:
            self._processes = []

        if callable(f):
            if not isinstance(f, (types.BuiltinFunctionType,
                                  types.BuiltinMethodType,
                                  types.FunctionType)):
                if args:
                    inst = f(args, **kwargs)
                else:
                    inst = f()
                self._processes.append(inst)
            else:
                if args or kwargs:
                    self._processes.append(partial(f, *args, **kwargs))
                else:
                    self._processes.append(f)
        else:
            raise ValueError(f"arg {f} is not callable")

        return self

    def emit(self, data: Any) -> Optional[Any]:
        """
        데이터 파이프라인으로 데이터를 입력하는 메서드

        Args:
            data (Any): 파이프라인으로 입력하는 데이터

        Returns:
            Optional[Any]: 파이프라인의 단계별 반환 값
        """
        if self._processes is None:
            return data

        else:

            for i, process in enumerate(self._processes):
                if i == 0:  # first process
                    result = data

                if asyncio.iscoroutinefunction(process.__call__):
                    result = asyncio.run(process(result))
                else:
                    result = process(result)

                if result is False:
                    # interrupt current step, e.g. one step => from the first to the end of process in self._processes
                    return False

            # to the next step
            if result is not None:
                return result

            else:
                return None

