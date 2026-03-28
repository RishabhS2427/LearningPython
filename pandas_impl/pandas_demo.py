import pandas as pd

def createDict():
    dict_ = {'a' : [11,12,13], 'b' : [21,22,23]}
    df = pd.DataFrame(dict_)
    print("------------------------")
    print(df.head())
    # calculate mean
    print("------------------------")
    print(df.mean())
    #discription all about the df
    print("------------------------")
    print(df.describe())

def main():
    createDict()

if __name__ == '__main__':
    print("Pandas demo")
    createDict()
