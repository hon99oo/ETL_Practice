import logging
from typing import Any

from app.interface import Pipeline


class ETLPractice(Pipeline):
    """
    building_floor 테이블 가공하는 데이터 파이프라인 클래스
    """

    def __init__(
        self,
        loop: int,
    ):
        """
        Args:
        """
        self._loop = loop


    def run(self) -> Any:
        """
        파이프라인을 실행 메서드
        Returns:
            [Any]: 파이프라인의 단계별 반환 값
        """
        logging.info(f"running pipeline")
        for obj in range(self._loop):
            logging.info("start ETL on ",obj)
            data={}
            result = self.emit(data)
        return result
