from turtle import addshape
import pandas as pd

#minedBlocks = pd.read_csv(r"AggregateBlkData.csv", usecols = ['Prime', 'Region1', 'Region2', 'Region3', 'Zone11', 'Zone12', 'Zone13', 'Zone21', 'Zone22', 'Zone23', 'Zone31', 'Zone32', 'Zone33'])
#txs = pd.read_csv(r"AggregateTxData.csv", usecols = ['Prime', 'Region1', 'Region2', 'Region3', 'Zone11', 'Zone12', 'Zone13', 'Zone21', 'Zone22', 'Zone23', 'Zone31', 'Zone32', 'Zone33'])
df = pd.read_csv(r"Addresses.csv", usecols = ["Total", "Discord User Names"])

# Notes for tomorrow: compile addresses spreadsheet into 2 columns - split addresses from 1 single column


#Use functions var.split and var.lower to lowercase and split all addresses into lists


#Create dictionary with key: discord name and value: addresses 
#Dictionary has been verified against original dataset!!
dicts = {}

for y, row in df.iterrows():
    user = str(row["Discord User Names"])
    adds = str(row["Total"])
    #adds = adds.lower()
    #adds = adds.split(", ")
    dicts[user] = adds
        



# Create user dictionary from csv with user discord names and addresses, i.e. tie the user to their addresses
# Dataframe with value count for each address in mined blocks csv
# Create first for loop iterating thru each mined address value count
# nested Within that, create another for loop that checks if address is in array of users addresses
# If address is in the array, add value count to rewards value in user dictionary 