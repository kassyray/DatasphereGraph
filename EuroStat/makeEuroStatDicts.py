import pandas as pd
import json

def make_save_dict(file, out_file): 
	df = pd.read_csv(file, delimiter = '\t', header = None)
	out_dict = df.set_index(0).T.to_dict('list')
	json.dump(out_dict, open(out_file,'w'))

# IMPORT FILES
files = ['ESTAT_ANIMALS_en.tsv', 'ESTAT_UNIT_en.tsv', 'ESTAT_GEO_en.tsv']

for file in files: 
	out_name = '%s.json' % file[:-4]
	make_save_dict(file, out_name)

