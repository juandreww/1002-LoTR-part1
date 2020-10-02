import pandas as pd

#Lord of The Rings
dataframe = pd.read_csv("D:/Downloads D/archive/WordsByCharacter.csv")
print(dataframe)
print(dataframe.index.names)
print("#Lanjut\n")
multi = dataframe.set_index(['Film', 'Chapter', 'Race', 'Character']).sort_index()
print(multi.index.names)
print(multi.index.values)
print(multi.reset_index())
print(multi.loc[('The Two Towers', '64: Farewell To Faramir'), :])
print(multi.loc[('The Two Towers', '58: Forth Eorlingas'), :])
print(multi.loc[('The Two Towers'), :])
print(multi.loc[('The Two Towers',slice(None),slice(None),['Gandalf','Aragorn']), :])
print("total :",multi.xs('Aragorn', level='Character').sum())

#Pivot Table
print("#Ini Pivot Table\n")
pivoted = dataframe.pivot_table(index = ['Race', 'Character'],
                                columns = 'Film',
                                aggfunc = 'sum',
                                margins = True, # total column
                                margins_name= 'All Films',
                                fill_value= 0).sort_index()

order = [('Words', 'The Two Towers'),
         ('Words', 'The Fellowship Of The Ring'),
         ('Words', 'The Return Of The King'),
         ('Words', 'All Films')]

pivoted = pivoted.sort_values(by=('Words', 'All Films'), ascending=False)
pivoted = pivoted.reindex(order, axis=1)
print(pivoted)
