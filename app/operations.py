import pandas as pd

def make_mock_dataframe(data: dict) -> dict:
    a=pd.DataFrame(
        {
            "a":[1,2,3],
            "b":[4,5,6],
            "c":[7,8,9]
        }
    )
    b=pd.DataFrame(
        {
            "a":[1,2,3],
            "b":[4,5,6],
            "c":[7,8,9]
        }
    )

    return data

def test(data: dict) -> dict:

    return data