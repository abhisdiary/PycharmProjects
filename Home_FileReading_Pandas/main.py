import pandas

df1 = pandas.read_csv("res/supermarkets.csv")  # reading csv
df2 = pandas.read_json("res/supermarkets.json")  # reading json
df3 = pandas.read_excel("res/supermarkets.xlsx", sheet_name=0)  # reading excel
df4 = pandas.read_csv("res/supermarkets-commas.txt")  # reading text; comma separator
df5 = pandas.read_csv("res/supermarkets-semi-colons.txt", sep=";")  # reading text; semi-colon separator

print(df2)  # pandas automatically takes the first row as header

# If this happens that we don not have any header in our data
df5 = pandas.read_csv("res/supermarkets-semi-colons.txt", sep=";", header=None)  # No Header
print(df5)

# Custom Column Name
df5.columns = ["Col1", "Col2", "Col3", "Col4", "Col5", "Col6", "Col7"]
print(df5)

# Setting up a new index column
df6 = df2.set_index("Name", drop=False)  # drop = false does not delete the actual column from its place
print(df6)

# Accessing the data from the table
city = df6.loc["Sanchez", "City"]
print(city)
print(list(df6.loc[:, "Name"]))
print(list(df6.loc["Richvalley", :]))

print("==== Select Row (Madeira to Super River) & Column (Address to Country) ====")
portion_of_table = df6.loc["Madeira":"Super River", "Address":"Country"]  # ':' means 'to'
print(portion_of_table)

print("==== Select Row: 1 to 4 & Column: 2 to 4 ====")
portion_of_table = df6.iloc[1:4, 2:4]  # select portion by row & column number
print(portion_of_table)

print("==== Select all Rows ====")
portion_of_table = df6.iloc[:, 2:4]  # select all rows
print(portion_of_table)

print("==== Select Row 3 ====")
portion_of_table = df6.iloc[3, 2:4]  # select row number 3
print(portion_of_table)

print("==== Delete Column ====")
column_deleted = df6.drop("City", 1)  # 1 is used to denote column & 0 for row
print(column_deleted)

print("==== Delete Row ====")
row_deleted = df6.drop("Sanchez", 0)  # 1 is used to denote column & 0 for row
print(row_deleted)

# row_deleted_by_indexing = df6.drop(df6.index[0:1, 0])  # delete by indexing
# print(row_deleted_by_indexing)

print("==== Printing Row and Column Indexes ====")
row_indexes = df1.index
column_indexes = df1.columns
print(row_indexes)
print(column_indexes)

print("===== Print Row and Column Number =====")
print(df5.shape)

print("==== Update or Add new Column ====")
df4["Continent"] = df4.shape[0] * ["North America"]
print(df4)
df4["Continent"] = df4["City"] + "," + "North America"
print(df4)

print("==== Update or Add new Rows ====")
df1_drop = df1.drop("ID", 1)
print(df1_drop.set_index("Address"))  # Making the Address column as index for rows
df1_T = df1_drop.T  # Making the data frame transpose (rows become column and vice versa)
print(df1_T)
df1_T["My Address"] = ["My City", "My Country", 10, 7, "My State", "My Continent"]
print(df1_T.T)
