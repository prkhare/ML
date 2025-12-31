import pandas as pd
from sklearn.datasets import load_iris

def load_data():
    iris=load_iris(as_frame=True)
    df=iris.frame
    df.to_csv("/workspaces/ML_DVC_DEMO/data/raw/iris.csv",index=False)
    print(df.head())

if __name__=="__main__":
    load_data()
