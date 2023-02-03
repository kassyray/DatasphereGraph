CREATE CONSTRAINT datasource ON (datasource:Datasource) ASSERT datasource.name IS UNIQUE;
CREATE CONSTRAINT category ON (category:Category) ASSERT category.name IS UNIQUE;
CREATE CONSTRAINT area ON (area:Area) ASSERT area.name IS UNIQUE
CREATE CONSTRAINT table ON (table:table) ASSERT table.name IS UNIQUE