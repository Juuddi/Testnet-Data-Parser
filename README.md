# Testnet-Data-Parser

This repository helps sort through post testnet data to determine community $QUAI rewards. 
In order for the algorithm to function correctly, all of the .csv files must be uploaded, named, and formatted as the ones currently in the repo.

dataparser.py takes in 5 .csv files, 2 of which contain testnet mined block and transaction data, and the other 3 containing user generate data
from testnet submission forms. dataparser.py outputs a compiled rewards dictionary to a .csv of your choice for easy communication with existing bot architecture.

All of the submission form generated .csvs must be ran thru an additional data parser to remove extraneous responses. For bronze age testnet data, this
additional parsing was done using a matlab script. In future iterations, the matlab script functionality will be moved into python for simplicity and
ease of use for the rest of the team.
