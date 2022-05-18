<img align="left" src="Documentation/OCACS.jpg" width="300" hspace=25 vspace=15>

<h1>OC Survey American Community Survey (ACS)<br>GeoDemographics Repository</h1>
Dr. Kostas Alexandridis, GISP <br> OC Public Works, OC Survey Geospatial Services, 2019-2022.
<br/><br/>

<h2>Description</h2>

This repository contains basic code for processing, customizing and displaying geodatabases containing the spatially-explicit data of the US Census American Community Survey (ACS), 5-year estimates for the Orange County, California.
<br/>

<h2>Census Data</h2>

The original data are downloaded from the US Census TIGER/Line dataset with linked ACS demographic tables.
<b>Data source</b>: <a href="https://www.census.gov/geographies/mapping-files/time-series/geo/tiger-data.html" target="_blank">US Census TIGER/Line with Selected Demographic and Economic Data.</a>
<br/>

<h2>Geographies included</h2>

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

<h2>Geodemographic Tables by group</h2>

For each of the 14 geographies described in the previous section four categories of geodemographic characteristics are linked:

<ol>
    <li><a href="Documentation/ACSDemographic.md"><b>Demographic Characteristics</b> (6 groups, 105 fields)</a></li>
    <li><a href="Documentation/ACSSocial.md"><b>Social Characteristics</b> (19 groups, 500 fields)</a></li>
    <li><a href="Documentation/ACSEconomic.md"><b>Economic Characteristics</b> (19 groups, 397 fields)</a></li>
    <li><a href="Documentation/ACSHousing.md"><b>Housing Characteristics</b> (19 groups, 406 fields)</a></li>
</ol>

Each of the geographies is represented by a separate geodatabase structure. Within of each of the geographic level geodatabases, each of the four characteristics is represented by a _feature class_ respectively. In order to easily identify each of the sub-groups within each category, the name of the original census table field was adjusted by prepending to it the subgroup identification code. For example, the original field B01001e1 would become D01_B01001e1 in the new feature class for the demographic characteristics.

A more detailed description of each sub-group within each of the four feature classes representing the ACS table characteristics is provided in each of the sections above (opens the documentation markdown file). The table's columns represent: the subgroup's code; its descriptive name;the universe (summative) level of the reference; the ACS cenus table in which the original fields are located; the fields/variables of the data, and; how many fields are included in the subgroup.
<br/>

<h2>Geodatabase Feature Class Metadata Description</h2>

Tabulation of level abbreviations by geography and ACS category characteristics. The 3-letter abbreviation consists of:
<ul>
    <li>First and Second letter: Geography level (14-levels)</li>
    <li>Third letter: ACS category characteristics (4-levels)</li>
</ul>


<table>
    <caption>Total abbreviations: 14 georaphies x 4 characteristics = 56 feature class levels (four in each geodatabase).</caption>
    <thead>
        <tr>
            <th>Geography</th>
            <th>Demographic (D)</th>
            <th>Social (S)</th>
            <th>Economic (E)</th>
            <th>Housing (H)</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="text-align:left">1. County (CO)</td>
            <td style="text-align:center">COD</td>
            <td style="text-align:center">COS</td>
            <td style="text-align:center">COE</td>
            <td style="text-align:center">COH</td>
        </tr>
        <tr>
            <td style="text-align:left">2. County Subdivision (CS)</td>
            <td style="text-align:center">CSD</td>
            <td style="text-align:center">CSS</td>
            <td style="text-align:center">CSE</td>
            <td style="text-align:center">CSH</td>
        </tr>
        <tr>
            <td style="text-align:left">3. Cities/Places (PL)</td>
            <td style="text-align:center">PLD</td>
            <td style="text-align:center">PLS</td>
            <td style="text-align:center">PLE</td>
            <td style="text-align:center">PLH</td>
        </tr>
        <tr>
            <td style="text-align:left">4. ZIP Code Tabulation Areas (ZC)</td>
            <td style="text-align:center">ZCD</td>
            <td style="text-align:center">ZCS</td>
            <td style="text-align:center">ZCE</td>
            <td style="text-align:center">ZCH</td>
        </tr>
        <tr>
            <td style="text-align:left">5. Congressional Districts (CD)</td>
            <td style="text-align:center">CDD</td>
            <td style="text-align:center">CDS</td>
            <td style="text-align:center">CDE</td>
            <td style="text-align:center">CDH</td>
        </tr>
        <tr>
            <td style="text-align:left">6. State Assembly Legislative Districts (LL)</td>
            <td style="text-align:center">LLD</td>
            <td style="text-align:center">LLS</td>
            <td style="text-align:center">LLE</td>
            <td style="text-align:center">LLH</td>
        </tr>
        <tr>
            <td style="text-align:left">7. State Senate Legislative Districts (UL)</td>
            <td style="text-align:center">ULD</td>
            <td style="text-align:center">ULS</td>
            <td style="text-align:center">ULE</td>
            <td style="text-align:center">ULH</td>
        </tr>
        <tr>
            <td style="text-align:left">8. Elementary School Districts (ED)</td>
            <td style="text-align:center">EDD</td>
            <td style="text-align:center">EDS</td>
            <td style="text-align:center">EDE</td>
            <td style="text-align:center">EDH</td>
        </tr>
        <tr>
            <td style="text-align:left">9. Secondary School Districts (SD)</td>
            <td style="text-align:center">SDD</td>
            <td style="text-align:center">SDS</td>
            <td style="text-align:center">SDE</td>
            <td style="text-align:center">SDH</td>
        </tr>
        <tr>
            <td style="text-align:left">10. Unified School Districts (UD)</td>
            <td style="text-align:center">UDD</td>
            <td style="text-align:center">UDS</td>
            <td style="text-align:center">UDE</td>
            <td style="text-align:center">UDH</td>
        </tr>
        <tr>
            <td style="text-align:left">11. Urban Areas (UA)</td>
            <td style="text-align:center">UAD</td>
            <td style="text-align:center">UAS</td>
            <td style="text-align:center">UAE</td>
            <td style="text-align:center">UAH</td>
        </tr>
        <tr>
            <td style="text-align:left">12. Public Use Microdata Areas (PU)</td>
            <td style="text-align:center">PUD</td>
            <td style="text-align:center">PUS</td>
            <td style="text-align:center">PUE</td>
            <td style="text-align:center">PUH</td>
        </tr>
        <tr>
            <td style="text-align:left">13. Block Groups (BG)</td>
            <td style="text-align:center">BGD</td>
            <td style="text-align:center">BGS</td>
            <td style="text-align:center">BGE</td>
            <td style="text-align:center">BGH</td>
        </tr>
        <tr>
            <td style="text-align:left">14. Census Tracts (TR)</td>
            <td style="text-align:center">TRD</td>
            <td style="text-align:center">TRS</td>
            <td style="text-align:center">TRE</td>
            <td style="text-align:center">TRH</td>
        </tr>
    </tbody>
</table>
<br/>

For complete geodatabase metadata information and description, please <a href="Documentation/GeodatabaseMetadata.md" target="_blank">follow this link to the full metadata document.</a>

<br/>