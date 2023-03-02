import pandas as pd
import tabula as tb

df_new = tb.read_pdf(r"C:\Users\Evan Mc Garry\Desktop\FDS\Homework1\GDP11.pdf", area = (89, 0, 650, 365), pages = '1', stream=True)
df_new = df_new[0]
df_new.rename(columns={'USA':'', '1':'Ranking', 'United States':'Economy', '20,936,600':'(millions of US Dollars)'}, inplace=True)
print(df_new.columns)

new_row = pd.DataFrame({'':'USA', 'Ranking':1, 'Economy':'United States', '(millions of US Dollars)':'20,936,600'}, index=[0])
df = pd.concat([new_row,df_new.loc[:]]).reset_index(drop=True)
[print(df)]

print(df.to_latex(index=False))