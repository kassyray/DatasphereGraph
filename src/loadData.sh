#!/bin/bash

DATADIR='/Users/kassyraymond/PhD/trunk/DatasphereGraph/input_data'

for source in FAOTIER1 UNFCCC Laying Stocks MilkAnimals ProducingAnimalsSlaughtered
do
    echo "Loading FAOSTAT data FAOSTAT_${source}...."
    python loadData.py FAOSTAT_${source} ${DATADIR}
done

for table_source in EuroStat_apro_ec_lshen EuroStat_apro_ec_poula EuroStat_apro_mt_lsequi EuroStat_apro_mt_lsgoat EuroStat_apro_mt_lspig EuroStat_apro_mt_lssheep
do
    echo "Loading EuroStat data ${table_source}...."
    python loadData.py ${table_source} ${DATADIR}
done

echo "Loading WOAH data..."
python loadData.py WOAH_WOAHpopulation ${DATADIR}

for source in Camels Cattle Donkeys Goats Horses Mules Poultry Sheep 
do
    echo "Loading EthCSA data ${source}"
    python loadData.py Ethiopia\ Central\ Statistics\ Agency\ Agricultural\ Sample\ Survey_${source} ${DATADIR}
done 
