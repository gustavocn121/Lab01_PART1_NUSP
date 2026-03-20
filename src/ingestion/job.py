import logging
from pathlib import Path

from ..utils import read_config
from .kaggle_client import download_dataset


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
    force_download = config.get("force_download")

    try:
        Path(raw_path).mkdir(parents=True, exist_ok=True)
        dataset_path = download_dataset(
            dataset, output_dir=raw_path, force_download=force_download
        )
        logging.info(f"Downloaded dataset to: {dataset_path}")
    except Exception as e:
        logging.error(f"Ingestion failed: {e}")
        raise


if __name__ == "__main__":
    run()
