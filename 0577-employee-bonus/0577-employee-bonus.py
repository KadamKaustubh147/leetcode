import pandas as pd

def employee_bonus(employee: pd.DataFrame, bonus: pd.DataFrame) -> pd.DataFrame:
    # to find employees with no bonus or less than 1000 bonus --> we use left join where left is employee

    res = pd.merge(employee,bonus,on="empId", how="left")

    return res[(res['bonus'] < 1000) | (res['bonus'].isna())][['name', 'bonus']]