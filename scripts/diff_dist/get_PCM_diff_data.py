import pandas as pd
from LLRunner.read.SST import sst
from get_copath_data import get_diff


df = sst.df

# get the "Accession Number" column of df as a list of strings
case_numbers = df["Accession Number"].tolist()


print(case_numbers)