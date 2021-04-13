import pandas as pd

df = pd.read_csv("by_department.csv")
df[df["department"]=="IT Support"].to_csv('itsupport.csv', index=False)
