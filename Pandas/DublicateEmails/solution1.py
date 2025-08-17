import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    # Find emails that appear more than once
    duplicated_emails = person['email'].value_counts()
    duplicated_emails = duplicated_emails[duplicated_emails > 1].index
    # Return as a DataFrame
    return pd.DataFrame(duplicated_emails, columns=['email'])