import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    # Compute ranks
    scores["rank"] = scores["score"].rank(method="dense", ascending=False).astype(int)

    # Return result table ordered by score descending
    result = scores[["score", "rank"]].sort_values(by="score", ascending=False).reset_index(drop=True)

    return result