import pandas as pd
import csv
import sys

def drop_cols(df, drop_list, col): 

	for i in drop_list:
		df = df[df[col].str.contains(i) == False]

	return(df)

if __name__ == "__main__":

	if len(sys.argv) != 4: 
		sys.exit('Please provide FAOSTAT code and path to out file directory.')
	else: 
		in_path = sys.argv[1]
		in_file = sys.argv[2]
		outpath = sys.argv[3]

	out_name = in_file[:-4]

	if out_name == 'FAOSTAT_EF':

		df = pd.read_csv('%s/%s' % (in_path, in_file), encoding = "ISO-8859-1")
		df = df[df['Unit'].str.contains('kilotonnes') == False]
		drop_cols = ['Area Code','Area Code (M49)', 'Element Code', 'Year Code', 'Source Code','Unit']
		df = df.drop(columns=drop_cols)

		df.columns = ['area','Item Code','Item Code (CPC)','species','table_name','year','source','value','flag']
		# Source
		sources = df['source'].unique()
		for i in sources: 

			df_out = df.loc[df['source'] == i]	
			i = i.replace(" ","")	
			df_out.to_csv('%s/%s_%s.csv' % (outpath, out_name, i), index = False)

	elif out_name == 'FAOSTAT_QCL': 

		df = pd.read_csv('%s/%s' % (in_path, in_file), encoding = "ISO-8859-1")
		df = df.drop(columns = ['Area Code','Element Code','Year Code'])
		drop_units = ['ha', 'hg/ha', 'tonnes', '100mg/An','hg/An', '0.1g/An', '1000 No', 'No/An', 'hg']
		drop_item = ['Snails, not sea','Honey, natural','Beehives', 'Beeswax']

		df = drop_cols(df, drop_units, 'Unit')
		df = drop_cols(df, drop_item, 'Item')

		tables = df['Element'].unique()
		for i in tables:

			df_out = df.loc[df['Element'] == i]

			df_out.columns = ['area','Item Code', 'species', 'table_name', 'year', 'Unit', 'Value', 'Flag']

			if i == 'Producing Animals/Slaughtered':
				i = 'Producing Animals Slaughtered'
			i = i.replace(" ","")
			df_out.to_csv('%s/%s_%s.csv' % (outpath, out_name, i), index = False)
