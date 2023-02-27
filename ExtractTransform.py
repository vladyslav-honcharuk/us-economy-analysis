import pandas as pd

sheets = ["2021","2020","2019","2018","2017","2016","2015","2014","2013","2012","2011",
          "2010","2009","2008","2007","2006","2005","2004","2003","2002","2001",
          "2000","1999","1998","1997","1996","1995","1994","1993","1992"]


def preprocess_sheet(n_sheet):
    """Loads every sheet from mrts data stored in .xls file and runs a series of data cleaning procedures"""
    
    #import data and skip some rows from the top and the bottom of the sheet
    df = pd.read_excel("mrtssales92-present.xls", sheet_name=n_sheet, skiprows=4, skipfooter=47)
    #drops the first and the last columns
    df.drop(df.columns[[0,14]], axis=1, inplace=True)
    #renames the column that contain a kind of business
    df.rename(columns={"Unnamed: 1": "Kind of Business"}, inplace=True)
    
    #transponation of the DataFrame
    df_melted = df.melt(id_vars="Kind of Business", value_vars=df.columns[1:])
    #imputation of the categorical values that represent missing values
    df_melted.replace(["(S)", "(NA)"], "0", inplace=True)
    #drops the missing values
    df_melted.dropna(axis=0, inplace=True)

    #casts the data that represent revenue to the float type
    df_melted["value"] = df_melted["value"].astype(float)
    df_melted.rename(columns={"variable": "period"}, inplace=True)
    #casts the data that represent revenue to the datetime64[ns] type
    df_melted = df_melted.astype({"period": "datetime64[ns]"})
    
    return df_melted

#runs the preprocess_sheet(n_sheet) function for each sheet of the .xls file
df_complete = preprocess_sheet(sheets[1])
for i in sheets[2:]:
    df_complete = pd.concat([df_complete, preprocess_sheet(i)])

#creates unique index for each record of data 
df_complete.index = range(22236)

#saves transformed data into Comma-Separated Values file
df_complete.to_csv("mrts.csv")

