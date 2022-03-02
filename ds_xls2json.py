import os
import json
import pandas as pd
from byoi_utility.xls2json import build_import
os.chdir('C:/User/')

test = build_import('data-collection.xls')

with open('data-collection-batchFile.json', 'w') as outfile:
    json.dump(test, outfile)
