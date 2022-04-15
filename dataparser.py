import pandas as pd

minedBlocks = pd.read_csv(r"AggregateBlkData", usecols = ['Prime', 'Region1', 'Region2', 'Region3', 'Zone11', 'Zone12', 'Zone13', 'Zone21', 'Zone22', 'Zone23', 'Zone31', 'Zone32', 'Zone33'])
txs = pd.read_csv(r"AggregateTxData", usecols = ['Prime', 'Region1', 'Region2', 'Region3', 'Zone11', 'Zone12', 'Zone13', 'Zone21', 'Zone22', 'Zone23', 'Zone31', 'Zone32', 'Zone33'])
#addresses = pd.read_csv(r"UserData")






# Create user dictionary from csv with user discord names and addresses, i.e. tie the user to their addresses
# Dataframe with value count for each address in mined blocks csv
# Create first for loop iterating thru each mined address value count
# nested Within that, create another for loop that checks if address is in array of users addresses
# If address is in the array, add value count to rewards value in user dictionary 