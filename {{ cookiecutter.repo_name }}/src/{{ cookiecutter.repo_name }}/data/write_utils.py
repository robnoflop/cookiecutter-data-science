from pathlib import Path
import pandas as pd
from typing import Union


def write_df_as_paquet(df: pd.DataFrame, path: Union[str, Path]) -> None:
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    df.to_parquet(path)
