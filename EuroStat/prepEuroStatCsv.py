import pandas as pd
import sys
import os

file = sys.argv[1]

df = pd.read_csv(file)

df.columns = df.columns.str.lower()
df = df[(df['value'] != ':')]

table_name = os.path.basename(file[:-11])

df = df.assign(tablename = table_name)

cat_yr = df.groupby(['animals'])['time'].unique().apply(list).reset_index()
cat_area_yr = df.groupby(['animals','geo'])['time'].unique().apply(list).reset_index()
table_yr = df.groupby('tablename')['time'].unique().apply(list).reset_index()

cat_yr = cat_yr.assign(tablename = table_name)
cat_area_yr = cat_area_yr.assign(tablename = table_name)

outfile_table_yr = '%s_%s' % (file[:-4], 'table_yr.csv')
outfile_cat_yr = '%s_%s' % (file[:-4], 'cat_yr.csv')
outfile_cat_area_yr = '%s_%s' % (file[:-4], 'cat_area_yr.csv')

cat_yr.to_csv(outfile_cat_yr, index=False)
cat_area_yr.to_csv(outfile_cat_area_yr, index=False)
table_yr.to_csv(outfile_table_yr, index=False)