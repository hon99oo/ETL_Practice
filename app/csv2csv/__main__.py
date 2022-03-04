import argparse
import logging
import sys

from app.pipeline import ETLPractice
from app.operations import make_mock_dataframe

logging.basicConfig(
    stream=sys.stdout, level=logging.INFO, format="[%(levelname)s|%(asctime)s]:%(message)s"
)

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-loop",
        type=str,
        default=10,
        help="set the loop eg) 10 ",
    )
    args = parser.parse_args()
    (
        ETLPractice(args.loop)
        .add_pipe(make_mock_dataframe)
        .run()
    )
    logging.info("End of ETL")

