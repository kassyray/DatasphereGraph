#!/bin/bash

DATADIR='/Users/kassyraymond/PhD/trunk/DatasphereGraph/EthCSA'
outfile='EthCSA_allCats.csv'

for file in 2020_185.csv 2020_186.csv 2020_187.csv 2020_188.csv 2020_189.csv 2020_190.csv
do
	python cleanEth.py ${DATADIR}/${file} ${DATADIR}
done

for file in EthCSA_Camels.csv EthCSA_Donkeys.csv EthCSA_Horses.csv EthCSA_Poultry.csv EthCSA_Cattle.csv EthCSA_Goats.csv EthCSA_Mules.csv EthCSA_Sheep.csv
do
	tail -n +2 ${DATADIR}/${file} >> ${DATADIR}/${outfile}
done