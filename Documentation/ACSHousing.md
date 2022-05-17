# OCACS Geodemographics Documentation

Orange County American Community Survey (ACS) Geodemographic Repository
Dr. Kostas Alexandridis, GISP. OC Public Works, OC Survey/Geospatial Services, 2019 - 2022.

## Geodemographic Tables by group

For each of the 14 geographies described in the previous section four categories of geodemographic characteristics are linked:

>**[1. Demographic characteristics (6 groups, 105 fields)](Documentation/../ACSDemographic.md)**
**[2. Social characteristics (19 groups, 500 fields)](Documentation/../ACSSocial.md)**
**[3. Economic characteristics (19 groups, 397 fields)](Documentation/ACSEconomic.md)**
**4. Housing characteristics (23 groups, 406 fields)** _(this document)_

Each of the geographies is represented by a separate geodatabase structure. Within of each of the geographic level geodatabases, each of the four characteristics is represented by a _feature class_ respectively. In order to easily identify each of the sub-groups within each category, the name of the original census table field was adjusted by prepending to it the subgroup identification code. For example, the original field B01001e1 would become D01_B01001e1 in the new feature class for the demographic characteristics.

A more detailed description of each sub-group within each of the four feature classes representing the ACS table characteristics is provided below. The table's columns represent: the subgroup's code; its descriptive name;the universe (summative) level of the reference; the ACS cenus table in which the original fields are located; the fields/variables of the data, and; how many fields are included in the subgroup.

<br><br>
