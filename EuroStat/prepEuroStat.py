import pandas as pd
import sys
import json

def split_clean_cols(df, months = False): 
	if months == True: 
		df[['animals','month','unit','geo']] = df['animals,month,unit,geo'].str.split(',', expand = True)
		df = df.drop(columns = ['animals,month,unit,geo'])
		df.columns = df.columns.str.replace(' ','')
	else:
		df[['animals','unit','geo']] = df['animals,unit,geo'].str.split(',', expand = True)
		df = df.drop(columns = ['animals,unit,geo'])
		df.columns = df.columns.str.replace(' ','')
	return(df)

def replace_val(df, col_dict, col): 
	with open(col_dict) as json_file:
		col_dict = json.load(json_file)
	df[col] = df[col].map(col_dict).str[0]
	return(df)

if len(sys.argv) != 5: 
	sys.exit('Please provide input file and dicts.')
else:
	file = sys.argv[1]
	animal_dict = sys.argv[2]
	geo_dict = sys.argv[3]
	unit_dict = sys.argv[4]

df = pd.read_csv(file, delimiter = '\t')

cols = df.columns.tolist()

if 'month' in cols[0]: 
	cols[0] = 'animals,month,unit,geo'
	df.columns = cols

	df = split_clean_cols(df, months = True)
	df = df.melt(id_vars=['animals','unit','geo','month'], 
	        var_name='year', 
	        value_name='population')

else: 
	cols[0] = 'animals,unit,geo'
	df.columns = cols

	df = split_clean_cols(df)
	df = df.melt(id_vars=['animals','unit','geo'], 
	        var_name='year', 
	        value_name='population')


df = replace_val(df, animal_dict, 'animals')
df = replace_val(df, unit_dict, 'unit')
df = replace_val(df, geo_dict, 'geo')

cat_yr = df.groupby(['animals'])['year'].unique().apply(list).reset_index()
cat_area_yr = df.groupby(['animals','geo'])['year'].unique().apply(list).reset_index()

out_df = '%s_cleaned.csv' % (file[:-4])
outfile_cat_yr = '%s_%s' % (file[:-4], 'cat_yr.csv')
outfile_cat_area_yr = '%s_%s' % (file[:-4], 'cat_area_yr.csv')

df.to_csv(out_df, index=False)
cat_yr.to_csv(outfile_cat_yr, index=False)
cat_area_yr.to_csv(outfile_cat_area_yr, index=False)