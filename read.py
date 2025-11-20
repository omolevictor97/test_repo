import pandas as pd
def read_csv(filepath:str, n:int):
    df = pd.read_csv(filepath)
    print(df.head(n = n)
    return df

