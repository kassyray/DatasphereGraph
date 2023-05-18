import pandas as pd
import requests
import csv
import sys
import data_helpers as dh

if __name__ == "__main__":

	in_file = sys.argv[1]
	file_name = sys.argv[2]
	outpath = sys.argv[3]

	source = file_name.split('_')[0]

	if source == 'EuroStat': 
		table_name = file_name[9:-4]

	elif source == 'WOAH':
		table_name = 'WOAHpopulation'

	elif source == 'FAOSTAT':
		table_name = file_name.split('_')[2]
		table_name = table_name[:-4]

	df = pd.read_csv(in_file)

	dh.get_cat_yr(df, table_name, source, outpath)
	dh.get_cat_area_yr(df, table_name, source, outpath)
	dh.get_table_yr(df, table_name, source, outpath)
	dh.get_source_yr(df, table_name, source, outpath)

	