#!/usr/bin/env python3

from unittest import result
from neo4j import GraphDatabase

class graph:

    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()
    
    def check_if_exists(self, name):
        with self.driver.session() as session:
            check = session.write_transaction(self._check_if_exists, name)
            return(check)

    def print_datasource(self, name):
        print(name)
        with self.driver.session() as session:
            name_node = session.write_transaction(self._create_and_return_source, name)
            print(name_node)
    
    def print_create_return_table(self, source_name, table_name, year):
        with self.driver.session() as session: 
            table = session.write_transaction(self._create_return_table, source_name, table_name, year)
            print(table)
    
    def print_create_return_category(self, table_name, item_name, year):
        with self.driver.session() as session: 
            item = session.write_transaction(self._create_return_category, table_name, item_name, year)
            print(item)
    
    def create_return_fao_area(self, item_name, area_name, year, source):
        with self.driver.session() as session:
            item = session.write_transaction(self._create_return_fao_area, item_name, area_name, year, source)
            print(item)

    def print_create_return_woah_area(self, item_name, area_name, year, source):
        with self.driver.session() as session:
            item = session.write_transaction(self._create_return_woah_area, item_name, area_name, year, source)
            print(item)

    def print_create_return_eurostat_area(self, item_name, area_name, year, source):
        with self.driver.session() as session:
            item = session.write_transaction(self._create_return_eurostat_area, item_name, area_name, year, source)
            #print(item)

    def print_create_return_eth_area(self, item_name, area_name, year, source):
        with self.driver.session() as session:
            item = session.write_transaction(self._create_return_eth_area, item_name, area_name, year, source)

    @staticmethod
    def _check_if_exists(tx, name):
        result = tx.run("MATCH (n:Datasource) "
                        "WHERE n.name = $name "
                        "RETURN n", name=name)
                    
        return result.single()

    @staticmethod
    def _create_and_return_source(tx, name):
        result = tx.run("CREATE (d:Datasource) "
                        "SET d.name = $name "
                        "RETURN d.name", name=name)
        return result.single()[0]
    
    @staticmethod
    def _create_return_table(tx, source_name, table_name, year):
        result = tx.run("MATCH (d:Datasource) "
                        "WHERE d.name = $source_name "
                        "CREATE (d)-[s:HAS_TABLE]->(t:table) "
                        "SET s.year = $year "
                        "SET t.name = $table_name "
                        "RETURN t.name", source_name = source_name, year = year, table_name = table_name)
        return result.single()[0]
    
    @staticmethod
    def _create_return_category(tx, table_name, item_name, year): 
        result = tx.run("MATCH (t:table) "
                        "WHERE t.name = $table_name "
                        "MERGE (c:Category {name: $item_name}) "
                        "MERGE (t)-[r:HAS_CATEGORY]->(c) "
                        "SET r.year = $year "
                        "RETURN c.name, t.name", table_name = table_name, item_name = item_name, year = year)
        return result.single()[0]
    
    @staticmethod
    def _create_return_eurostat_area(tx, item_name, area_name, year, source):
        if source == 'apro_ec_lshen':
            result = tx.run("MATCH (c:Category) "
                            "WHERE c.name = $item_name "
                            "MERGE (a:Area {name: $area_name}) "
                            "MERGE (c)-[r:REPORTED_BY]->(a) "
                            "SET r.year_apro_ec_lshen = $year "
                            "RETURN r.year_apro_ec_lshen", item_name = item_name, area_name = area_name, year = year)
            return result.single()[0]
        elif source ==  'apro_mt_lscatl':
            result = tx.run("MATCH (c:Category) "
                            "WHERE c.name = $item_name "
                            "MERGE (a:Area {name: $area_name}) "
                            "MERGE (c)-[r:REPORTED_BY]->(a) "
                            "SET r.year_apro_mt_lscatl = $year "
                            "RETURN r.year_apro_mt_lscatl", item_name = item_name, area_name = area_name, year = year)
            return result.single()[0]
        elif source == 'apro_mt_lsequi':
            result = tx.run("MATCH (c:Category) "
                            "WHERE c.name = $item_name "
                            "MERGE (a:Area {name: $area_name}) "
                            "MERGE (c)-[r:REPORTED_BY]->(a) "
                            "SET r.year_apro_mt_lsequi = $year "
                            "RETURN r.year_apro_mt_lsequi", item_name = item_name, area_name = area_name, year = year)
            return result.single()[0]
        elif source ==  'apro_mt_lsgoat':
            result = tx.run("MATCH (c:Category) "
                            "WHERE c.name = $item_name "
                            "MERGE (a:Area {name: $area_name}) "
                            "MERGE (c)-[r:REPORTED_BY]->(a) "
                            "SET r.year_apro_mt_lsgoat = $year "
                            "RETURN r.year_apro_mt_lsgoat", item_name = item_name, area_name = area_name, year = year)
            return result.single()[0]
        elif source == 'apro_mt_lspig':
            result = tx.run("MATCH (c:Category) "
                            "WHERE c.name = $item_name "
                            "MERGE (a:Area {name: $area_name}) "
                            "MERGE (c)-[r:REPORTED_BY]->(a) "
                            "SET r.year_apro_mt_lspig = $year "
                            "RETURN r.year_apro_mt_lspig", item_name = item_name, area_name = area_name, year = year)
            return result.single()[0]
        elif source == 'apro_mt_lssheep':
            result = tx.run("MATCH (c:Category) "
                            "WHERE c.name = $item_name "
                            "MERGE (a:Area {name: $area_name}) "
                            "MERGE (c)-[r:REPORTED_BY]->(a) "
                            "SET r.year_apro_mt_lssheep = $year "
                            "RETURN r.year_apro_mt_lssheep", item_name = item_name, area_name = area_name, year = year)
            return result.single()[0]
        elif source == 'apro_ec_poula':
            result = tx.run("MATCH (c:Category) "
                            "WHERE c.name = $item_name "
                            "MERGE (a:Area {name: $area_name}) "
                            "MERGE (c)-[r:REPORTED_BY]-(a) "
                            "SET r.year_apro_ec_poula = $year "
                            "RETURN r.year_apro_ec_poula", item_name = item_name, area_name = area_name, year = year)
            return result.single()[0]
    
    @staticmethod
    def _create_return_eth_area(tx, item_name, area_name, year, source):
        result = tx.run("MATCH (c:Category) "
                        "WHERE c.name = $item_name "
                        "MERGE (a:Area {name: $area_name}) "
                        "MERGE (c)-[r:REPORTED_BY]-(a) "
                        "SET r.year_ethCSA = $year "
                        "RETURN c.name", item_name = item_name, area_name = area_name, year = year)

        return result.single()[0]

    @staticmethod
    def _create_return_woah_area(tx, item_name, area_name, year, source):
        result = tx.run("MATCH (c:Category) "
                        "WHERE c.name = $item_name "
                        "MERGE (a:Area {name: $area_name}) "
                        "MERGE (c)-[r:REPORTED_BY]->(a) "
                        "SET r.year_WOAHpopulation = $year "
                        "RETURN c.name", item_name = item_name, area_name = area_name, year = year)
        return result.single()[0]

    @staticmethod
    def _create_return_fao_area(tx, item_name, area_name, year, source):
        if source == 'UNFCCC': 
            result = tx.run("MATCH (c:Category) "
                            "WHERE c.name = $item_name "
                            "MERGE (a:Area {name: $area_name}) "
                            "MERGE (c)-[r:REPORTED_BY]->(a) "
                            "SET r.year_UNFCCC = $year "
                            "RETURN r.year_UNFCCC", item_name = item_name, area_name = area_name, year = year) 
        if source == 'FAOTIER1':
            result = tx.run("MATCH (c:Category) "
                            "WHERE c.name = $item_name "
                            "MERGE (a:Area {name: $area_name}) "
                            "MERGE (c)-[r:REPORTED_BY]->(a) "
                            "SET r.year_FAOTIER1 = $year "
                            "RETURN r.year_FAOTIER1", item_name = item_name, area_name = area_name, year = year, source = source)
        if source == 'Laying':
            result = tx.run("MATCH (c:Category) "
                            "WHERE c.name = $item_name "
                            "MERGE (a:Area {name: $area_name}) "
                            "MERGE (c)-[r:REPORTED_BY]->(a) "
                            "SET r.year_Laying = $year "
                            "RETURN r.year_Laying", item_name = item_name, area_name = area_name, year = year)
        elif source == 'MilkAnimals': 
            result = tx.run("MATCH (c:Category) "
                            "WHERE c.name = $item_name "
                            "MERGE (a:Area {name: $area_name}) "
                            "MERGE (c)-[r:REPORTED_BY]->(a) "
                            "SET r.year_MilkAnimals = $year "
                            "RETURN r.year_MilkAnimals", item_name = item_name, area_name = area_name, year = year, source = source)
        elif source == 'ProducingAnimalsSlaughtered':
            result = tx.run("MATCH (c:Category) "
                            "WHERE c.name = $item_name "
                            "MERGE (a:Area {name: $area_name}) "
                            "MERGE (c)-[r:REPORTED_BY]->(a) "
                            "SET r.year_ProducingAnimalsSlaughtered = $year "
                            "RETURN r.year_ProducingAnimalsSlaughtered", item_name = item_name, area_name = area_name, year = year, source = source)
        elif source == 'Stocks':
            result = tx.run("MATCH (c:Category) "
                            "WHERE c.name = $item_name "
                            "MERGE (a:Area {name: $area_name}) "
                            "MERGE (c)-[r:REPORTED_BY]->(a) "
                            "SET r.year_Stocks = $year "
                            "RETURN r.year_Stocks", item_name = item_name, area_name = area_name, year = year, source = source)
  
        return result.single()[0]

                        