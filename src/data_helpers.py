import pandas as pd
import sys
import json
import requests 
from pyjstat import pyjstat
from collections import OrderedDict
from datetime import date
import csv

def make_call(url): 

	with requests.Session() as s:
		download = s.get(url)

		decoded_content = download.content.decode('utf-8')

		cr = csv.reader(decoded_content.splitlines(), delimiter=',')
		my_list = list(cr)

	return(my_list)

def get_jsonstat(url): 

	try: 
		data = requests.get(url)
		results = pyjstat.from_json_stat(data.json())

		for i in results:
			df = pd.DataFrame(i)
	except: 
		sys.exit('Something went wrong with the request')

	return(df)

def get_cat_yr(df, table_name, source, outpath):

	cat_yr = df.groupby(['species'])['year'].unique().apply(list).reset_index()
	cat_yr = cat_yr.assign(table_name = table_name)
	cat_yr.to_csv('%s/%s_%s_cat_yr.csv' % (outpath, source, table_name), index = False)

	return()

def get_cat_area_yr(df, table_name, source, outpath): 

	cat_area_yr = df.groupby(['species','area'])['year'].unique().apply(list).reset_index()
	cat_area_yr = cat_area_yr.assign(table_name = table_name)
	cat_area_yr.to_csv('%s/%s_%s_cat_area_yr.csv' % (outpath, source, table_name), index = False)

	return()

def get_table_yr(df, table_name, source, outpath):

	df = df.assign(table_name = table_name) 
	table_yr = df.groupby('table_name')['year'].unique().apply(list).reset_index()
	table_yr.to_csv('%s/%s_%s_table_yr.csv' % (outpath, source, table_name), index = False)

	return()

def get_source_yr(df, table_name, source, outpath):

	df = df.assign(source = source) 
	source_yr = df.groupby('source')['year'].unique().apply(list).reset_index()
	source_yr.to_csv('%s/%s_%s_yr.csv' % (outpath, source, table_name), index = False)

	return()


