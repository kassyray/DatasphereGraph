import pandas as pd
import sys
import json
import requests 
from pyjstat import pyjstat
from collections import OrderedDict
from datetime import date
import data_helpers as dh

if __name__ == "__main__":
    
	if len(sys.argv) != 3: 
		sys.exit('Please provide a table name and outpath')
	else: 
		dataset_code = sys.argv[1]
		outpath = sys.argv[2]

	# Prep url
	url = 'https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/'
	format_type = '?format=JSON'
	content_url = '%s%s%s' % (url, dataset_code, format_type)

	# Get data 
	df = dh.get_jsonstat(content_url)

	if (dataset_code == 'apro_mt_lscatl') or (dataset_code == 'apro_mt_lspig'):
		df.columns = ['Time frequency', 'species', 'Month', 'Unit of measure', 'area', 'year', 'value']

	else:

		if len(df.columns) == 6:
			df.columns = ['Time frequency', 'species', 'Unit of measure', 'area', 'year', 'value']

		elif len(df.columns) == 7: 
			df.columns = ['Time frequency', 'Month', 'species', 'Unit of measure', 'area', 'year', 'value']

		else: 
			df.to_csv('%s/%s_%s.csv' % (outpath, source, dataset_code), index = False)
			sys.exit('Unexpected number of columns retrieved. Dataset saved without renaming columns.')

	# Prep data format for graphdb
	df = df[df['value'].notna()].reset_index(drop=True)
	df = df.sort_values(by=['year'])

	source = 'EuroStat'

	df.to_csv('%s/%s_%s.csv' % (outpath, source, dataset_code), index = False)










	
	

