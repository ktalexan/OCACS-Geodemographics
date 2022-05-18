# OCACS-Geodemographics
Orange County American Community Survey (ACS) Geodemographics
## OC Survey American Community Survey (ACS) GeoDemographics Repository

Dr. Kostas Alexandridis, GISP. OC Public Works, OC Survey/Geospatial Services, 2019.

### Description

---
This repository contains basic code for processing, customizing and displaying geodatabases containing the spatially-explicit data of the US Census American Community Survey (ACS), 5-year estimates for the Orange County, California.

### Census Data

---
The original data are downloaded from the US Census TIGER/Line dataset with linked ACS demographic tables.

**Data source**: [US Census TIGER/Line with Selected Demographic and Economic Data.](https://www.census.gov/geographies/mapping-files/time-series/geo/tiger-data.html)

### Geographies included

---
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

<br/><br/>

### Geodemographic Tables by group

For each of the 14 geographies described in the previous section four categories of geodemographic characteristics are linked:
>**[1. Demographic characteristics (6 groups, 105 fields)](Documentation/ACSDemographic.md)**
**[2. Social characteristics (19 groups, 500 fields)](Documentation/ACSSocial.md)**
**[3. Economic characteristics (19 groups, 397 fields)](Documentation/ACSEconomic.md)**
**[4. Housing characteristics (23 groups, 406 fields)](Documentation/ACSHousing.md)**

Each of the geographies is represented by a separate geodatabase structure. Within of each of the geographic level geodatabases, each of the four characteristics is represented by a _feature class_ respectively. In order to easily identify each of the sub-groups within each category, the name of the original census table field was adjusted by prepending to it the subgroup identification code. For example, the original field B01001e1 would become D01_B01001e1 in the new feature class for the demographic characteristics.

A more detailed description of each sub-group within each of the four feature classes representing the ACS table characteristics is provided in each of the sections above (opens the documentation markdown file). The table's columns represent: the subgroup's code; its descriptive name;the universe (summative) level of the reference; the ACS cenus table in which the original fields are located; the fields/variables of the data, and; how many fields are included in the subgroup.

<br><br>

### Geodatabase Feature Class Metadata Description

<br>

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

<br>

<h4 id="CO">Orange County</h4>

<h5>COD: County Demographic Characteristics</h5>

Name|Orange County ACS 2017 (5-year estimates): County Level Demographic Characteristics (ACS2017COD)
:---|:---
Tags|geodemographics; Orange County; California; US Census; ACS; American Community Survey; demographics; age and sex; median age; race; Hispanic or Latino; voting age
Summary|Key demographic characteristics of the 2017 American Community Survey (ACS), 5-year estimates for Orange County, California. The purpose of the dataset is to assist spatial visualization and analysis of basic demographic statistical information in the county. Universe: Total population.
Description | US Census American Community Survey (ACS) 2017, 5-year estimates of the key demographic characteristics for Orange County, California. The layer contains demographic data for tables X01, X02, X03 and X05 of the ACS 2017 (5-year) dataset for Orange County. The US Census geodemographic data are based on the 2017 TigerLines across multiple census geographies. The spatial geographies were merged with ACS demographic data tables. The selected fields contain six table groups: D01 - Sex and age (universe: total population, 49 fields, table X01); D02 - Median age by sex and race (universe: total population, 12 fields, table X1); D03 - Race (universe: total population, 8 fields, table X2); D04 - Race alone or in combination with one or more other races (universe: total population, 7 fields, table X2); D05 - Hispanic or Latino and race (universe: total population, 21 fields, X3); D06 - Citizen voting age population (universe: citizen, 18 years and over population, 8 fields, table X5).
Terms of Use | Original datasets from US Census [TigerLine Geography](https://www.census.gov/geo/maps-data/data/tiger-line.html), and [American FactFinder](https://factfinder.census.gov) for the selected tables of the American Community Survey (ACS, 2017). Linking and merging geographic with demographic tables along with final production of the merged spatial geodatabase and online datasets are performed by Orange County Public Works, OC Survey/Geospatial Services, Dr. Kostas Alexandridis, GISP, on December 2019.

<br>
<h5>COS: County Social Characteristics</h5>

Name|Orange County ACS 2017 (5-year estimates): County Level Social Characteristics (ACS2017COD)
:---|:---
Tags|geodemographics; Orange County; California; US Census; ACS; American Community Survey; social characteristics; households;
Summary|Key demographic characteristics of the 2017 American Community Survey (ACS), 5-year estimates for Orange County, California. The purpose of the dataset is to assist spatial visualization and analysis of basic demographic statistical information in the county. Universe: Total population.
Description | US Census American Community Survey (ACS) 2017, 5-year estimates of the key demographic characteristics for Orange County, California. The layer contains demographic data for tables X01, X02, X03 and X05 of the ACS 2017 (5-year) dataset for Orange County. The US Census geodemographic data are based on the 2017 TigerLines across multiple census geographies. The spatial geographies were merged with ACS demographic data tables. The selected fields contain six table groups: D01 - Sex and age (universe: total population, 49 fields, table X01); D02 - Median age by sex and race (universe: total population, 12 fields, table X1); D03 - Race (universe: total population, 8 fields, table X2); D04 - Race alone or in combination with one or more other races (universe: total population, 7 fields, table X2); D05 - Hispanic or Latino and race (universe: total population, 21 fields, X3); D06 - Citizen voting age population (universe: citizen, 18 years and over population, 8 fields, table X5).
Terms of Use | Original datasets from US Census [TigerLine Geography](https://www.census.gov/geo/maps-data/data/tiger-line.html), and [American FactFinder](https://factfinder.census.gov) for the selected tables of the American Community Survey (ACS, 2017). Linking and merging geographic with demographic tables along with final production of the merged spatial geodatabase and online datasets are performed by Orange County Public Works, OC Survey/Geospatial Services, Dr. Kostas Alexandridis, GISP, on December 2019.

<br>
<h5>COE: County Economic Characteristics</h5>

<br>
<h5>COH: County Housing Characteristics</h5>

<br>
<h4 id="CS">County Subdivisions</h4>

<h5>CSD: County Subdivisions Demographic Characteristics</h5>

<br>
<h5>CSS: County Subdivisions Social Characteristics</h5>

<br>
<h5>CSE: County Subdivisions Economic Characteristics</h5>

<br>
<h5>CSH: County Subdivisions Housing Characteristics</h5>

<br>
<h4 id="PL">Cities/Places</h4>

<h5>PLD: Cities/Places Demographic Characteristics</h5>

<br>
<h5>PLS: Cities/Places Social Characteristics</h5>

<br>
<h5>PLE: Cities/Places Economic Characteristics</h5>

<br>
<h5>PLH: Cities/Places Housing Characteristics</h5>

<br>
<h4 id="ZC">ZIP Code Tabulation Areas</h4>

<h5>ZCD: ZIP Code Tabulation Areas Demographic Characteristics</h5>

<br>
<h5>ZCS: ZIP Code Tabulation Areas Social Characteristics</h5>

<br>
<h5>ZCE: ZIP Code Tabulation Areas Economic Characteristics</h5>

<br>
<h5>ZCH: ZIP Code Tabulation Areas Housing Characteristics</h5>

<br>
<h4 id="CD">Congressional Districts</h4>

<h5>CDD: Congressional Districts Demographic Characteristics</h5>

<br>
<h5>CDS: Congressional Districts Social Characteristics</h5>

<br>
<h5>CDE: Congressional Districts Economic Characteristics</h5>

<br>
<h5>CDH: Congressional Districts Housing Characteristics</h5>

<br>
<h4 id="SA">State Assembly Legislative Districts</h4>

<h5>SAD: State Assembly Legislative Districts Demographic Characteristics</h5>

<br>
<h5>SAS: State Assembly Legislative Districts Social Characteristics</h5>

<br>
<h5>SAE: State Assembly Legislative Districts Economic Characteristics</h5>

<br>
<h5>SAH: State Assembly Legislative Districts Housing Characteristics</h5>

<br>
<h4 id="SS">State Senate Legislative Districts</h4>

<h5>SSD: State Senate Legislative Districts Demographic Characteristics</h5>

<br>
<h5>SSS: State Senate Legislative Districts Social Characteristics</h5>

<br>
<h5>SSE: State Senate Legislative Districts Economic Characteristics</h5>

<br>
<h5>SSH: State Senate Legislative Districts Housing Characteristics</h5>

<br>
<h4 id="EE">Elementary School Districts</h4>

<h5>EED: Elementary School Districts Demographic Characteristics</h5>

<br>
<h5>EES: Elementary School Districts Social Characteristics</h5>

<br>
<h5>EEE: Elementary School Districts Economic Characteristics</h5>

<br>
<h5>EEH: Elementary School Districts Housing Characteristics</h5>
