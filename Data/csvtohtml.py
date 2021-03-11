#import pandas
import pandas as pd 
import os


#path for csv
csv_path = "Data/cities.csv"

df= pd.read_csv(csv_path)


#convert csv to data frame
df_=pd.DataFrame(df)
#convert dataframe to html table
html_df= df_.to_html()

with open("html_df.html","w") as file:
    file.write(html_df)



