# python-librarie/funcitons

# to convert into 0 and 1
sample.housing.map(dict(yes=1, no=0))
# if name is not a single word
df.Contract=df.Contract.eq('One year').mul(1)


#to drop a column
df=df.drop(['customerID'],axis='columns')

# converting 'Weight' column from float to int
df['Weight'] = df['Weight'].astype(int)

# to find total NaN in each colum
df.isnull().sum()

# to check how much unique datas in a column 
df.DeviceProtection.nunique()

# to see all data types of table
df.dtypes

# to get the index of null values
df[df['TotalCharges'].isnull()].index.tolist()

# get mean of a column
df.tenure.mean()
df.tenure.std()

# sum of  a column
df.tenure.sum()

# to get colums in df
for col in df:
    print df.col or df[col]

# all column unique data
for col in df:
    print(df[col].nunique())

# all info of dataframe
df.info()

#way to add new column with value 1
X['extra']=X['tenure']*0 +1

# row count in dataframe
len(df)

# if w=[]*5 it's a row matrix,multiply with a matrix
w=[1]*len(X.columns)
x=df.dot(w)

# sum of each row of dataframe
X.sum(axis=1)

# print a row
X.iloc[5]

# apply tanh function to each entry of a dataframe
df.apply(np.tanh)
df['column']=df['column'].apply(np.tanh)

# Transpose of a Dataframe
X.T or X.transpose()

# Replace datas of predict with 0 or 1
Y_predict[Y_predict<=0]=0
Y_predict[Y_predict>0]=1

# matrix multiplication
X.dot(Y)