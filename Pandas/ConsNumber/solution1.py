import pandas as pd

def consecutive_numbers(logs: pd.DataFrame) -> pd.DataFrame:
    
    # Identify positions where the current value equals the previous two
    mask = (logs["num"] == logs["num"].shift(1)) & (logs["num"] == logs["num"].shift(2))
    
    # Return unique numbers that meet the condition
    return pd.DataFrame({"ConsecutiveNums": logs.loc[mask, "num"].unique()})