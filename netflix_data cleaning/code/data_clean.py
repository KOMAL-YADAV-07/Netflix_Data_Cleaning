import pandas as pd


""" loading the data """
df = pd.read_csv("data\movies_netflix.csv")


""" Basic information about data """
print(df.info())
print("First 5 rows:")
print(df.head())
print(df.isnull().sum())



""" Handling missing values """
df["director"].fillna("Not Available", inplace=True)
df["cast"].fillna("Not Available", inplace=True)
df["country"].fillna("Unknown", inplace=True)
df["rating"].fillna(df["rating"].mode()[0], inplace=True)


""" Droping columns with null values """
df.dropna(subset=["date_added"], inplace=True)


""" changing date column to date format """
df["date_added"] = df["date_added"].str.strip()
df['date_added'] = pd.to_datetime(df['date_added'])


""" clean duration column """
df["duration_type"] = df["duration"].str.replace('\d+','', regex=True).str.strip()
df["duration_number"] = df["duration"].str.extract('(\d+)').astype(int)


""" droping duplicate values """
df.drop_duplicates(inplace=True)
df.columns = df.columns.str.lower().str.strip()
print(df.info())






