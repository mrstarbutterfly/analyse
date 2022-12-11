import pandas as pd
import matplotlib.pyplot as plt

def create_df():
    df = pd.read_csv('Mall_Customers.csv')
    return df

def create_graph(df):
    df_female = df[df['Genre'] == 'Female']
    df_male = df[df['Genre'] == 'Male']
    for col in list(df_female.columns)[3:]:
        plt.hist(df_female[col])
        plt.xlabel(col)
        plt.ylabel('Num of female')
        plt.savefig(f'images/female_{col}.jpg')
        plt.clf()
    for col in list(df_male.columns)[3:]:
        plt.hist(df_male[col])
        plt.xlabel(col)
        plt.ylabel('Num of male')
        plt.savefig(f'images/male_{col}.jpg')
        plt.clf()



def check(df):
    count_of_female = len(df[(df['Genre'] == 'Female') & (df['Annual Income (k$)'] > 61.5)])
    count_of_male = len(df[(df['Genre'] == 'Male') & (df['Annual Income (k$)'] > 61.5)])
    if count_of_female>count_of_male:
        return True
    else:
        return False

def main():
    df = create_df()
    create_graph(df)
    print(f'num of man: {len(df[df["Genre"] == "Male"])} and num of woman: {len(df[df["Genre"] == "Female"])}')
    print(df.describe())
    print(check(df))



if __name__=='__main__':
    main()