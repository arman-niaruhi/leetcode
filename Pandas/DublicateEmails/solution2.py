import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    dupes = person['email'].value_counts().loc[lambda x:x>1].index.to_list()
    return pd.DataFrame({'Email':dupes})
    