from operator import index
from numpy import number
import pandas as pd

#Import .csvs
minedBlocks = pd.read_csv(r"AggregateBlkData.csv", usecols = ['Prime', 'Region1', 'Region2', 'Region3', 'Zone11', 'Zone12', 'Zone13', 'Zone21', 'Zone22', 'Zone23', 'Zone31', 'Zone32', 'Zone33'])
txs = pd.read_csv(r"AggregateTxData.csv", usecols = ['Prime', 'Region1', 'Region2', 'Region3', 'Zone11', 'Zone12', 'Zone13', 'Zone21', 'Zone22', 'Zone23', 'Zone31', 'Zone32', 'Zone33'])
mineradds = pd.read_csv(r"Addresses.csv", usecols = ["Total", "Discord User Names"])
citizenadds = pd.read_csv(r"CitizenData.csv", usecols = ["Discord User Names", "Wallet Addresses"])
nodes = pd.read_csv(r"NodeData.csv", usecols = ["Discord User Names", "Number of Nodes", "Type of Node"])

#Make all .csvs the same case
minedBlocks = minedBlocks.applymap(lambda s: s.lower() if type(s) == str else s)
txs = txs.applymap(lambda s: s.lower() if type(s) == str else s)

# NodeData.csv still needs to be created with the format shown in the algorithm below
# Create node-reward/discord username dictionary
noderewards = {}
for x, row in nodes.iterrows():
    operator = str(row["Discord User Names"])
    numberOfNodes = row["Number of Nodes"]
    nodeType = str(row["Type of Node"])
    nodeType = nodeType.lower()
    if nodeType == "full node":
        base = 5000
        multiplier = 1000
    if nodeType == "slice node":
        base = 5000
        multiplier = 200
    if nodeType == "nan":
        base = 0
        multiplier = 0
    if numberOfNodes == "nan":
        base = 0
        multiplier = 0
    reward = multiplier*numberOfNodes + base
    noderewards[operator] = reward


#List of values to be removed from address responses
remove_values = ["0x0767d31b0d7671c3e97c6abed055a26fb59b4149", "0x11a03db52d12201e614466cb98ec5d49a1205bda", "0x3bcec1847c55246cf9ea32a5dfe652f147ac091c", "0x5e6b0261c32b25f187786612d27a39f6d0c31771", "0x1a6ad97c8f06c7ae79fea47e43a8c048da5b1f7d", "0x186da447ec1dd29cdec8cca5653ccc4fd8f9e5e3", "0x2ab56840530b1c395ecf91e5923446fa696c7933", "0x454f47e9da39a4d2cff17d7ca50757576a298fb2", "0x4c190ab6136e94b3b510172784a4fed22f566622", "0x5446d13d4907630425928fceb67ca35a6bf1bb0e", "0x677c5623aabeb5d6d978cc2ec11ac5297a8afcbd", "0x7717ddddd08eacc0bb981c47348d1ec3a99566f8", "0x8169c0a78e20ee6e5c53cc18ee2f4eb3f762ee05", "", "na", "n/a", "-", "no", "nan"]

#Create miner address/discord user name dictionary, split by commas and make lowercase
mineraddresses = {}
for x, row in mineradds.iterrows():
    miner = str(row["Discord User Names"])
    adds = str(row["Total"])
    adds = adds.lower()
    adds = adds.split(", ")
    for x in remove_values:
        valueToBeRemoved = x
        adds = list(filter((x).__ne__,adds))
    mineraddresses[miner] = adds
print(mineraddresses)

df = pd.DataFrame.from_dict(mineraddresses, orient="index")
df.to_csv("Blank.csv")

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
    if v == "nan":
        continue
    reward = 0
    for i in addresses:
        if i == "nan":
            continue
        for col in minedBlocks.columns:
             filtereddf = minedBlocks.loc[minedBlocks[col] == i]
             idx = len(filtereddf)
             reward = reward + idx
        minerrewards[miner] = reward

df = pd.DataFrame.from_dict(minerrewards, orient="index")
df.to_csv("Blank.csv")

#Compare citizenaddresses against txs to generate citizen rewards
citizenrewards = {}
for k, v in citizenaddresses.items():
    k = citizen
    v = addresses
    if v == "nan":
        continue
    rewards = 0
    for i in addresses:
        if i == "nan":
            continue
        for col in txs.columns:
            filtereddf = txs.loc[txs[col] == i]
            idx = len(filtereddf)
            reward = reward + idx
        citizenrewards[citizen] = reward

#Last thing that needs to be done - combine all rewards dictionaries in some fashion and write them all to a .csv file