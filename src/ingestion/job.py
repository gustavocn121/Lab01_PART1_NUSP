import logging
from pathlib import Path
from .kaggle_client import download_dataset
from ..utils import read_config

def load_config():
    logging.info("Loading configuration...")
    config_path = Path(__file__).resolve().parents[0] / "config.yaml"
    config = read_config(config_path)
    logging.info(f"Configuration loaded: {config}")
    return config

def run():
    logging.info("Starting dataset ingestion...")
    config = load_config()
    raw_path = config.get("raw_path")
    dataset = config.get("dataset")

    try:
        Path(raw_path).mkdir(parents=True, exist_ok=True)
        dataset_path = download_dataset(dataset, output_dir=raw_path)
        logging.info(f"Downloaded dataset to: {dataset_path}")
    except Exception as e:
        logging.error(f"Ingestion failed: {e}")
        raise


if __name__ == "__main__":
    run()