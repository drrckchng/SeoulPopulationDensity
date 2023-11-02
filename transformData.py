import pandas as pd

df = pd.read_csv('mois_pop_gu_data.csv', header=0)
df = df[df['기간'] >= 1995]

pivot_df = df.pivot(index='자치구', columns='기간', values='인구')
pivot_df.fillna(0, inplace=True)

pivot_df = pivot_df.astype(int)

pivot_df.to_csv('transformed_seoul_pop_data.csv')
