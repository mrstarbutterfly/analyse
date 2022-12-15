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

    plt.hist(df['Genre'])
    plt.xlabel('Genre')
    plt.ylabel('Num of men and women')
    plt.savefig(f'images/male_genre.jpg')




def check(df):
    count_of_female = len(df[(df['Genre'] == 'Female') & (df['Annual Income (k$)'] > 61.5)])
    count_of_male = len(df[(df['Genre'] == 'Male') & (df['Annual Income (k$)'] > 61.5)])

    if count_of_female>count_of_male:
        return True
    else:
        return False


def main():
    df = create_df()
    print(df.head())
    create_graph(df)
    print("\nMy hypothesis is women spends more money than men yearly. "
          "We check it on the dataset about mall customers \n")
    print(f'num of man: {len(df[df["Genre"] == "Male"])} and num of woman: {len(df[df["Genre"] == "Female"])}')
    print("Number of men and women almost equal\n")
    print("Description of dataset")
    print(df.describe())
    print('\nExplore the annual income')
    print(df.describe()['Annual Income (k$)'])
    print("\nWe can see that median is 61,5 so we use it for hypothesis")
    if check(df):
        print("\nIn the result we understand that Women spends more many than men in this mall yearly")



if __name__=='__main__':
    main()