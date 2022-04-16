import pandas as pd

#Import .csvs
minedBlocks = pd.read_csv(r"AggregateBlkData.csv", usecols = ['Prime', 'Region1', 'Region2', 'Region3', 'Zone11', 'Zone12', 'Zone13', 'Zone21', 'Zone22', 'Zone23', 'Zone31', 'Zone32', 'Zone33'])
txs = pd.read_csv(r"AggregateTxData.csv", usecols = ['Prime', 'Region1', 'Region2', 'Region3', 'Zone11', 'Zone12', 'Zone13', 'Zone21', 'Zone22', 'Zone23', 'Zone31', 'Zone32', 'Zone33'])
mineradds = pd.read_csv(r"Addresses.csv", usecols = ["Total", "Discord User Names"])
citizenadds = pd.read_csv(r"CitizenData.csv", usecols = ["Discord User Names", "Wallet Addresses"])
nodes = pd.read_csv(r"NodeData.csv", usecols = ["Discord User Names", "Node Amount", "Node Type"])

#Make all .csvs the same case
minedBlocks = minedBlocks.applymap(lambda s: s.lower() if type(s) == str else s)
txs = txs.applymap(lambda s: s.lower() if type(s) == str else s)

#NodeData.csv still needs to be created with the format shown in the algorithm below
#Create node-reward/discord username dictionary
noderewards = {}
for x, row in nodes.iterrows():
    operator = str(row["Discord User Names"])
    numberOfNodes = row["Node Amount"]
    nodeType = row["Node Type"]
    nodeType = nodeType.lower()
    if nodeType == "full node":
        multiplier = 1000
    if nodeType == "slice node":
        multiplier = 200
    if nodeType == "nan":
        multiplier = 0
    reward = multiplier*numberOfNodes
    noderewards[operator] = reward

#Create miner address/discord user name dictionary, split by commas and make lowercase
mineraddresses = {}
for x, row in mineradds.iterrows():
    miner = str(row["Discord User Names"])
    adds = str(row["Total"])
    adds = adds.lower()
    adds = adds.split(", ")
    mineraddresses[miner] = adds

#Create citizen address/discord username dictionary, split by commas and make lowercase
citizenaddresses = {}
for x, row in citizenadds.iterrows():
    citizen = str(row["Discord User Names"])
    adds = str(row["Wallet Addresses"])
    adds = adds.lower()
    adds = adds.split(", ")
    citizenaddresses[citizen] = adds

#Compare mineraddresses against minedBlocks to generate rewards dictionary
minerrewards = {}
for k, v in mineraddresses.items():
    miner = k
    addresses = v
    reward = 0
    for i in addresses:
        if i == "nan":
            continue
        filtereddf = minedBlocks.loc[minedBlocks["Prime"] == i]
        primeidx = len(filtereddf)
        filtereddf = minedBlocks.loc[minedBlocks["Region1"] == i]
        r1idx = len(filtereddf)
        filtereddf = minedBlocks.loc[minedBlocks["Region2"] == i]
        r2idx = len(filtereddf)
        filtereddf = minedBlocks.loc[minedBlocks["Region3"] == i]
        r3idx = len(filtereddf)
        filtereddf = minedBlocks.loc[minedBlocks["Zone11"] == i]
        z11idx = len(filtereddf)
        filtereddf = minedBlocks.loc[minedBlocks["Zone12"] == i]
        z12idx = len(filtereddf)
        filtereddf = minedBlocks.loc[minedBlocks["Zone13"] == i]
        z13idx = len(filtereddf)
        filtereddf = minedBlocks.loc[minedBlocks["Zone21"] == i]
        z21idx = len(filtereddf)
        filtereddf = minedBlocks.loc[minedBlocks["Zone22"] == i]
        z22idx = len(filtereddf)
        filtereddf = minedBlocks.loc[minedBlocks["Zone23"] == i]
        z23idx = len(filtereddf)
        filtereddf = minedBlocks.loc[minedBlocks["Zone31"] == i]
        z31idx = len(filtereddf)
        filtereddf = minedBlocks.loc[minedBlocks["Zone32"] == i]
        z32idx = len(filtereddf)
        filtereddf = minedBlocks.loc[minedBlocks["Zone33"] == i]
        z33idx = len(filtereddf)

        reward = primeidx+r1idx+r2idx+r3idx+z11idx+z12idx+z13idx+z21idx+z22idx+z23idx+z31idx+z32idx+z33idx
        minerrewards[miner] = reward

#Compare citizenaddresses against txs to generate citizen rewards
citizenrewards = {}
for k, v in citizenaddresses.items():
    k = citizen
    v = addresses
    rewards = 0
    for i in addresses:
        if i == "nan":
            continue
        filtereddf = txs.loc[txs["Prime"] == i]
        primeidx = len(filtereddf)
        filtereddf = txs.loc[txs["Region1"] == i]
        r1idx = len(filtereddf)
        filtereddf = txs.loc[txs["Region2"] == i]
        r2idx = len(filtereddf)
        filtereddf = txs.loc[txs["Region3"] == i]
        r3idx = len(filtereddf)
        filtereddf = txs.loc[txs["Zone11"] == i]
        z11idx = len(filtereddf)
        filtereddf = txs.loc[txs["Zone12"] == i]
        z12idx = len(filtereddf)
        filtereddf = txs.loc[txs["Zone13"] == i]
        z13idx = len(filtereddf)
        filtereddf = txs.loc[txs["Zone21"] == i]
        z21idx = len(filtereddf)
        filtereddf = txs.loc[txs["Zone22"] == i]
        z22idx = len(filtereddf)
        filtereddf = txs.loc[txs["Zone23"] == i]
        z23idx = len(filtereddf)
        filtereddf = txs.loc[txs["Zone31"] == i]
        z31idx = len(filtereddf)
        filtereddf = txs.loc[txs["Zone32"] == i]
        z32idx = len(filtereddf)
        filtereddf = txs.loc[txs["Zone33"] == i]
        z33idx = len(filtereddf)    
        
        reward = primeidx+r1idx+r2idx+r3idx+z11idx+z12idx+z13idx+z21idx+z22idx+z23idx+z31idx+z32idx+z33idx
        citizenrewards[citizen] = reward

#Last thing that needs to be done - combine all rewards dictionaries in some fashion and write them all to a .csv file