## Этот скрипт - небольшой проект по анализу датасета и постройке графиков

import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('https://raw.githubusercontent.com/Raven-ES1617/cu/main/datasets/week2/diamonds.csv')
df["cut"] = df["cut"].str.replace("ideal", "Ideal")

df["cut"] = df["cut"].str.replace("ideal", "Ideal")
df = df.sort_values('price', ascending= False)
df = df.assign(avg = df['price']/df['carat'])
df_1 = df.pivot_table(values= 'avg', index = 'color', aggfunc= 'mean').reset_index()
plt.title("Средняя цена за карат по цвету")
plt.ylabel('Средняя цена')
plt.bar(df_1['color'], df_1['avg'], color = 'skyblue')
plt.show()
# -----------------------------------------------------------------------
df_2 = df.pivot_table(values= 'avg', index = 'cut', aggfunc= 'mean').reset_index()
plt.title("Средняя цена за карат по цвету")
plt.ylabel('Средняя цена')
plt.bar(df_2['cut'], df_2['avg'], color = 'red')
plt.show()

def plot_stacked_bar(df: pd.DataFrame,
                     groupby_col: str,
                     category_col: str,
                     xlabel: str="",
                     ylabel: str="",
                     title: str="",
                     ) -> None:
    stack = pd.Series(index=df[category_col].unique(), data=0).sort_index()
    for i in df[groupby_col].unique():
        df_i = df[df[groupby_col] == i][category_col].value_counts().sort_index()
        plt.bar(x=df_i.index,
              bottom=stack,
              height=df_i.values,
              label=i,
              alpha=.9)
        stack += df_i


    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.legend()
    plt.show()
df = pd.read_csv('https://raw.githubusercontent.com/Raven-ES1617/cu/main/datasets/week2/diamonds.csv')
df["cut"] = df["cut"].str.replace("ideal", "Ideal")
plot_stacked_bar(df, groupby_col= 'cut', category_col= 'color', xlabel= 'Цвет', ylabel= 'Огранка', title= 'Частота огранки по цветам')

def price_range(price):
    if price < 3000:
        return 'низкий'
    elif 3000 <= price <= 12000:
        return 'средний'
    else:
        return 'высокий'

df['category'] = df['price'].apply(price_range)
df_1 = df.groupby('category').agg('count').reset_index()
df_1 = df_1[['category', 'carat']]
df_1 = df_1.rename(columns= {'carat' : 'count'})
df_1 = df_1.assign(color = ['red', 'blue', 'green'])
print(df_1)
plt.title('Доля алмазов по ценовым категориям')
plt.pie(df_1['count'], labels = df_1['category'],autopct='%1.1f%%', colors = df_1['color'])
plt.show()
df_2 = df.groupby('category').agg({'price' : ['sum']}).reset_index()
df_2.columns = ['category', 'total_sum']
df_2 = df_2.assign(share = df_2['total_sum']/ sum(df_2['total_sum']))
print(df_2)
plt.title('Доля алмазов по выручке')
plt.pie(df_2['share'], labels = df_2['category'],  autopct='%1.1f%%')
plt.show()