#!/bin/bash

DATADIR='/Users/kassyraymond/PhD/trunk/DatasphereGraph/data'
INDIR='/Users/kassyraymond/PhD/trunk/DatasphereGraph/input_data'

echo "Getting EuroStat data from API..."

for table in apro_mt_lscatl apro_mt_lsequi apro_mt_lsgoat apro_mt_lspig apro_mt_lssheep apro_ec_poula apro_ec_lshen
do
	echo "Processing ${table}"
	python getEuroStat.py ${table} ${DATADIR}
done

echo "Cleaning FAOSTAT data..."

for file in FAOSTAT_EF FAOSTAT_QCL
do
	echo "Processing ${file}.csv"
	python cleanFAOSTAT.py ${INDIR} ${file}.csv ${DATADIR}
done

echo "Getting WOAH data from API..."

python getWOAH.py ${DATADIR}

echo "Creating files for loading..."

for file in `ls ${DATADIR}`
do
	echo "Processing ${file}"
	python createFiles.py ${DATADIR}/${file} ${file} ${INDIR}
done

