#!/bin/bash

DATADIR='/Users/kassyraymond/PhD/trunk/DatasphereGraph/EthCSA'

for table in Camels Cattle Donkeys Goats Horses Mules Poultry Sheep 
do
    python prepEth.py ${DATADIR}/EthCSA_${table}.csv ${table}
done