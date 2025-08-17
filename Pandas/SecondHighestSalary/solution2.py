import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    ranked = sorted(set(employee['salary']), reverse=True)  
    return pd.DataFrame([{'SecondHighestSalary': ranked[1] if len(ranked) >= 2 else None}])



    