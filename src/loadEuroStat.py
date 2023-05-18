#!/usr/bin/env python3

import pandas as pd
from graph_helpers import graph
from neo4j import GraphDatabase
import sys

graph_db = graph("bolt://localhost:7687", "neo4j", "asdf")

datasource = sys.argv[1]
cat_area_yr = sys.argv[2]
cat_yr = sys.argv[3]
table_yr = sys.argv[4]

cat_area_yr = pd.read_csv(cat_area_yr)
cat_yr = pd.read_csv(cat_yr)
table_yr = pd.read_csv(table_yr)

#graph_db.print_datasource(datasource)
source = table_yr['tablename'].iloc[0]
year = table_yr['tablename'].iloc[0]
# graph_db.print_create_return_table(datasource, source, year)

# for i in range(0, cat_yr.shape[0]):
#     source = cat_yr['tablename'].iloc[i]
#     year = cat_yr['time'].iloc[i]
#     item = cat_yr['animals'].iloc[i]
#     graph_db.print_create_return_category(source, item, year)

for i in range(0, cat_area_yr.shape[0]):
    source = cat_area_yr['tablename'].iloc[i]
    year = cat_area_yr['time'].iloc[i]
    item = cat_area_yr['animals'].iloc[i]
    area = cat_area_yr['geo'].iloc[i]
    graph_db.print_create_return_eurostat_area(item, area, year, source)