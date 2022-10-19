import zipfile
from pathlib import Path

import pandas as pd

from reproml.config import etl_conf as es
from reproml.etl.utils import download_url


def run_lyrics(dstpath: str = es.root_path / es.raw_data_path / es.lyrics.path) -> Path:  # noqa
    dstpath = Path(dstpath)

    download_url(es.lyrics.url, Path(es.lyrics.url).name, dstpath)
    return dstpath


def process_lyrics(
    srcpath: str = es.root_path / es.raw_data_path,
    dstpath: str = es.root_path / es.processed_data_path / es.lyrics.path,
) -> Path:

    srcpath = Path(srcpath)
    dstpath = Path(dstpath)

    with zipfile.ZipFile(srcpath / Path(es.lyrics.url).name) as z:
        with z.open(es.lyrics.file_name) as f:
            train = pd.read_csv(f, header=0, delimiter=",")

    train.to_parquet(dstpath, partition_cols=es.lyrics.partition_cols)

    return dstpath
