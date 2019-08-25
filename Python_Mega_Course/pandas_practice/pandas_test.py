import pandas

df1 = pandas.DataFrame([[2, 4, 6], [10, 20, 30]])
print(df1)
"""
    0   1   2
0   2   4   6
1  10  20  30
"""

df1 = pandas.DataFrame([[2, 4, 6], [10, 20, 30]], columns=["Price", "Age", "Value"], index=["First", "Second"])
print(df1)
"""
        Price  Age  Value
First       2    4      6
Second     10   20     30
"""

df2 = pandas.DataFrame([{"Name": "Abhijeet", "Surname": "Roy"}, {"Name": "Arijeet"}])
print(df2)
"""
       Name Surname
0  Abhijeet     Roy
1   Arijeet     NaN
"""

print(df1.mean())
"""
Price     6.0
Age      12.0
Value    18.0
dtype: float64
"""

print(df1.mean().mean())
# 12.0
print(df1.Price)
"""
First      2
Second    10
Name: Price, dtype: int64
"""
print(df1.Price.max())
# 10
