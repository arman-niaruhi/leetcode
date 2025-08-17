import pandas as pd

def delete_duplicate_emails(person: pd.DataFrame) -> None:
     # Sort by 'id' so the smallest id comes first
    person.sort_values('id', inplace=True)
    
    # Drop duplicates and keep the first (smallest id)
    person.drop_duplicates(subset=['email'], keep='first', inplace=True)
    
    # Reset index starting from 1
    person.reset_index(drop=True, inplace=True)