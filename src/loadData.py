import pandas as pd
from neo4j import GraphDatabase
import csv
import sys
from graph_helpers import graph
import os.path

if __name__ == "__main__":

    # Get info
    if len(sys.argv) != 3: 
        sys.exit('Please provide correct system arguments.')
    else:
        source_table = sys.argv[1]
        indir = sys.argv[2]

    # Connect with graph
    graph_db = graph("bolt://localhost:7687", "neo4j", "asdf")

    # Read files 
    cat_area_yr = pd.read_csv('%s/%s_cat_area_yr.csv' % (indir, source_table))
    cat_yr = pd.read_csv('%s/%s_cat_yr.csv' % (indir, source_table))
    table_yr = pd.read_csv('%s/%s_table_yr.csv' % (indir, source_table))

    # Get info
    source = source_table.split('_')[0]
    table_name = table_yr['table_name'].iloc[0]
    table_year = table_yr['year'].iloc[0]

    if source == 'FAOSTAT':
        if table_name == 'FAOTIER1' or table_name == 'UNFCCC':
            source = 'FAOSTAT Enteric Fermentation'
        else: 
            source = 'FAOSTAT Production: Crops and livestock products'

    # Load source node 
    result = graph_db.check_if_exists(source)
    if result == None: 
       graph_db.print_datasource(source)

    # Load table
    graph_db.print_create_return_table(source, table_name, table_year)

    # Load categories 
    for i in range(0, cat_yr.shape[0]):
        table_name = cat_yr['table_name'].iloc[i]
        item = cat_yr['species'].iloc[i]
        year = cat_yr['year'].iloc[i]
        graph_db.print_create_return_category(table_name, item, year)
    
    for i in range(0, cat_area_yr.shape[0]):
        item = cat_area_yr['species'].iloc[i]
        area = cat_area_yr['area'].iloc[i]
        year = cat_area_yr['year'].iloc[i]
        table_name = cat_area_yr['table_name'].iloc[i]
        if 'FAOSTAT' in source:
            graph_db.create_return_fao_area(item, area, year, table_name)
        elif source == 'EuroStat':
            graph_db.print_create_return_eurostat_area(item, area, year, table_name)
        elif source == 'WOAH':
            graph_db.print_create_return_woah_area(item, area, year, table_name)
        elif source == 'Ethiopia Central Statistics Agency Agricultural Sample Survey':
            graph_db.print_create_return_eth_area(item, area, year, table_name)
        

    