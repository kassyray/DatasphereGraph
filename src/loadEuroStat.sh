#!/bin/bash

DATADIR='/Users/kassyraymond/PhD/trunk/DatasphereGraph/E'

for file in apro_ec_lshen apro_mt_lscatl apro_mt_lsequi apro_mt_lsgoat apro_mt_lspig apro_mt_lssheep
do
	cat_area_yr="${DATADIR}/${file}_1_Data_cat_area_yr.csv"
	cat_yr="${DATADIR}/${file}_1_Data_cat_yr.csv"
	table_yr="${DATADIR}/${file}_1_Data_table_yr.csv"
	python loadEuroStat.py 'EuroStat' ${cat_area_yr} ${cat_yr} ${table_yr}
done