import pandas as pd
import requests
import csv
import sys
import data_helpers as dh

if __name__ == "__main__":

	out_dir = sys.argv[1]

	# Get all WOAH data 
	base_url = 'http://gbadske.org:9000/GBADsLivestockPopulation/oie?species=*&year='
	df_list = []
	for year in range(2005, 2020):
		url = '%s%d&format=file' % (base_url, year)
		df = dh.make_call(url)
		df = pd.DataFrame(df[1:],columns=df[0])
		df_list.append(df)

	woah_df = pd.concat(df_list)

	woah_df.columns = ['area','year','species','population','metadataflags']

	woah_df.to_csv('%s/WOAH_data.csv' % out_dir, index = False)