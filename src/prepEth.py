import pandas as pd
import sys
import data_helpers as dh
import os

if __name__ == "__main__":

	file_path = sys.argv[1]
	table_name = sys.argv[2]
	df = pd.read_csv(file_path, sep = ';')
	df.columns = ['species','year','table_name']
	source = 'Ethiopia Central Statistics Agency Agricultural Sample Survey'
	df['source'] = source
	df['area'] = 'Ethiopia'
	outpath = '/Users/kassyraymond/PhD/trunk/DatasphereGraph/input_data'

	dh.get_cat_yr(df, table_name, source, outpath)
	dh.get_cat_area_yr(df, table_name, source, outpath)
	dh.get_table_yr(df, table_name, source, outpath)
	dh.get_source_yr(df, table_name, source, outpath)
