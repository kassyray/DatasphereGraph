#!/bin/bash

DATADIR='/Users/kassyraymond/PhD/trunk/DatasphereGraph/EuroStat/inFilesCSV'

for file in apro_ec_lshen apro_mt_lscatl apro_mt_lsequi apro_mt_lsgoat apro_mt_lspig apro_mt_lssheep
do
	inFile="${DATADIR}/${file}_1_Data.csv"
	echo "Processing ${file}"
	python prepEuroStatCsv.py ${inFile} 
done