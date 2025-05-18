import argparse
import os
import json
import logging
from logging.config import dictConfig
from text2sql2.agent.metadata import SUPPORTED_DATABASES
from text2sql2.agent.graphs.main_graph import SQLReactAgent



cur_file_dir = os.path.dirname(os.path.realpath(__file__))
logging_config_path = os.path.join(cur_file_dir, "agent", "configs", "logging_config.json")
assert os.path.exists(logging_config_path)

with open(logging_config_path, 'r') as file:
    dict_config = json.load(file)


dictConfig(dict_config)
logger = logging.getLogger(__name__)


def main():
    parser = argparse.ArgumentParser(description="A simple command line argument parser.")
    parser.add_argument('-db', '--database', type=str, required=True, help='Provide the database name you want to work with')

    args = parser.parse_args()

    db_name = args.database.lower()
    assert db_name in SUPPORTED_DATABASES
    db_obj = eval(SUPPORTED_DATABASES[db_name])()
    agent = SQLReactAgent(db_obj)
    agent.run()

    logger.info("test logging")
    return "Test Run"


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logger.exception(e)
        raise e

# pip install -ve .
# python package -c /d/git_repos/baseML/project/package/configs/run_configs/mnist_trainer.yaml