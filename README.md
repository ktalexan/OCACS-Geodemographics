# OCACS-Geodemographics
---

Orange County American Community Survey (ACS) Geodemographics
## OC Survey American Community Survey (ACS) GeoDemographics Repository

Dr. Kostas Alexandridis, GISP. OC Public Works, OC Survey/Geospatial Services, 2019.
<br/>

### Description

This repository contains basic code for processing, customizing and displaying geodatabases containing the spatially-explicit data of the US Census American Community Survey (ACS), 5-year estimates for the Orange County, California.
<br/>

### Census Data

The original data are downloaded from the US Census TIGER/Line dataset with linked ACS demographic tables.
**Data source**: [US Census TIGER/Line with Selected Demographic and Economic Data.](https://www.census.gov/geographies/mapping-files/time-series/geo/tiger-data.html)
<br/>

### Geographies included

The dataset incude 14 separate geographies, and 25 data tables per geography in each geodatabase. Specifically, the included geographies are:

<table>
    <thead>
        <tr>
            <th>Category</th>
            <th>Level</th>
            <th>Abbrev</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td rowspan=4>Administrative</td>
            <td>County</td>
            <td>CO</td>
            <td>County of Orange</td>
        </tr>
        <tr>
            <td>County Subdivisions</td>
            <td>CS</td>
            <td>Orange County subdivisions</td>
        </tr>
        <tr>
            <td>Cities/Places</td>
            <td>PL</td>
            <td>Orange County Cities</td>
        </tr>
        <tr>
            <td>ZIP Codes</td>
            <td>ZC</td>
            <td>ZIP Code Tabulation Areas for Orange County</td>
        </tr>
        <tr>
            <td rowspan = 3>Political</td>
            <td>Congressional Districts</td>
            <td>CD</td>
            <td>Congressional Districts, 113th-116th US Congress for Orange County</td>
        </tr>
        <tr>
            <td>State Assembly</td>
            <td>LL</td>
            <td>State Assembly Legislative Districts (Lower) for Orange County</td>
        </tr>
        <tr>
            <td>State Senate</td>
            <td>UL</td>
            <td>State Senate Legislative Districts (Upper) for Orange County</td>
        </tr>
        <tr>
            <td rowspan = 3>Education</td>
            <td>Elementary</td>
            <td>ED</td>
            <td>Elementary School Districts for Orange County</td>
        </tr>
        <tr>
            <td>Secondary</td>
            <td>SD</td>
            <td>Secondary School Districts for Orange County</td>
        </tr>
        <tr>
            <td>Unified</td>
            <td>UD</td>
            <td>Unified School Districts for Orange County</td>
        </tr>
        <tr>
            <td rowspan = 4>Census</td>
            <td>Urban Areas</td>
            <td>UA</td>
            <td>Urban Areas for Orange and Los Angeles Counties</td>
        </tr>
        <tr>
            <td>Public Use Microdata Areas</td>
            <td>PU</td>
            <td>Census Public Use Microdata Areas (PUMA) for Orange County</td>
        </tr>
        <tr>
            <td>Block Groups</td>
            <td>BG</td>
            <td>Census Block Groups for Orange County</td>
        </tr>
        <tr>
            <td>Census Tracts</td>
            <td>TR
</td>
            <td>Census Tracts for Orange County</td>
        </tr>
    </tbody>
</table>

<br/>

### Geodemographic Tables by group

For each of the 14 geographies described in the previous section four categories of geodemographic characteristics are linked:
**1. [Demographic characteristics (6 groups, 105 fields)](Documentation/ACSDemographic.md)**
**2. [Social characteristics (19 groups, 500 fields)](Documentation/ACSSocial.md)**
**3. [Economic characteristics (19 groups, 397 fields)](Documentation/ACSEconomic.md)**
**4. [Housing characteristics (23 groups, 406 fields)](Documentation/ACSHousing.md)**

Each of the geographies is represented by a separate geodatabase structure. Within of each of the geographic level geodatabases, each of the four characteristics is represented by a _feature class_ respectively. In order to easily identify each of the sub-groups within each category, the name of the original census table field was adjusted by prepending to it the subgroup identification code. For example, the original field B01001e1 would become D01_B01001e1 in the new feature class for the demographic characteristics.

A more detailed description of each sub-group within each of the four feature classes representing the ACS table characteristics is provided in each of the sections above (opens the documentation markdown file). The table's columns represent: the subgroup's code; its descriptive name;the universe (summative) level of the reference; the ACS cenus table in which the original fields are located; the fields/variables of the data, and; how many fields are included in the subgroup.
<br/>

### Geodatabase Feature Class Metadata Description

Tabulation of level abbreviations by geography and ACS category characteristics. The 3-letter abbreviation consists of:

* First and Second letter: Geography level (14-levels)
* Third letter: ACS category characteristics (4-levels)

Total abbreviations: 14 georaphies x 4 characteristics = 56 feature class levels (four in each geodatabase).

Geography|Demographic (D)|Social (S)|Economic (E)|Housing (H)
---|:---:|:---:|:---:|:---:
County (CO)|COD|COS|COE|COH
County Subdivision (CS)|CSD|CSS|CSE|CSH
Cities/Places (PL)|PLD|PLS|PLE|PLH
ZIP Code Tabulation Areas (ZC)|ZCD|ZCS|ZCE|ZCH
Congressional Districts (CD)|CDD|CDS|CDE|CDH
State Assembly Legislative Districts (LL)|LLD|LLS|LLE|LLH
State Senate Legislative Districts (UL)|ULD|ULS|ULE|ULH
Elementary School Districts (ED)|EDD|EDS|EDE|EDH
Secondary School Districts (SD)|SDD|SDS|SDE|SDH
Unified School Districts (UD)|UDD|UDS|UDE|UDH
Urban Areas (UA)|UAD|UAS|UAE|UAH
Public Use Microdata Areas (PU)|PUD|PUS|PUE|PUH
Block Groups (BG)|BGD|BGS|BGE|BGH
Census Tracts (TR)|TRD|TRS|TRE|TRH

<br/>

For complete geodatabase metadata information and description, please [follow this link to the full metadata document](Documentation/GeodatabaseMedatada.md)
