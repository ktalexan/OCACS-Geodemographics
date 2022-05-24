# OC Survey American Community Survey (ACS)<br>Geodemographics Repository

*Dr. Kostas Alexandridis, GISP <br> OC Public Works, OC Survey Geospatial Services, 2019-2022.*


## Geodatabase Feature Class Metadata Descriptions

Tabulation of level abbreviations by geography and ACS category characteristics. The 3-letter abbreviation consists of:

* First and second letter: *Geography level* (14-levels)
* Third letter: *ACS category characteristics* (4-levels)

*Total abbreviations: 14 georaphies x 4 characteristics = 56 feature class levels (four in each geodatabase).*

| Geography Demographic (D) | Social (S) | Economic (E) | Housing (H) |
| :--- | :---: | :---: | :---: | :---: |
| 1. County (CO) | COD | COS | COE | COH |
| 2. County Subdivision (CS) | CSD | CSS | CSE | CSH |
| 3. Cities/Places (PL) | PLD | PLS | PLE | PLH |
| 4. ZIP Code Tabulation Areas (ZC) | ZCD | ZCS | ZCE | ZCH |
| 5. Congressional Districts (CD) | CDD | CDS | CDE | CDH |
| 6. State Assembly Legislative Districts (LL) | LLD | LLS | LLE | LLH |
| 7. State Senate Legislative Districts (UL) | ULD | ULS | ULE | ULH |
| 8. Elementary School Districts (ED) | EDD | EDS | EDE | EDH |
| 9. Secondary School Districts (SD) | SDD | SDS | SDE | SDH |
| 10. Unified School Districts (UD) | UDD | UDS | UDE | UDH |
| 11. Urban Areas (UA) | UAD | UAS | UAE | UAH |
| 12. Public Use Microdata Areas (PU) | PUD | PUS | PUE | PUH |
| 13. Block Groups (BG) | BGD | BGS | BGE | BGH |
| 14. Census Tracts (TR) | TRD | TRS | TRE | TRH |


The specific and detailed metadata documentation for these geographies and characteristics are listed below.

## Contents: 
- [OC Survey American Community Survey (ACS)<br>Geodemographics Repository](#oc-survey-american-community-survey-acsgeodemographics-repository)
  - [Geodatabase Feature Class Metadata Descriptions](#geodatabase-feature-class-metadata-descriptions)
  - [Contents:](#contents)
  - [Year: 2013](#year-2013)
    - [2013.1. Demographic Characteristics](#20131-demographic-characteristics)
      - [2013.1.1. County Level Demographic Characteristics](#201311-county-level-demographic-characteristics)
      - [2013.1.2. County Subdivision Demographic Characteristics](#201312-county-subdivision-demographic-characteristics)
      - [2013.1.3. Cities/Places Demographic Characteristics](#201313-citiesplaces-demographic-characteristics)
      - [2013.1.4. ZIP Code Tabulation Areas Demographic Characteristics](#201314-zip-code-tabulation-areas-demographic-characteristics)
      - [2013.1.5. Congressional Districts Demographic Characteristics](#201315-congressional-districts-demographic-characteristics)
      - [2013.1.6. State Assembly Legislative Districts Demographic Characteristics](#201316-state-assembly-legislative-districts-demographic-characteristics)
      - [2013.1.7. State Senate Legislative Districts Demographic Characteristics](#201317-state-senate-legislative-districts-demographic-characteristics)
      - [2013.1.8. Elementary School Districts Demographic Characteristics](#201318-elementary-school-districts-demographic-characteristics)
      - [2013.1.9. Secondary School Districts Demographic Characteristics](#201319-secondary-school-districts-demographic-characteristics)
      - [2013.1.10. Unified School Districts Demographic Characteristics](#2013110-unified-school-districts-demographic-characteristics)
      - [2013.1.11. Urban Areas Demographic Characteristics](#2013111-urban-areas-demographic-characteristics)
      - [2013.1.12. Public Use Microdata Areas Demographic Characteristics](#2013112-public-use-microdata-areas-demographic-characteristics)
      - [2013.1.13. Block Groups Demographic Characteristics](#2013113-block-groups-demographic-characteristics)
      - [2013.1.14. Census Tracts Demographic Characteristics](#2013114-census-tracts-demographic-characteristics)
    - [2013.2. Social Characteristics](#20132-social-characteristics)
      - [2013.2.1. County Level Social Characteristics](#201321-county-level-social-characteristics)
      - [2013.2.2. County Subdivision Social Characteristics](#201322-county-subdivision-social-characteristics)
      - [2013.2.3. Cities/Places Social Characteristics](#201323-citiesplaces-social-characteristics)
      - [2013.2.4. ZIP Code Tabulation Areas Social Characteristics](#201324-zip-code-tabulation-areas-social-characteristics)
      - [2013.2.5. Congressional Districts Social Characteristics](#201325-congressional-districts-social-characteristics)
      - [2013.2.6. State Assembly Legislative Districts Social Characteristics](#201326-state-assembly-legislative-districts-social-characteristics)
      - [2013.2.7. State Senate Legislative Districts Social Characteristics](#201327-state-senate-legislative-districts-social-characteristics)
      - [2013.2.8. Elementary School Districts Social Characteristics](#201328-elementary-school-districts-social-characteristics)
      - [2013.2.9. Secondary School Districts Social Characteristics](#201329-secondary-school-districts-social-characteristics)
      - [2013.2.10. Unified School Districts Social Characteristics](#2013210-unified-school-districts-social-characteristics)
      - [2013.2.11. Urban Areas Social Characteristics](#2013211-urban-areas-social-characteristics)
      - [2013.2.12. Public Use Microdata Areas Social Characteristics](#2013212-public-use-microdata-areas-social-characteristics)
      - [2013.2.13. Block Groups Social Characteristics](#2013213-block-groups-social-characteristics)
      - [2013.2.14. Census Tracts Social Characteristics](#2013214-census-tracts-social-characteristics)
    - [2013.3. Economic Characteristics](#20133-economic-characteristics)
      - [2013.3.1. County Level Economic Characteristics](#201331-county-level-economic-characteristics)
      - [2013.3.2. County Subdivision Economic Characteristics](#201332-county-subdivision-economic-characteristics)
      - [2013.3.3. Cities/Places Economic Characteristics](#201333-citiesplaces-economic-characteristics)
      - [2013.3.4. ZIP Code Tabulation Areas Economic Characteristics](#201334-zip-code-tabulation-areas-economic-characteristics)
      - [2013.3.5. Congressional Districts Economic Characteristics](#201335-congressional-districts-economic-characteristics)
      - [2013.3.6. State Assembly Legislative Districts Economic Characteristics](#201336-state-assembly-legislative-districts-economic-characteristics)
      - [2013.3.7. State Senate Legislative Districts Economic Characteristics](#201337-state-senate-legislative-districts-economic-characteristics)
      - [2013.3.8. Elementary School Districts Economic Characteristics](#201338-elementary-school-districts-economic-characteristics)
      - [2013.3.9. Secondary School Districts Economic Characteristics](#201339-secondary-school-districts-economic-characteristics)
      - [2013.3.10. Unified School Districts Economic Characteristics](#2013310-unified-school-districts-economic-characteristics)
      - [2013.3.11. Urban Areas Economic Characteristics](#2013311-urban-areas-economic-characteristics)
      - [2013.3.12. Public Use Microdata Areas Economic Characteristics](#2013312-public-use-microdata-areas-economic-characteristics)
      - [2013.3.13. Block Groups Economic Characteristics](#2013313-block-groups-economic-characteristics)
      - [2013.3.14. Census Tracts Economic Characteristics](#2013314-census-tracts-economic-characteristics)
    - [2013.4. Housing Characteristics](#20134-housing-characteristics)
      - [2013.4.1. County Level Housing Characteristics](#201341-county-level-housing-characteristics)
      - [2013.4.2. County Subdivision Housing Characteristics](#201342-county-subdivision-housing-characteristics)
      - [2013.4.3. Cities/Places Housing Characteristics](#201343-citiesplaces-housing-characteristics)
      - [2013.4.4. ZIP Code Tabulation Areas Housing Characteristics](#201344-zip-code-tabulation-areas-housing-characteristics)
      - [2013.4.5. Congressional Districts Housing Characteristics](#201345-congressional-districts-housing-characteristics)
      - [2013.4.6. State Assembly Legislative Districts Housing Characteristics](#201346-state-assembly-legislative-districts-housing-characteristics)
      - [2013.4.7. State Senate Legislative Districts Housing Characteristics](#201347-state-senate-legislative-districts-housing-characteristics)
      - [2013.4.8. Elementary School Districts Housing Characteristics](#201348-elementary-school-districts-housing-characteristics)
      - [2013.4.9. Secondary School Districts Housing Characteristics](#201349-secondary-school-districts-housing-characteristics)
      - [2013.4.10. Unified School Districts Housing Characteristics](#2013410-unified-school-districts-housing-characteristics)
      - [2013.4.11. Urban Areas Housing Characteristics](#2013411-urban-areas-housing-characteristics)
      - [2013.4.12. Public Use Microdata Areas Housing Characteristics](#2013412-public-use-microdata-areas-housing-characteristics)
      - [2013.4.13. Block Groups Housing Characteristics](#2013413-block-groups-housing-characteristics)
      - [2013.4.14. Census Tracts Housing Characteristics](#2013414-census-tracts-housing-characteristics)
  - [Year: 2014](#year-2014)
    - [2014.1. Demographic Characteristics](#20141-demographic-characteristics)
      - [2014.1.1. County Level Demographic Characteristics](#201411-county-level-demographic-characteristics)
      - [2014.1.2. County Subdivision Demographic Characteristics](#201412-county-subdivision-demographic-characteristics)
      - [2014.1.3. Cities/Places Demographic Characteristics](#201413-citiesplaces-demographic-characteristics)
      - [2014.1.4. ZIP Code Tabulation Areas Demographic Characteristics](#201414-zip-code-tabulation-areas-demographic-characteristics)
      - [2014.1.5. Congressional Districts Demographic Characteristics](#201415-congressional-districts-demographic-characteristics)
      - [2014.1.6. State Assembly Legislative Districts Demographic Characteristics](#201416-state-assembly-legislative-districts-demographic-characteristics)
      - [2014.1.7. State Senate Legislative Districts Demographic Characteristics](#201417-state-senate-legislative-districts-demographic-characteristics)
      - [2014.1.8. Elementary School Districts Demographic Characteristics](#201418-elementary-school-districts-demographic-characteristics)
      - [2014.1.9. Secondary School Districts Demographic Characteristics](#201419-secondary-school-districts-demographic-characteristics)
      - [2014.1.10. Unified School Districts Demographic Characteristics](#2014110-unified-school-districts-demographic-characteristics)
      - [2014.1.11. Urban Areas Demographic Characteristics](#2014111-urban-areas-demographic-characteristics)
      - [2014.1.12. Public Use Microdata Areas Demographic Characteristics](#2014112-public-use-microdata-areas-demographic-characteristics)
      - [2014.1.13. Block Groups Demographic Characteristics](#2014113-block-groups-demographic-characteristics)
      - [2014.1.14. Census Tracts Demographic Characteristics](#2014114-census-tracts-demographic-characteristics)
    - [2014.2. Social Characteristics](#20142-social-characteristics)
      - [2014.2.1. County Level Social Characteristics](#201421-county-level-social-characteristics)
      - [2014.2.2. County Subdivision Social Characteristics](#201422-county-subdivision-social-characteristics)
      - [2014.2.3. Cities/Places Social Characteristics](#201423-citiesplaces-social-characteristics)
      - [2014.2.4. ZIP Code Tabulation Areas Social Characteristics](#201424-zip-code-tabulation-areas-social-characteristics)
      - [2014.2.5. Congressional Districts Social Characteristics](#201425-congressional-districts-social-characteristics)
      - [2014.2.6. State Assembly Legislative Districts Social Characteristics](#201426-state-assembly-legislative-districts-social-characteristics)
      - [2014.2.7. State Senate Legislative Districts Social Characteristics](#201427-state-senate-legislative-districts-social-characteristics)
      - [2014.2.8. Elementary School Districts Social Characteristics](#201428-elementary-school-districts-social-characteristics)
      - [2014.2.9. Secondary School Districts Social Characteristics](#201429-secondary-school-districts-social-characteristics)
      - [2014.2.10. Unified School Districts Social Characteristics](#2014210-unified-school-districts-social-characteristics)
      - [2014.2.11. Urban Areas Social Characteristics](#2014211-urban-areas-social-characteristics)
      - [2014.2.12. Public Use Microdata Areas Social Characteristics](#2014212-public-use-microdata-areas-social-characteristics)
      - [2014.2.13. Block Groups Social Characteristics](#2014213-block-groups-social-characteristics)
      - [2014.2.14. Census Tracts Social Characteristics](#2014214-census-tracts-social-characteristics)
    - [2014.3. Economic Characteristics](#20143-economic-characteristics)
      - [2014.3.1. County Level Economic Characteristics](#201431-county-level-economic-characteristics)
      - [2014.3.2. County Subdivision Economic Characteristics](#201432-county-subdivision-economic-characteristics)
      - [2014.3.3. Cities/Places Economic Characteristics](#201433-citiesplaces-economic-characteristics)
      - [2014.3.4. ZIP Code Tabulation Areas Economic Characteristics](#201434-zip-code-tabulation-areas-economic-characteristics)
      - [2014.3.5. Congressional Districts Economic Characteristics](#201435-congressional-districts-economic-characteristics)
      - [2014.3.6. State Assembly Legislative Districts Economic Characteristics](#201436-state-assembly-legislative-districts-economic-characteristics)
      - [2014.3.7. State Senate Legislative Districts Economic Characteristics](#201437-state-senate-legislative-districts-economic-characteristics)
      - [2014.3.8. Elementary School Districts Economic Characteristics](#201438-elementary-school-districts-economic-characteristics)
      - [2014.3.9. Secondary School Districts Economic Characteristics](#201439-secondary-school-districts-economic-characteristics)
      - [2014.3.10. Unified School Districts Economic Characteristics](#2014310-unified-school-districts-economic-characteristics)
      - [2014.3.11. Urban Areas Economic Characteristics](#2014311-urban-areas-economic-characteristics)
      - [2014.3.12. Public Use Microdata Areas Economic Characteristics](#2014312-public-use-microdata-areas-economic-characteristics)
      - [2014.3.13. Block Groups Economic Characteristics](#2014313-block-groups-economic-characteristics)
      - [2014.3.14. Census Tracts Economic Characteristics](#2014314-census-tracts-economic-characteristics)
    - [2014.4. Housing Characteristics](#20144-housing-characteristics)
      - [2014.4.1. County Level Housing Characteristics](#201441-county-level-housing-characteristics)
      - [2014.4.2. County Subdivision Housing Characteristics](#201442-county-subdivision-housing-characteristics)
      - [2014.4.3. Cities/Places Housing Characteristics](#201443-citiesplaces-housing-characteristics)
      - [2014.4.4. ZIP Code Tabulation Areas Housing Characteristics](#201444-zip-code-tabulation-areas-housing-characteristics)
      - [2014.4.5. Congressional Districts Housing Characteristics](#201445-congressional-districts-housing-characteristics)
      - [2014.4.6. State Assembly Legislative Districts Housing Characteristics](#201446-state-assembly-legislative-districts-housing-characteristics)
      - [2014.4.7. State Senate Legislative Districts Housing Characteristics](#201447-state-senate-legislative-districts-housing-characteristics)
      - [2014.4.8. Elementary School Districts Housing Characteristics](#201448-elementary-school-districts-housing-characteristics)
      - [2014.4.9. Secondary School Districts Housing Characteristics](#201449-secondary-school-districts-housing-characteristics)
      - [2014.4.10. Unified School Districts Housing Characteristics](#2014410-unified-school-districts-housing-characteristics)
      - [2014.4.11. Urban Areas Housing Characteristics](#2014411-urban-areas-housing-characteristics)
      - [2014.4.12. Public Use Microdata Areas Housing Characteristics](#2014412-public-use-microdata-areas-housing-characteristics)
      - [2014.4.13. Block Groups Housing Characteristics](#2014413-block-groups-housing-characteristics)
      - [2014.4.14. Census Tracts Housing Characteristics](#2014414-census-tracts-housing-characteristics)
  - [Year: 2015](#year-2015)
    - [2015.1. Demographic Characteristics](#20151-demographic-characteristics)
      - [2015.1.1. County Level Demographic Characteristics](#201511-county-level-demographic-characteristics)
      - [2015.1.2. County Subdivision Demographic Characteristics](#201512-county-subdivision-demographic-characteristics)
      - [2015.1.3. Cities/Places Demographic Characteristics](#201513-citiesplaces-demographic-characteristics)
      - [2015.1.4. ZIP Code Tabulation Areas Demographic Characteristics](#201514-zip-code-tabulation-areas-demographic-characteristics)
      - [2015.1.5. Congressional Districts Demographic Characteristics](#201515-congressional-districts-demographic-characteristics)
      - [2015.1.6. State Assembly Legislative Districts Demographic Characteristics](#201516-state-assembly-legislative-districts-demographic-characteristics)
      - [2015.1.7. State Senate Legislative Districts Demographic Characteristics](#201517-state-senate-legislative-districts-demographic-characteristics)
      - [2015.1.8. Elementary School Districts Demographic Characteristics](#201518-elementary-school-districts-demographic-characteristics)
      - [2015.1.9. Secondary School Districts Demographic Characteristics](#201519-secondary-school-districts-demographic-characteristics)
      - [2015.1.10. Unified School Districts Demographic Characteristics](#2015110-unified-school-districts-demographic-characteristics)
      - [2015.1.11. Urban Areas Demographic Characteristics](#2015111-urban-areas-demographic-characteristics)
      - [2015.1.12. Public Use Microdata Areas Demographic Characteristics](#2015112-public-use-microdata-areas-demographic-characteristics)
      - [2015.1.13. Block Groups Demographic Characteristics](#2015113-block-groups-demographic-characteristics)
      - [2015.1.14. Census Tracts Demographic Characteristics](#2015114-census-tracts-demographic-characteristics)
    - [2015.2. Social Characteristics](#20152-social-characteristics)
      - [2015.2.1. County Level Social Characteristics](#201521-county-level-social-characteristics)
      - [2015.2.2. County Subdivision Social Characteristics](#201522-county-subdivision-social-characteristics)
      - [2015.2.3. Cities/Places Social Characteristics](#201523-citiesplaces-social-characteristics)
      - [2015.2.4. ZIP Code Tabulation Areas Social Characteristics](#201524-zip-code-tabulation-areas-social-characteristics)
      - [2015.2.5. Congressional Districts Social Characteristics](#201525-congressional-districts-social-characteristics)
      - [2015.2.6. State Assembly Legislative Districts Social Characteristics](#201526-state-assembly-legislative-districts-social-characteristics)
      - [2015.2.7. State Senate Legislative Districts Social Characteristics](#201527-state-senate-legislative-districts-social-characteristics)
      - [2015.2.8. Elementary School Districts Social Characteristics](#201528-elementary-school-districts-social-characteristics)
      - [2015.2.9. Secondary School Districts Social Characteristics](#201529-secondary-school-districts-social-characteristics)
      - [2015.2.10. Unified School Districts Social Characteristics](#2015210-unified-school-districts-social-characteristics)
      - [2015.2.11. Urban Areas Social Characteristics](#2015211-urban-areas-social-characteristics)
      - [2015.2.12. Public Use Microdata Areas Social Characteristics](#2015212-public-use-microdata-areas-social-characteristics)
      - [2015.2.13. Block Groups Social Characteristics](#2015213-block-groups-social-characteristics)
      - [2015.2.14. Census Tracts Social Characteristics](#2015214-census-tracts-social-characteristics)
    - [2015.3. Economic Characteristics](#20153-economic-characteristics)
      - [2015.3.1. County Level Economic Characteristics](#201531-county-level-economic-characteristics)
      - [2015.3.2. County Subdivision Economic Characteristics](#201532-county-subdivision-economic-characteristics)
      - [2015.3.3. Cities/Places Economic Characteristics](#201533-citiesplaces-economic-characteristics)
      - [2015.3.4. ZIP Code Tabulation Areas Economic Characteristics](#201534-zip-code-tabulation-areas-economic-characteristics)
      - [2015.3.5. Congressional Districts Economic Characteristics](#201535-congressional-districts-economic-characteristics)
      - [2015.3.6. State Assembly Legislative Districts Economic Characteristics](#201536-state-assembly-legislative-districts-economic-characteristics)
      - [2015.3.7. State Senate Legislative Districts Economic Characteristics](#201537-state-senate-legislative-districts-economic-characteristics)
      - [2015.3.8. Elementary School Districts Economic Characteristics](#201538-elementary-school-districts-economic-characteristics)
      - [2015.3.9. Secondary School Districts Economic Characteristics](#201539-secondary-school-districts-economic-characteristics)
      - [2015.3.10. Unified School Districts Economic Characteristics](#2015310-unified-school-districts-economic-characteristics)
      - [2015.3.11. Urban Areas Economic Characteristics](#2015311-urban-areas-economic-characteristics)
      - [2015.3.12. Public Use Microdata Areas Economic Characteristics](#2015312-public-use-microdata-areas-economic-characteristics)
      - [2015.3.13. Block Groups Economic Characteristics](#2015313-block-groups-economic-characteristics)
      - [2015.3.14. Census Tracts Economic Characteristics](#2015314-census-tracts-economic-characteristics)
    - [2015.4. Housing Characteristics](#20154-housing-characteristics)
      - [2015.4.1. County Level Housing Characteristics](#201541-county-level-housing-characteristics)
      - [2015.4.2. County Subdivision Housing Characteristics](#201542-county-subdivision-housing-characteristics)
      - [2015.4.3. Cities/Places Housing Characteristics](#201543-citiesplaces-housing-characteristics)
      - [2015.4.4. ZIP Code Tabulation Areas Housing Characteristics](#201544-zip-code-tabulation-areas-housing-characteristics)
      - [2015.4.5. Congressional Districts Housing Characteristics](#201545-congressional-districts-housing-characteristics)
      - [2015.4.6. State Assembly Legislative Districts Housing Characteristics](#201546-state-assembly-legislative-districts-housing-characteristics)
      - [2015.4.7. State Senate Legislative Districts Housing Characteristics](#201547-state-senate-legislative-districts-housing-characteristics)
      - [2015.4.8. Elementary School Districts Housing Characteristics](#201548-elementary-school-districts-housing-characteristics)
      - [2015.4.9. Secondary School Districts Housing Characteristics](#201549-secondary-school-districts-housing-characteristics)
      - [2015.4.10. Unified School Districts Housing Characteristics](#2015410-unified-school-districts-housing-characteristics)
      - [2015.4.11. Urban Areas Housing Characteristics](#2015411-urban-areas-housing-characteristics)
      - [2015.4.12. Public Use Microdata Areas Housing Characteristics](#2015412-public-use-microdata-areas-housing-characteristics)
      - [2015.4.13. Block Groups Housing Characteristics](#2015413-block-groups-housing-characteristics)
      - [2015.4.14. Census Tracts Housing Characteristics](#2015414-census-tracts-housing-characteristics)
  - [Year: 2016](#year-2016)
    - [2016.1. Demographic Characteristics](#20161-demographic-characteristics)
      - [2016.1.1. County Level Demographic Characteristics](#201611-county-level-demographic-characteristics)
      - [2016.1.2. County Subdivision Demographic Characteristics](#201612-county-subdivision-demographic-characteristics)
      - [2016.1.3. Cities/Places Demographic Characteristics](#201613-citiesplaces-demographic-characteristics)
      - [2016.1.4. ZIP Code Tabulation Areas Demographic Characteristics](#201614-zip-code-tabulation-areas-demographic-characteristics)
      - [2016.1.5. Congressional Districts Demographic Characteristics](#201615-congressional-districts-demographic-characteristics)
      - [2016.1.6. State Assembly Legislative Districts Demographic Characteristics](#201616-state-assembly-legislative-districts-demographic-characteristics)
      - [2016.1.7. State Senate Legislative Districts Demographic Characteristics](#201617-state-senate-legislative-districts-demographic-characteristics)
      - [2016.1.8. Elementary School Districts Demographic Characteristics](#201618-elementary-school-districts-demographic-characteristics)
      - [2016.1.9. Secondary School Districts Demographic Characteristics](#201619-secondary-school-districts-demographic-characteristics)
      - [2016.1.10. Unified School Districts Demographic Characteristics](#2016110-unified-school-districts-demographic-characteristics)
      - [2016.1.11. Urban Areas Demographic Characteristics](#2016111-urban-areas-demographic-characteristics)
      - [2016.1.12. Public Use Microdata Areas Demographic Characteristics](#2016112-public-use-microdata-areas-demographic-characteristics)
      - [2016.1.13. Block Groups Demographic Characteristics](#2016113-block-groups-demographic-characteristics)
      - [2016.1.14. Census Tracts Demographic Characteristics](#2016114-census-tracts-demographic-characteristics)
    - [2016.2. Social Characteristics](#20162-social-characteristics)
      - [2016.2.1. County Level Social Characteristics](#201621-county-level-social-characteristics)
      - [2016.2.2. County Subdivision Social Characteristics](#201622-county-subdivision-social-characteristics)
      - [2016.2.3. Cities/Places Social Characteristics](#201623-citiesplaces-social-characteristics)
      - [2016.2.4. ZIP Code Tabulation Areas Social Characteristics](#201624-zip-code-tabulation-areas-social-characteristics)
      - [2016.2.5. Congressional Districts Social Characteristics](#201625-congressional-districts-social-characteristics)
      - [2016.2.6. State Assembly Legislative Districts Social Characteristics](#201626-state-assembly-legislative-districts-social-characteristics)
      - [2016.2.7. State Senate Legislative Districts Social Characteristics](#201627-state-senate-legislative-districts-social-characteristics)
      - [2016.2.8. Elementary School Districts Social Characteristics](#201628-elementary-school-districts-social-characteristics)
      - [2016.2.9. Secondary School Districts Social Characteristics](#201629-secondary-school-districts-social-characteristics)
      - [2016.2.10. Unified School Districts Social Characteristics](#2016210-unified-school-districts-social-characteristics)
      - [2016.2.11. Urban Areas Social Characteristics](#2016211-urban-areas-social-characteristics)
      - [2016.2.12. Public Use Microdata Areas Social Characteristics](#2016212-public-use-microdata-areas-social-characteristics)
      - [2016.2.13. Block Groups Social Characteristics](#2016213-block-groups-social-characteristics)
      - [2016.2.14. Census Tracts Social Characteristics](#2016214-census-tracts-social-characteristics)
    - [2016.3. Economic Characteristics](#20163-economic-characteristics)
      - [2016.3.1. County Level Economic Characteristics](#201631-county-level-economic-characteristics)
      - [2016.3.2. County Subdivision Economic Characteristics](#201632-county-subdivision-economic-characteristics)
      - [2016.3.3. Cities/Places Economic Characteristics](#201633-citiesplaces-economic-characteristics)
      - [2016.3.4. ZIP Code Tabulation Areas Economic Characteristics](#201634-zip-code-tabulation-areas-economic-characteristics)
      - [2016.3.5. Congressional Districts Economic Characteristics](#201635-congressional-districts-economic-characteristics)
      - [2016.3.6. State Assembly Legislative Districts Economic Characteristics](#201636-state-assembly-legislative-districts-economic-characteristics)
      - [2016.3.7. State Senate Legislative Districts Economic Characteristics](#201637-state-senate-legislative-districts-economic-characteristics)
      - [2016.3.8. Elementary School Districts Economic Characteristics](#201638-elementary-school-districts-economic-characteristics)
      - [2016.3.9. Secondary School Districts Economic Characteristics](#201639-secondary-school-districts-economic-characteristics)
      - [2016.3.10. Unified School Districts Economic Characteristics](#2016310-unified-school-districts-economic-characteristics)
      - [2016.3.11. Urban Areas Economic Characteristics](#2016311-urban-areas-economic-characteristics)
      - [2016.3.12. Public Use Microdata Areas Economic Characteristics](#2016312-public-use-microdata-areas-economic-characteristics)
      - [2016.3.13. Block Groups Economic Characteristics](#2016313-block-groups-economic-characteristics)
      - [2016.3.14. Census Tracts Economic Characteristics](#2016314-census-tracts-economic-characteristics)
    - [2016.4. Housing Characteristics](#20164-housing-characteristics)
      - [2016.4.1. County Level Housing Characteristics](#201641-county-level-housing-characteristics)
      - [2016.4.2. County Subdivision Housing Characteristics](#201642-county-subdivision-housing-characteristics)
      - [2016.4.3. Cities/Places Housing Characteristics](#201643-citiesplaces-housing-characteristics)
      - [2016.4.4. ZIP Code Tabulation Areas Housing Characteristics](#201644-zip-code-tabulation-areas-housing-characteristics)
      - [2016.4.5. Congressional Districts Housing Characteristics](#201645-congressional-districts-housing-characteristics)
      - [2016.4.6. State Assembly Legislative Districts Housing Characteristics](#201646-state-assembly-legislative-districts-housing-characteristics)
      - [2016.4.7. State Senate Legislative Districts Housing Characteristics](#201647-state-senate-legislative-districts-housing-characteristics)
      - [2016.4.8. Elementary School Districts Housing Characteristics](#201648-elementary-school-districts-housing-characteristics)
      - [2016.4.9. Secondary School Districts Housing Characteristics](#201649-secondary-school-districts-housing-characteristics)
      - [2016.4.10. Unified School Districts Housing Characteristics](#2016410-unified-school-districts-housing-characteristics)
      - [2016.4.11. Urban Areas Housing Characteristics](#2016411-urban-areas-housing-characteristics)
      - [2016.4.12. Public Use Microdata Areas Housing Characteristics](#2016412-public-use-microdata-areas-housing-characteristics)
      - [2016.4.13. Block Groups Housing Characteristics](#2016413-block-groups-housing-characteristics)
      - [2016.4.14. Census Tracts Housing Characteristics](#2016414-census-tracts-housing-characteristics)
  - [Year: 2017](#year-2017)
    - [2017.1. Demographic Characteristics](#20171-demographic-characteristics)
      - [2017.1.1. County Level Demographic Characteristics](#201711-county-level-demographic-characteristics)
      - [2017.1.2. County Subdivision Demographic Characteristics](#201712-county-subdivision-demographic-characteristics)
      - [2017.1.3. Cities/Places Demographic Characteristics](#201713-citiesplaces-demographic-characteristics)
      - [2017.1.4. ZIP Code Tabulation Areas Demographic Characteristics](#201714-zip-code-tabulation-areas-demographic-characteristics)
      - [2017.1.5. Congressional Districts Demographic Characteristics](#201715-congressional-districts-demographic-characteristics)
      - [2017.1.6. State Assembly Legislative Districts Demographic Characteristics](#201716-state-assembly-legislative-districts-demographic-characteristics)
      - [2017.1.7. State Senate Legislative Districts Demographic Characteristics](#201717-state-senate-legislative-districts-demographic-characteristics)
      - [2017.1.8. Elementary School Districts Demographic Characteristics](#201718-elementary-school-districts-demographic-characteristics)
      - [2017.1.9. Secondary School Districts Demographic Characteristics](#201719-secondary-school-districts-demographic-characteristics)
      - [2017.1.10. Unified School Districts Demographic Characteristics](#2017110-unified-school-districts-demographic-characteristics)
      - [2017.1.11. Urban Areas Demographic Characteristics](#2017111-urban-areas-demographic-characteristics)
      - [2017.1.12. Public Use Microdata Areas Demographic Characteristics](#2017112-public-use-microdata-areas-demographic-characteristics)
      - [2017.1.13. Block Groups Demographic Characteristics](#2017113-block-groups-demographic-characteristics)
      - [2017.1.14. Census Tracts Demographic Characteristics](#2017114-census-tracts-demographic-characteristics)
    - [2017.2. Social Characteristics](#20172-social-characteristics)
      - [2017.2.1. County Level Social Characteristics](#201721-county-level-social-characteristics)
      - [2017.2.2. County Subdivision Social Characteristics](#201722-county-subdivision-social-characteristics)
      - [2017.2.3. Cities/Places Social Characteristics](#201723-citiesplaces-social-characteristics)
      - [2017.2.4. ZIP Code Tabulation Areas Social Characteristics](#201724-zip-code-tabulation-areas-social-characteristics)
      - [2017.2.5. Congressional Districts Social Characteristics](#201725-congressional-districts-social-characteristics)
      - [2017.2.6. State Assembly Legislative Districts Social Characteristics](#201726-state-assembly-legislative-districts-social-characteristics)
      - [2017.2.7. State Senate Legislative Districts Social Characteristics](#201727-state-senate-legislative-districts-social-characteristics)
      - [2017.2.8. Elementary School Districts Social Characteristics](#201728-elementary-school-districts-social-characteristics)
      - [2017.2.9. Secondary School Districts Social Characteristics](#201729-secondary-school-districts-social-characteristics)
      - [2017.2.10. Unified School Districts Social Characteristics](#2017210-unified-school-districts-social-characteristics)
      - [2017.2.11. Urban Areas Social Characteristics](#2017211-urban-areas-social-characteristics)
      - [2017.2.12. Public Use Microdata Areas Social Characteristics](#2017212-public-use-microdata-areas-social-characteristics)
      - [2017.2.13. Block Groups Social Characteristics](#2017213-block-groups-social-characteristics)
      - [2017.2.14. Census Tracts Social Characteristics](#2017214-census-tracts-social-characteristics)
    - [2017.3. Economic Characteristics](#20173-economic-characteristics)
      - [2017.3.1. County Level Economic Characteristics](#201731-county-level-economic-characteristics)
      - [2017.3.2. County Subdivision Economic Characteristics](#201732-county-subdivision-economic-characteristics)
      - [2017.3.3. Cities/Places Economic Characteristics](#201733-citiesplaces-economic-characteristics)
      - [2017.3.4. ZIP Code Tabulation Areas Economic Characteristics](#201734-zip-code-tabulation-areas-economic-characteristics)
      - [2017.3.5. Congressional Districts Economic Characteristics](#201735-congressional-districts-economic-characteristics)
      - [2017.3.6. State Assembly Legislative Districts Economic Characteristics](#201736-state-assembly-legislative-districts-economic-characteristics)
      - [2017.3.7. State Senate Legislative Districts Economic Characteristics](#201737-state-senate-legislative-districts-economic-characteristics)
      - [2017.3.8. Elementary School Districts Economic Characteristics](#201738-elementary-school-districts-economic-characteristics)
      - [2017.3.9. Secondary School Districts Economic Characteristics](#201739-secondary-school-districts-economic-characteristics)
      - [2017.3.10. Unified School Districts Economic Characteristics](#2017310-unified-school-districts-economic-characteristics)
      - [2017.3.11. Urban Areas Economic Characteristics](#2017311-urban-areas-economic-characteristics)
      - [2017.3.12. Public Use Microdata Areas Economic Characteristics](#2017312-public-use-microdata-areas-economic-characteristics)
      - [2017.3.13. Block Groups Economic Characteristics](#2017313-block-groups-economic-characteristics)
      - [2017.3.14. Census Tracts Economic Characteristics](#2017314-census-tracts-economic-characteristics)
    - [2017.4. Housing Characteristics](#20174-housing-characteristics)
      - [2017.4.1. County Level Housing Characteristics](#201741-county-level-housing-characteristics)
      - [2017.4.2. County Subdivision Housing Characteristics](#201742-county-subdivision-housing-characteristics)
      - [2017.4.3. Cities/Places Housing Characteristics](#201743-citiesplaces-housing-characteristics)
      - [2017.4.4. ZIP Code Tabulation Areas Housing Characteristics](#201744-zip-code-tabulation-areas-housing-characteristics)
      - [2017.4.5. Congressional Districts Housing Characteristics](#201745-congressional-districts-housing-characteristics)
      - [2017.4.6. State Assembly Legislative Districts Housing Characteristics](#201746-state-assembly-legislative-districts-housing-characteristics)
      - [2017.4.7. State Senate Legislative Districts Housing Characteristics](#201747-state-senate-legislative-districts-housing-characteristics)
      - [2017.4.8. Elementary School Districts Housing Characteristics](#201748-elementary-school-districts-housing-characteristics)
      - [2017.4.9. Secondary School Districts Housing Characteristics](#201749-secondary-school-districts-housing-characteristics)
      - [2017.4.10. Unified School Districts Housing Characteristics](#2017410-unified-school-districts-housing-characteristics)
      - [2017.4.11. Urban Areas Housing Characteristics](#2017411-urban-areas-housing-characteristics)
      - [2017.4.12. Public Use Microdata Areas Housing Characteristics](#2017412-public-use-microdata-areas-housing-characteristics)
      - [2017.4.13. Block Groups Housing Characteristics](#2017413-block-groups-housing-characteristics)
      - [2017.4.14. Census Tracts Housing Characteristics](#2017414-census-tracts-housing-characteristics)
  - [Year: 2018](#year-2018)
    - [2018.1. Demographic Characteristics](#20181-demographic-characteristics)
      - [2018.1.1. County Level Demographic Characteristics](#201811-county-level-demographic-characteristics)
      - [2018.1.2. County Subdivision Demographic Characteristics](#201812-county-subdivision-demographic-characteristics)
      - [2018.1.3. Cities/Places Demographic Characteristics](#201813-citiesplaces-demographic-characteristics)
      - [2018.1.4. ZIP Code Tabulation Areas Demographic Characteristics](#201814-zip-code-tabulation-areas-demographic-characteristics)
      - [2018.1.5. Congressional Districts Demographic Characteristics](#201815-congressional-districts-demographic-characteristics)
      - [2018.1.6. State Assembly Legislative Districts Demographic Characteristics](#201816-state-assembly-legislative-districts-demographic-characteristics)
      - [2018.1.7. State Senate Legislative Districts Demographic Characteristics](#201817-state-senate-legislative-districts-demographic-characteristics)
      - [2018.1.8. Elementary School Districts Demographic Characteristics](#201818-elementary-school-districts-demographic-characteristics)
      - [2018.1.9. Secondary School Districts Demographic Characteristics](#201819-secondary-school-districts-demographic-characteristics)
      - [2018.1.10. Unified School Districts Demographic Characteristics](#2018110-unified-school-districts-demographic-characteristics)
      - [2018.1.11. Urban Areas Demographic Characteristics](#2018111-urban-areas-demographic-characteristics)
      - [2018.1.12. Public Use Microdata Areas Demographic Characteristics](#2018112-public-use-microdata-areas-demographic-characteristics)
      - [2018.1.13. Block Groups Demographic Characteristics](#2018113-block-groups-demographic-characteristics)
      - [2018.1.14. Census Tracts Demographic Characteristics](#2018114-census-tracts-demographic-characteristics)
    - [2018.2. Social Characteristics](#20182-social-characteristics)
      - [2018.2.1. County Level Social Characteristics](#201821-county-level-social-characteristics)
      - [2018.2.2. County Subdivision Social Characteristics](#201822-county-subdivision-social-characteristics)
      - [2018.2.3. Cities/Places Social Characteristics](#201823-citiesplaces-social-characteristics)
      - [2018.2.4. ZIP Code Tabulation Areas Social Characteristics](#201824-zip-code-tabulation-areas-social-characteristics)
      - [2018.2.5. Congressional Districts Social Characteristics](#201825-congressional-districts-social-characteristics)
      - [2018.2.6. State Assembly Legislative Districts Social Characteristics](#201826-state-assembly-legislative-districts-social-characteristics)
      - [2018.2.7. State Senate Legislative Districts Social Characteristics](#201827-state-senate-legislative-districts-social-characteristics)
      - [2018.2.8. Elementary School Districts Social Characteristics](#201828-elementary-school-districts-social-characteristics)
      - [2018.2.9. Secondary School Districts Social Characteristics](#201829-secondary-school-districts-social-characteristics)
      - [2018.2.10. Unified School Districts Social Characteristics](#2018210-unified-school-districts-social-characteristics)
      - [2018.2.11. Urban Areas Social Characteristics](#2018211-urban-areas-social-characteristics)
      - [2018.2.12. Public Use Microdata Areas Social Characteristics](#2018212-public-use-microdata-areas-social-characteristics)
      - [2018.2.13. Block Groups Social Characteristics](#2018213-block-groups-social-characteristics)
      - [2018.2.14. Census Tracts Social Characteristics](#2018214-census-tracts-social-characteristics)
    - [2018.3. Economic Characteristics](#20183-economic-characteristics)
      - [2018.3.1. County Level Economic Characteristics](#201831-county-level-economic-characteristics)
      - [2018.3.2. County Subdivision Economic Characteristics](#201832-county-subdivision-economic-characteristics)
      - [2018.3.3. Cities/Places Economic Characteristics](#201833-citiesplaces-economic-characteristics)
      - [2018.3.4. ZIP Code Tabulation Areas Economic Characteristics](#201834-zip-code-tabulation-areas-economic-characteristics)
      - [2018.3.5. Congressional Districts Economic Characteristics](#201835-congressional-districts-economic-characteristics)
      - [2018.3.6. State Assembly Legislative Districts Economic Characteristics](#201836-state-assembly-legislative-districts-economic-characteristics)
      - [2018.3.7. State Senate Legislative Districts Economic Characteristics](#201837-state-senate-legislative-districts-economic-characteristics)
      - [2018.3.8. Elementary School Districts Economic Characteristics](#201838-elementary-school-districts-economic-characteristics)
      - [2018.3.9. Secondary School Districts Economic Characteristics](#201839-secondary-school-districts-economic-characteristics)
      - [2018.3.10. Unified School Districts Economic Characteristics](#2018310-unified-school-districts-economic-characteristics)
      - [2018.3.11. Urban Areas Economic Characteristics](#2018311-urban-areas-economic-characteristics)
      - [2018.3.12. Public Use Microdata Areas Economic Characteristics](#2018312-public-use-microdata-areas-economic-characteristics)
      - [2018.3.13. Block Groups Economic Characteristics](#2018313-block-groups-economic-characteristics)
      - [2018.3.14. Census Tracts Economic Characteristics](#2018314-census-tracts-economic-characteristics)
    - [2018.4. Housing Characteristics](#20184-housing-characteristics)
      - [2018.4.1. County Level Housing Characteristics](#201841-county-level-housing-characteristics)
      - [2018.4.2. County Subdivision Housing Characteristics](#201842-county-subdivision-housing-characteristics)
      - [2018.4.3. Cities/Places Housing Characteristics](#201843-citiesplaces-housing-characteristics)
      - [2018.4.4. ZIP Code Tabulation Areas Housing Characteristics](#201844-zip-code-tabulation-areas-housing-characteristics)
      - [2018.4.5. Congressional Districts Housing Characteristics](#201845-congressional-districts-housing-characteristics)
      - [2018.4.6. State Assembly Legislative Districts Housing Characteristics](#201846-state-assembly-legislative-districts-housing-characteristics)
      - [2018.4.7. State Senate Legislative Districts Housing Characteristics](#201847-state-senate-legislative-districts-housing-characteristics)
      - [2018.4.8. Elementary School Districts Housing Characteristics](#201848-elementary-school-districts-housing-characteristics)
      - [2018.4.9. Secondary School Districts Housing Characteristics](#201849-secondary-school-districts-housing-characteristics)
      - [2018.4.10. Unified School Districts Housing Characteristics](#2018410-unified-school-districts-housing-characteristics)
      - [2018.4.11. Urban Areas Housing Characteristics](#2018411-urban-areas-housing-characteristics)
      - [2018.4.12. Public Use Microdata Areas Housing Characteristics](#2018412-public-use-microdata-areas-housing-characteristics)
      - [2018.4.13. Block Groups Housing Characteristics](#2018413-block-groups-housing-characteristics)
      - [2018.4.14. Census Tracts Housing Characteristics](#2018414-census-tracts-housing-characteristics)
  - [Year: 2019](#year-2019)
    - [2019.1. Demographic Characteristics](#20191-demographic-characteristics)
      - [2019.1.1. County Level Demographic Characteristics](#201911-county-level-demographic-characteristics)
      - [2019.1.2. County Subdivision Demographic Characteristics](#201912-county-subdivision-demographic-characteristics)
      - [2019.1.3. Cities/Places Demographic Characteristics](#201913-citiesplaces-demographic-characteristics)
      - [2019.1.4. ZIP Code Tabulation Areas Demographic Characteristics](#201914-zip-code-tabulation-areas-demographic-characteristics)
      - [2019.1.5. Congressional Districts Demographic Characteristics](#201915-congressional-districts-demographic-characteristics)
      - [2019.1.6. State Assembly Legislative Districts Demographic Characteristics](#201916-state-assembly-legislative-districts-demographic-characteristics)
      - [2019.1.7. State Senate Legislative Districts Demographic Characteristics](#201917-state-senate-legislative-districts-demographic-characteristics)
      - [2019.1.8. Elementary School Districts Demographic Characteristics](#201918-elementary-school-districts-demographic-characteristics)
      - [2019.1.9. Secondary School Districts Demographic Characteristics](#201919-secondary-school-districts-demographic-characteristics)
      - [2019.1.10. Unified School Districts Demographic Characteristics](#2019110-unified-school-districts-demographic-characteristics)
      - [2019.1.11. Urban Areas Demographic Characteristics](#2019111-urban-areas-demographic-characteristics)
      - [2019.1.12. Public Use Microdata Areas Demographic Characteristics](#2019112-public-use-microdata-areas-demographic-characteristics)
      - [2019.1.13. Block Groups Demographic Characteristics](#2019113-block-groups-demographic-characteristics)
      - [2019.1.14. Census Tracts Demographic Characteristics](#2019114-census-tracts-demographic-characteristics)
    - [2019.2. Social Characteristics](#20192-social-characteristics)
      - [2019.2.1. County Level Social Characteristics](#201921-county-level-social-characteristics)
      - [2019.2.2. County Subdivision Social Characteristics](#201922-county-subdivision-social-characteristics)
      - [2019.2.3. Cities/Places Social Characteristics](#201923-citiesplaces-social-characteristics)
      - [2019.2.4. ZIP Code Tabulation Areas Social Characteristics](#201924-zip-code-tabulation-areas-social-characteristics)
      - [2019.2.5. Congressional Districts Social Characteristics](#201925-congressional-districts-social-characteristics)
      - [2019.2.6. State Assembly Legislative Districts Social Characteristics](#201926-state-assembly-legislative-districts-social-characteristics)
      - [2019.2.7. State Senate Legislative Districts Social Characteristics](#201927-state-senate-legislative-districts-social-characteristics)
      - [2019.2.8. Elementary School Districts Social Characteristics](#201928-elementary-school-districts-social-characteristics)
      - [2019.2.9. Secondary School Districts Social Characteristics](#201929-secondary-school-districts-social-characteristics)
      - [2019.2.10. Unified School Districts Social Characteristics](#2019210-unified-school-districts-social-characteristics)
      - [2019.2.11. Urban Areas Social Characteristics](#2019211-urban-areas-social-characteristics)
      - [2019.2.12. Public Use Microdata Areas Social Characteristics](#2019212-public-use-microdata-areas-social-characteristics)
      - [2019.2.13. Block Groups Social Characteristics](#2019213-block-groups-social-characteristics)
      - [2019.2.14. Census Tracts Social Characteristics](#2019214-census-tracts-social-characteristics)
    - [2019.3. Economic Characteristics](#20193-economic-characteristics)
      - [2019.3.1. County Level Economic Characteristics](#201931-county-level-economic-characteristics)
      - [2019.3.2. County Subdivision Economic Characteristics](#201932-county-subdivision-economic-characteristics)
      - [2019.3.3. Cities/Places Economic Characteristics](#201933-citiesplaces-economic-characteristics)
      - [2019.3.4. ZIP Code Tabulation Areas Economic Characteristics](#201934-zip-code-tabulation-areas-economic-characteristics)
      - [2019.3.5. Congressional Districts Economic Characteristics](#201935-congressional-districts-economic-characteristics)
      - [2019.3.6. State Assembly Legislative Districts Economic Characteristics](#201936-state-assembly-legislative-districts-economic-characteristics)
      - [2019.3.7. State Senate Legislative Districts Economic Characteristics](#201937-state-senate-legislative-districts-economic-characteristics)
      - [2019.3.8. Elementary School Districts Economic Characteristics](#201938-elementary-school-districts-economic-characteristics)
      - [2019.3.9. Secondary School Districts Economic Characteristics](#201939-secondary-school-districts-economic-characteristics)
      - [2019.3.10. Unified School Districts Economic Characteristics](#2019310-unified-school-districts-economic-characteristics)
      - [2019.3.11. Urban Areas Economic Characteristics](#2019311-urban-areas-economic-characteristics)
      - [2019.3.12. Public Use Microdata Areas Economic Characteristics](#2019312-public-use-microdata-areas-economic-characteristics)
      - [2019.3.13. Block Groups Economic Characteristics](#2019313-block-groups-economic-characteristics)
      - [2019.3.14. Census Tracts Economic Characteristics](#2019314-census-tracts-economic-characteristics)
    - [2019.4. Housing Characteristics](#20194-housing-characteristics)
      - [2019.4.1. County Level Housing Characteristics](#201941-county-level-housing-characteristics)
      - [2019.4.2. County Subdivision Housing Characteristics](#201942-county-subdivision-housing-characteristics)
      - [2019.4.3. Cities/Places Housing Characteristics](#201943-citiesplaces-housing-characteristics)
      - [2019.4.4. ZIP Code Tabulation Areas Housing Characteristics](#201944-zip-code-tabulation-areas-housing-characteristics)
      - [2019.4.5. Congressional Districts Housing Characteristics](#201945-congressional-districts-housing-characteristics)
      - [2019.4.6. State Assembly Legislative Districts Housing Characteristics](#201946-state-assembly-legislative-districts-housing-characteristics)
      - [2019.4.7. State Senate Legislative Districts Housing Characteristics](#201947-state-senate-legislative-districts-housing-characteristics)
      - [2019.4.8. Elementary School Districts Housing Characteristics](#201948-elementary-school-districts-housing-characteristics)
      - [2019.4.9. Secondary School Districts Housing Characteristics](#201949-secondary-school-districts-housing-characteristics)
      - [2019.4.10. Unified School Districts Housing Characteristics](#2019410-unified-school-districts-housing-characteristics)
      - [2019.4.11. Urban Areas Housing Characteristics](#2019411-urban-areas-housing-characteristics)
      - [2019.4.12. Public Use Microdata Areas Housing Characteristics](#2019412-public-use-microdata-areas-housing-characteristics)
      - [2019.4.13. Block Groups Housing Characteristics](#2019413-block-groups-housing-characteristics)
      - [2019.4.14. Census Tracts Housing Characteristics](#2019414-census-tracts-housing-characteristics)==

<br/><br/>

---
## Year: 2013
---
### 2013.1. Demographic Characteristics
---
> #### 2013.1.1. County Level Demographic Characteristics

- **Name**: OCACS2013COD 
- **Title**: OCACS 2013 County Level Selected Demographic Characteristics
- **Tags**: geodemographics, Orange County, California, US Census, ACS, American Community Survey, Demographic Characteristics, Orange County, age, sex, race, Hispanic or Latino, citizen, voting
- **Summary**: Key demographic characteristics of the 2013 American Community Survey (ACS), 5-year estimates in Orange County, California.
- **Description**: US Census American Community Survey (ACS) 2013, 5-year estimates of the key demographic characteristics for Orange County, California. The data contains 105 fields for the variable groups D01: Sex and age (universe: total population, table X1, 49 fields); D02: Median age by sex and race (universe: total population, table X1, 12 fields); D03: Race (universe: total population, table X2, 8 fields); D04: Race alone or in combinationwith one or more other races (universe: total population, table X2, 7 fields); D05: Hispanic or Latino and race (universe: total population, table X3, 21 fields), and; D06: Citizen voting age population (universe: citizen, 18 and over, table X5, 8 fields). The US Census geodemographic data are based on the 2013 TigerLines across multiple geographies. The spatial geographies were merged with ACS data tables. See full documentation at the OCACS project github page (<https://github.com/ktalexan/OCACS-Geodemographics>).
- **Terms of Use**: Original datasets from US Census TigerLine Geography (<https://www.census.gov/geo/maps-data/data/tiger-line.html>), and American FactFinder (<https://factfinder.census.gov/>) for the selected tables of the American Community Survey (ACS, 2013). Linking and merging geographic with demographic tables along with final production of the merged spatial geodatabase and online datasets are performed by Orange County Public Works, OC Survey Geospatial Services, Dr. Kostas Alexandridis, GISP.
- **Map**: <https://data-ocpw.opendata.arcgis.com/datasets/OCPW::ocacs-2013-demographic-characteristics-for-orange-county>
- **Web**: <https://data-ocpw.opendata.arcgis.com/datasets/OCPW::ocacs-2013-demographic-characteristics-for-orange-county/about>
- **REST**: <https://services.arcgis.com/UXmFoWC7yDHcDN5Q/arcgis/rest/services/OCACS_2013_Demographic_Characteristics_for_Orange_County/FeatureServer/>
- **Metadata**: <https://www.arcgis.com/sharing/rest/content/items/c6ede376a36a46158a1e482a012b5054/info/metadata/metadata.xml?format=default&output=html>
- **GeoService API**: <https://services.arcgis.com/UXmFoWC7yDHcDN5Q/arcgis/rest/services/OCACS_2013_Demographic_Characteristics_for_Orange_County/FeatureServer/1/query?outFields=*&where=1%3D1>
- **GeoJSON API**: <https://services.arcgis.com/UXmFoWC7yDHcDN5Q/arcgis/rest/services/OCACS_2013_Demographic_Characteristics_for_Orange_County/FeatureServer/1/query?outFields=*&where=1%3D1&f=geojson>

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2013.1.2. County Subdivision Demographic Characteristics

- **Name**: OCACS2013CSD
- **Title**: OCACS 2013 County Subdivisions Selected Demographic Characteristics
- **Tags**: geodemographics, Orange County, California, US Census, ACS, American Community Survey, Demographic Characteristics, County Subdivisions, age, sex, race, Hispanic or Latino, citizen, voting
- **Summary**: Key demographic characteristics of the 2013 American Community Survey (ACS), 5-year estimates for County Subdivisions in Orange County, California. 
- **Description**: US Census American Community Survey (ACS) 2013, 5-year estimates of the key demographic characteristics of County Subdivisions geographic level in Orange County, California. The data contains 105 fields for the variable groups D01: Sex and age (universe: total population, table X1, 49 fields); D02: Median age by sex and race (universe: total population, table X1, 12 fields); D03: Race (universe: total population, table X2, 8 fields); D04: Race alone or in combination with one or more other races (universe: total population, table X2, 7 fields); D05: Hispanic or Latino and race (universe: total population, table X3, 21 fields), and; D06: Citizen voting age population (universe: citizen, 18 and over, table X5, 8 fields). The US Census geodemographic data are based on the 2013 TigerLines across multiple geographies. The spatial geographies were merged with ACS data tables. See full documentation at the OCACS project github page (<https://github.com/ktalexan/OCACS-Geodemographics>).
- **Terms of Use**: Original datasets from US Census TigerLine Geography (<https://www.census.gov/geo/maps-data/data/tiger-line.html>), and American FactFinder (<https://factfinder.census.gov/>) for the selected tables of the American Community Survey (ACS, 2013). Linking and merging geographic with demographic tables along with final production of the merged spatial geodatabase and online datasets are performed by Orange County Public Works, OC Survey Geospatial Services, Dr. Kostas Alexandridis, GISP.
- **Map**: <https://data-ocpw.opendata.arcgis.com/datasets/OCPW::ocacs-2013-demographic-characteristics-for-county-subdivisions>
- **Web**: <https://data-ocpw.opendata.arcgis.com/datasets/OCPW::ocacs-2013-demographic-characteristics-for-county-subdivisions/about>
- **REST**: <https://services.arcgis.com/UXmFoWC7yDHcDN5Q/arcgis/rest/services/OCACS_2013_Demographic_Characteristics_for_County_Subdivisions/FeatureServer/>
- **Metadata**: <https://www.arcgis.com/sharing/rest/content/items/f582b6f52e26483590b8cf1514c764e6/info/metadata/metadata.xml?format=default&output=html>
- **GeoService API**: <https://services.arcgis.com/UXmFoWC7yDHcDN5Q/arcgis/rest/services/OCACS_2013_Demographic_Characteristics_for_County_Subdivisions/FeatureServer/1/query?outFields=*&where=1%3D1>
- **GeoJSON API**: <https://services.arcgis.com/UXmFoWC7yDHcDN5Q/arcgis/rest/services/OCACS_2013_Demographic_Characteristics_for_County_Subdivisions/FeatureServer/1/query?outFields=*&where=1%3D1&f=geojson>

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2013.1.3. Cities/Places Demographic Characteristics

- **Name**: OCACS2013PLD
- **Title**: OCACS 2013 Cities Selected Demographic Characteristics
- **Tags**: geodemographics, Orange County, California, US Census, ACS, American Community Survey, Demographic Characteristics, Cities, Places, age, sex, race, Hispanic or Latino, citizen, voting
- **Summary**: Key demographic characteristics of the 2013 American Community Survey (ACS), 5-year estimates for Cities/Places in Orange County, California. 
- **Description**: US Census American Community Survey (ACS) 2013, 5-year estimates of the key demographic characteristics of Cities/Places geographic level in Orange County, California. The data contains 105 fields for the variable groups D01: Sex and age (universe: total population, table X1, 49 fields); D02: Median age by sex and race (universe: total population, table X1, 12 fields); D03: Race (universe: total population, table X2, 8 fields); D04: Race alone or in combination with one or more other races (universe: total population, table X2, 7 fields); D05: Hispanic or Latino and race (universe: total population, table X3, 21 fields), and; D06: Citizen voting age population (universe: citizen, 18 and over, table X5, 8 fields). The US Census geodemographic data are based on the 2013 TigerLines across multiple geographies. The spatial geographies were merged with ACS data tables. See full documentation at the OCACS project github page (<https://github.com/ktalexan/OCACS-Geodemographics>).
- **Terms of Use**: Original datasets from US Census TigerLine Geography (<https://www.census.gov/geo/maps-data/data/tiger-line.html>), and American FactFinder (<https://factfinder.census.gov/>) for the selected tables of the American Community Survey (ACS, 2013). Linking and merging geographic with demographic tables along with final production of the merged spatial geodatabase and online datasets are performed by Orange County Public Works, OC Survey Geospatial Services, Dr. Kostas Alexandridis, GISP.
- **Map**: <https://data-ocpw.opendata.arcgis.com/datasets/OCPW::ocacs-2013-demographic-characteristics-for-cities>
- **Web**: <https://data-ocpw.opendata.arcgis.com/datasets/OCPW::ocacs-2013-demographic-characteristics-for-cities/about>
- **REST**: <https://services.arcgis.com/UXmFoWC7yDHcDN5Q/arcgis/rest/services/OCACS_2013_Demographic_Characteristics_for_Cities/FeatureServer/>
- **Metadata**: <https://www.arcgis.com/sharing/rest/content/items/d06f3b3906e646a2b555c45079475039/info/metadata/metadata.xml?format=default&output=html>
- **GeoService API**: <https://services.arcgis.com/UXmFoWC7yDHcDN5Q/arcgis/rest/services/OCACS_2013_Demographic_Characteristics_for_Cities/FeatureServer/1/query?outFields=*&where=1%3D1>
- **GeoJSON API**: <https://services.arcgis.com/UXmFoWC7yDHcDN5Q/arcgis/rest/services/OCACS_2013_Demographic_Characteristics_for_Cities/FeatureServer/1/query?outFields=*&where=1%3D1&f=geojson>

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2013.1.4. ZIP Code Tabulation Areas Demographic Characteristics

- **Name**: OCACS2013ZCD
- **Title**: OCACS 2013 ZIP Code Tabulation Areas Selected Demographic Characteristics
- **Tags**: geodemographics, Orange County, California, US Census, ACS, American Community Survey, Demographic Characteristics, ZIP Code, age, sex, race, Hispanic or Latino, citizen, voting
- **Summary**: Key demographic characteristics of the 2013 American Community Survey (ACS), 5-year estimates for ZIP Code Tabulation Areas in Orange County, California. 
- **Description**: US Census American Community Survey (ACS) 2013, 5-year estimates of the key demographic characteristics of ZIP Code Tabulation Areas geographic level in Orange County, California. The data contains 105 fields for the variable groups D01: Sex and age (universe: total population, table X1, 49 fields); D02: Median age by sex and race (universe: total population, table X1, 12 fields); D03: Race (universe: total population, table X2, 8 fields); D04: Race alone or in combination with one or more other races (universe: total population, table X2, 7 fields); D05: Hispanic or Latino and race (universe: total population, table X3, 21 fields), and; D06: Citizen voting age population (universe: citizen, 18 and over, table X5, 8 fields). The US Census geodemographic data are based on the 2013 TigerLines across multiple geographies. The spatial geographies were merged with ACS data tables. See full documentation at the OCACS project github page (<https://github.com/ktalexan/OCACS-Geodemographics>).
- **Terms of Use**: Original datasets from US Census TigerLine Geography (<https://www.census.gov/geo/maps-data/data/tiger-line.html>), and American FactFinder (<https://factfinder.census.gov/>) for the selected tables of the American Community Survey (ACS, 2013). Linking and merging geographic with demographic tables along with final production of the merged spatial geodatabase and online datasets are performed by Orange County Public Works, OC Survey Geospatial Services, Dr. Kostas Alexandridis, GISP.
- **Map**: <https://data-ocpw.opendata.arcgis.com/maps/ocacs-2013-demographic-characteristics-for-zip-code-tabulation-areas>
- **Web**: <https://data-ocpw.opendata.arcgis.com/datasets/OCPW::ocacs-2013-demographic-characteristics-for-zip-code-tabulation-areas/about>
- **REST**: <https://services.arcgis.com/UXmFoWC7yDHcDN5Q/arcgis/rest/services/OCACS_2013_Demographic_Characteristics_for_ZIP_Code_Tabulation_Areas/FeatureServer>
- **Metadata**: <https://www.arcgis.com/sharing/rest/content/items/e28bee0162ea4704b1332d5f0c36acbf/info/metadata/metadata.xml?format=default&output=html>
- **GeoService API**: <https://services.arcgis.com/UXmFoWC7yDHcDN5Q/arcgis/rest/services/OCACS_2013_Demographic_Characteristics_for_ZIP_Code_Tabulation_Areas/FeatureServer/1/query?outFields=*&where=1%3D1>
- **GeoJSON API**: <https://services.arcgis.com/UXmFoWC7yDHcDN5Q/arcgis/rest/services/OCACS_2013_Demographic_Characteristics_for_ZIP_Code_Tabulation_Areas/FeatureServer/1/query?outFields=*&where=1%3D1&f=geojson>

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2013.1.5. Congressional Districts Demographic Characteristics

- **Name**: OCACS2013CDD
- **Title**: OCACS 2013 Congressional Districts Selected Demographic Characteristics
- **Tags**: geodemographics, Orange County, California, US Census, ACS, American Community Survey, Demographic Characteristics, Congressional Districts, 115th US Congress, age, sex, race, Hispanic or Latino, citizen, voting
- **Summary**: Key demographic characteristics of the 2013 American Community Survey (ACS), 5-year estimates for Congressional Districts (115th US Congress) in Orange County, California. 
- **Description**: US Census American Community Survey (ACS) 2013, 5-year estimates of the key demographic characteristics of Congressional Districts (115th US Congress) geographic level in Orange County, California. The data contains 105 fields for the variable groups D01: Sex and age (universe: total population, table X1, 49 fields); D02: Median age by sex and race (universe: total population, table X1, 12 fields); D03: Race (universe: total population, table X2, 8 fields); D04: Race alone or in combination with one or more other races (universe: total population, table X2, 7 fields); D05: Hispanic or Latino and race (universe: total population, table X3, 21 fields), and; D06: Citizen voting age population (universe: citizen, 18 and over, table X5, 8 fields). The US Census geodemographic data are based on the 2013 TigerLines across multiple geographies. The spatial geographies were merged with ACS data tables. See full documentation at the OCACS project github page (<https://github.com/ktalexan/OCACS-Geodemographics>).
- **Terms of Use**: Original datasets from US Census TigerLine Geography (<https://www.census.gov/geo/maps-data/data/tiger-line.html>), and American FactFinder (<https://factfinder.census.gov/>) for the selected tables of the American Community Survey (ACS, 2013). Linking and merging geographic with demographic tables along with final production of the merged spatial geodatabase and online datasets are performed by Orange County Public Works, OC Survey Geospatial Services, Dr. Kostas Alexandridis, GISP.
- **Map**: <https://data-ocpw.opendata.arcgis.com/maps/ocacs-2013-demographic-characteristics-for-congressional-districts-of-the-113th-us-congress>
- **Web**: <https://data-ocpw.opendata.arcgis.com/datasets/OCPW::ocacs-2013-demographic-characteristics-for-congressional-districts-of-the-113th-us-congress/about>
- **REST**: <https://services.arcgis.com/UXmFoWC7yDHcDN5Q/arcgis/rest/services/OCACS_2013_Demographic_Characteristics_for_Congressional_Districts_of_the_113th_US_Congress/FeatureServer>
- **Metadata**: <https://www.arcgis.com/sharing/rest/content/items/f2df0ab4709d4a1eb8a729b41e716e61/info/metadata/metadata.xml?format=default&output=html>
- **GeoService API**: <https://services.arcgis.com/UXmFoWC7yDHcDN5Q/arcgis/rest/services/OCACS_2013_Demographic_Characteristics_for_Congressional_Districts_of_the_113th_US_Congress/FeatureServer/1/query?outFields=*&where=1%3D1>
- **GeoJSON API**: <https://services.arcgis.com/UXmFoWC7yDHcDN5Q/arcgis/rest/services/OCACS_2013_Demographic_Characteristics_for_Congressional_Districts_of_the_113th_US_Congress/FeatureServer/1/query?outFields=*&where=1%3D1&f=geojson>

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2013.1.6. State Assembly Legislative Districts Demographic Characteristics

- **Name**: OCACS2013LLD
- **Title**: OCACS 2013 State Assembly Legislative Districts Selected Demographic Characteristics
- **Tags**: geodemographics, Orange County, California, US Census, ACS, American Community Survey, Demographic Characteristics, State Assembly, Legislative Districts, age, sex, race, Hispanic or Latino, citizen, voting
- **Summary**: Key demographic characteristics of the 2013 American Community Survey (ACS), 5-year estimates for State Assembly Legislative Districts (Lower) in Orange County, California. 
- **Description**: US Census American Community Survey (ACS) 2013, 5-year estimates of the key demographic characteristics of State Assembly Legislative Districts (Lower) geographic level in Orange County, California. The data contains 105 fields for the variable groups D01: Sex and age (universe: total population, table X1, 49 fields); D02: Median age by sex and race (universe: total population, table X1, 12 fields); D03: Race (universe: total population, table X2, 8 fields); D04: Race alone or in combination with one or more other races (universe: total population, table X2, 7 fields); D05: Hispanic or Latino and race (universe: total population, table X3, 21 fields), and; D06: Citizen voting age population (universe: citizen, 18 and over, table X5, 8 fields). The US Census geodemographic data are based on the 2013 TigerLines across multiple geographies. The spatial geographies were merged with ACS data tables. See full documentation at the OCACS project github page (<https://github.com/ktalexan/OCACS-Geodemographics>)|
- **Terms of Use**: Original datasets from US Census TigerLine Geography (<https://www.census.gov/geo/maps-data/data/tiger-line.html>), and American FactFinder (<https://factfinder.census.gov/>) for the selected tables of the American Community Survey (ACS, 2013). Linking and merging geographic with demographic tables along with final production of the merged spatial geodatabase and online datasets are performed by Orange County Public Works, OC Survey Geospatial Services, Dr. Kostas Alexandridis, GISP.
- **Map**: <https://data-ocpw.opendata.arcgis.com/maps/ocacs-2013-demographic-characteristics-for-state-assembly-legislative-districts>
- **Web**: <https://data-ocpw.opendata.arcgis.com/datasets/OCPW::ocacs-2013-demographic-characteristics-for-state-assembly-legislative-districts/about>
| REST:<https://services.arcgis.com/UXmFoWC7yDHcDN5Q/arcgis/rest/services/OCACS_2013_Demographic_Characteristics_for_State_Assembly_Legislative_Districts/FeatureServer>
- **Metadata**: <https://www.arcgis.com/sharing/rest/content/items/22a96aceec55446fae59fd938e87cdbd/info/metadata/metadata.xml?format=default&output=html>
- **GeoService API**: <https://services.arcgis.com/UXmFoWC7yDHcDN5Q/arcgis/rest/services/OCACS_2013_Demographic_Characteristics_for_State_Assembly_Legislative_Districts/FeatureServer/1/query?outFields=*&where=1%3D1>
- **GeoJSON API**: <https://services.arcgis.com/UXmFoWC7yDHcDN5Q/arcgis/rest/services/OCACS_2013_Demographic_Characteristics_for_State_Assembly_Legislative_Districts/FeatureServer/1/query?outFields=*&where=1%3D1&f=geojson>

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2013.1.7. State Senate Legislative Districts Demographic Characteristics

- **Name**: OCACS2013ULD
- **Title**: OCACS 2013 State Senate Legislative Districts Selected Demographic Characteristics
- **Tags**: geodemographics, Orange County, California, US Census, ACS, American Community Survey, Demographic Characteristics, State Senate, Legislative Districts, age, sex, race, Hispanic or Latino, citizen, votinggeodemographics, Orange County, California, US Census, ACS, American Community Survey, Demographic Characteristics, State Senate, Legislative Districts, age, sex, race, Hispanic or Latino, citizen, voting
- **Summary**: Key demographic characteristics of the 2013 American Community Survey (ACS), 5-year estimates for State Senate Legislative Districts (Upper) in Orange County, California. 
- **Description**: US Census American Community Survey (ACS) 2013, 5-year estimates of the key demographic characteristics of State Senate Legislative Districts (Upper) geographic level in Orange County, California. The data contains 105 fields for the variable groups D01: Sex and age (universe: total population, table X1, 49 fields); D02: Median age by sex and race (universe: total population, table X1, 12 fields); D03: Race (universe: total population, table X2, 8 fields); D04: Race alone or in combination with one or more other races (universe: total population, table X2, 7 fields); D05: Hispanic or Latino and race (universe: total population, table X3, 21 fields), and; D06: Citizen voting age population (universe: citizen, 18 and over, table X5, 8 fields). The US Census geodemographic data are based on the 2013 TigerLines across multiple geographies. The spatial geographies were merged with ACS data tables. See full documentation at the OCACS project github page (https://github.com/ktalexan/OCACS-Geodemographics).
- **Terms of Use**: Original datasets from US Census TigerLine Geography (https://www.census.gov/geo/maps-data/data/tiger-line.html), and American FactFinder (https://factfinder.census.gov/) for the selected tables of the American Community Survey (ACS, 2013). Linking and merging geographic with demographic tables along with final production of the merged spatial geodatabase and online datasets are performed by Orange County Public Works, OC Survey Geospatial Services, Dr. Kostas Alexandridis, GISP.
- **Map**: https://data-ocpw.opendata.arcgis.com/maps/ocacs-2013-demographic-characteristics-for-state-senate-legislative-districts
- **Web**: https://data-ocpw.opendata.arcgis.com/datasets/OCPW::ocacs-2013-demographic-characteristics-for-state-senate-legislative-districts/about
- **REST**: https://services.arcgis.com/UXmFoWC7yDHcDN5Q/arcgis/rest/services/OCACS_2013_Demographic_Characteristics_for_State_Senate_Legislative_Districts/FeatureServer
- **Metadata**: https://www.arcgis.com/sharing/rest/content/items/f5b700ea8e924b9b8304bdf7f5d4056b/info/metadata/metadata.xml?format=default&output=html
- **GeoService API**: https://services.arcgis.com/UXmFoWC7yDHcDN5Q/arcgis/rest/services/OCACS_2013_Demographic_Characteristics_for_State_Senate_Legislative_Districts/FeatureServer/1/query?outFields=*&where=1%3D1
- **GeoJSON API**: https://services.arcgis.com/UXmFoWC7yDHcDN5Q/arcgis/rest/services/OCACS_2013_Demographic_Characteristics_for_State_Senate_Legislative_Districts/FeatureServer/1/query?outFields=*&where=1%3D1&f=geojson

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2013.1.8. Elementary School Districts Demographic Characteristics

- **Name**: OCACS2013EDD
- **Title**: OCACS 2013 Elementary School Districts Selected Demographic Characteristics
- **Tags**: geodemographics, Orange County, California, US Census, ACS, American Community Survey, Demographic Characteristics, Elementary School Districts, age, sex, race, Hispanic or Latino, citizen, voting
- **Summary**: Key demographic characteristics of the 2013 American Community Survey (ACS), 5-year estimates for Elementary School Districts in Orange County, California.|
- **Description**: US Census American Community Survey (ACS) 2013, 5-year estimates of the key demographic characteristics of Elementary School Districts geographic level in Orange County, California. The data contains 105 fields for the variable groups D01: Sex and age (universe: total population, table X1, 49 fields); D02: Median age by sex and race (universe: total population, table X1, 12 fields); D03: Race (universe: total population, table X2, 8 fields); D04: Race alone or in combination with one or more other races (universe: total population, table X2, 7 fields); D05: Hispanic or Latino and race (universe: total population, table X3, 21 fields), and; D06: Citizen voting age population (universe: citizen, 18 and over, table X5, 8 fields). The US Census geodemographic data are based on the 2013 TigerLines across multiple geographies. The spatial geographies were merged with ACS data tables. See full documentation at the OCACS project github page (https://github.com/ktalexan/OCACS-Geodemographics).
- **Terms of Use**: Original datasets from US Census TigerLine Geography (https://www.census.gov/geo/maps-data/data/tiger-line.html), and American FactFinder (https://factfinder.census.gov/) for the selected tables of the American Community Survey (ACS, 2013). Linking and merging geographic with demographic tables along with final production of the merged spatial geodatabase and online datasets are performed by Orange County Public Works, OC Survey Geospatial Services, Dr. Kostas Alexandridis, GISP.
- **Map**: https://data-ocpw.opendata.arcgis.com/maps/ocacs-2013-demographic-characteristics-for-elementary-school-districts
- **Web**: https://data-ocpw.opendata.arcgis.com/datasets/OCPW::ocacs-2013-demographic-characteristics-for-elementary-school-districts/about
- **REST**: https://services.arcgis.com/UXmFoWC7yDHcDN5Q/arcgis/rest/services/OCACS_2013_Demographic_Characteristics_for_Elementary_School_Districts/FeatureServer
- **Metadata**: https://www.arcgis.com/sharing/rest/content/items/ee499748731441e0a88c9c3534a940aa/info/metadata/metadata.xml?format=default&output=html
- **GeoService API**: https://services.arcgis.com/UXmFoWC7yDHcDN5Q/arcgis/rest/services/OCACS_2013_Demographic_Characteristics_for_Elementary_School_Districts/FeatureServer/1/query?outFields=*&where=1%3D1
- **GeoJSON API**: https://services.arcgis.com/UXmFoWC7yDHcDN5Q/arcgis/rest/services/OCACS_2013_Demographic_Characteristics_for_Elementary_School_Districts/FeatureServer/1/query?outFields=*&where=1%3D1&f=geojson

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2013.1.9. Secondary School Districts Demographic Characteristics

- **Name**: OCACS2013SDD
- **Title**: OCACS 2013 Secondary School Districts Selected Demographic Characteristics
- **Tags**: geodemographics, Orange County, California, US Census, ACS, American Community Survey, Demographic Characteristics, Secondary School Districts, age, sex, race, Hispanic or Latino, citizen, voting
- **Summary**: Key demographic characteristics of the 2013 American Community Survey (ACS), 5-year estimates for Secondary School Districts in Orange County, California. 
- **Description**: US Census American Community Survey (ACS) 2013, 5-year estimates of the key demographic characteristics of Secondary School Districts geographic level in Orange County, California. The data contains 105 fields for the variable groups D01: Sex and age (universe: total population, table X1, 49 fields); D02: Median age by sex and race (universe: total population, table X1, 12 fields); D03: Race (universe: total population, table X2, 8 fields); D04: Race alone or in combination with one or more other races (universe: total population, table X2, 7 fields); D05: Hispanic or Latino and race (universe: total population, table X3, 21 fields), and; D06: Citizen voting age population (universe: citizen, 18 and over, table X5, 8 fields). The US Census geodemographic data are based on the 2013 TigerLines across multiple geographies. The spatial geographies were merged with ACS data tables. See full documentation at the OCACS project github page (https://github.com/ktalexan/OCACS-Geodemographics).
- **Terms of Use**: Original datasets from US Census TigerLine Geography (https://www.census.gov/geo/maps-data/data/tiger-line.html), and American FactFinder (https://factfinder.census.gov/) for the selected tables of the American Community Survey (ACS, 2013). Linking and merging geographic with demographic tables along with final production of the merged spatial geodatabase and online datasets are performed by Orange County Public Works, OC Survey Geospatial Services, Dr. Kostas Alexandridis, GISP.
- **Map**: https://data-ocpw.opendata.arcgis.com/maps/ocacs-2013-demographic-characteristics-for-secondary-school-districts
- **Web**: https://data-ocpw.opendata.arcgis.com/datasets/OCPW::ocacs-2013-demographic-characteristics-for-secondary-school-districts/about
- **REST**: https://services.arcgis.com/UXmFoWC7yDHcDN5Q/arcgis/rest/services/OCACS_2013_Demographic_Characteristics_for_Secondary_School_Districts/FeatureServer
- **Metadata**: https://www.arcgis.com/sharing/rest/content/items/1189c5656e074ee3875ba52b67dc767b/info/metadata/metadata.xml?format=default&output=html
- **GeoService API**: https://services.arcgis.com/UXmFoWC7yDHcDN5Q/arcgis/rest/services/OCACS_2013_Demographic_Characteristics_for_Secondary_School_Districts/FeatureServer/1/query?outFields=*&where=1%3D1
- **GeoJSON API**: https://services.arcgis.com/UXmFoWC7yDHcDN5Q/arcgis/rest/services/OCACS_2013_Demographic_Characteristics_for_Secondary_School_Districts/FeatureServer/1/query?outFields=*&where=1%3D1&f=geojson

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2013.1.10. Unified School Districts Demographic Characteristics

- **Name**: OCACS2013UDD
- **Title**: OCACS 2013 Unified School Districts Selected Demographic Characteristics
- **Tags**: geodemographics, Orange County, California, US Census, ACS, American Community Survey, Demographic Characteristics, Unified School Districts, age, sex, race, Hispanic or Latino, citizen, voting
- **Summary**: Key demographic characteristics of the 2013 American Community Survey (ACS), 5-year estimates for Unified School Districts in Orange County, California. 
- **Description**: US Census American Community Survey (ACS) 2013, 5-year estimates of the key demographic characteristics of Unified School Districts geographic level in Orange County, California. The data contains 105 fields for the variable groups D01: Sex and age (universe: total population, table X1, 49 fields); D02: Median age by sex and race (universe: total population, table X1, 12 fields); D03: Race (universe: total population, table X2, 8 fields); D04: Race alone or in combination with one or more other races (universe: total population, table X2, 7 fields); D05: Hispanic or Latino and race (universe: total population, table X3, 21 fields), and; D06: Citizen voting age population (universe: citizen, 18 and over, table X5, 8 fields). The US Census geodemographic data are based on the 2013 TigerLines across multiple geographies. The spatial geographies were merged with ACS data tables. See full documentation at the OCACS project github page (https://github.com/ktalexan/OCACS-Geodemographics).
- **Terms of Use**: Original datasets from US Census TigerLine Geography (https://www.census.gov/geo/maps-data/data/tiger-line.html), and American FactFinder (https://factfinder.census.gov/) for the selected tables of the American Community Survey (ACS, 2013). Linking and merging geographic with demographic tables along with final production of the merged spatial geodatabase and online datasets are performed by Orange County Public Works, OC Survey Geospatial Services, Dr. Kostas Alexandridis, GISP.
- **Map**: https://data-ocpw.opendata.arcgis.com/maps/ocacs-2013-demographic-characteristics-for-unified-school-districts
- **Web**: https://data-ocpw.opendata.arcgis.com/datasets/OCPW::ocacs-2013-demographic-characteristics-for-unified-school-districts/about
- **REST**: https://services.arcgis.com/UXmFoWC7yDHcDN5Q/arcgis/rest/services/OCACS_2013_Demographic_Characteristics_for_Unified_School_Districts/FeatureServer
- **Metadata**: https://www.arcgis.com/sharing/rest/content/items/567ad4e704fe46d7b706742b5531b213/info/metadata/metadata.xml?format=default&output=html
- **GeoService API**: https://services.arcgis.com/UXmFoWC7yDHcDN5Q/arcgis/rest/services/OCACS_2013_Demographic_Characteristics_for_Unified_School_Districts/FeatureServer/1/query?outFields=*&where=1%3D1
- **GeoJSON API**: https://services.arcgis.com/UXmFoWC7yDHcDN5Q/arcgis/rest/services/OCACS_2013_Demographic_Characteristics_for_Unified_School_Districts/FeatureServer/1/query?outFields=*&where=1%3D1&f=geojson

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2013.1.11. Urban Areas Demographic Characteristics

- **Name**: OCACS2013UAD
- **Title**: OCACS 2013 Urban Areas Selected Demographic Characteristics
- **Tags**: geodemographics, Orange County, California, US Census, ACS, American Community Survey, Demographic Characteristics, Urban Areas, age, sex, race, Hispanic or Latino, citizen, voting
- **Summary**: Key demographic characteristics of the 2013 American Community Survey (ACS), 5-year estimates for Urban Areas in Orange County, California. 
- **Description**: US Census American Community Survey (ACS) 2013, 5-year estimates of the key demographic characteristics of Urban Areas geographic level in Orange County, California. The data contains 105 fields for the variable groups D01: Sex and age (universe: total population, table X1, 49 fields); D02: Median age by sex and race (universe: total population, table X1, 12 fields); D03: Race (universe: total population, table X2, 8 fields); D04: Race alone or in combination with one or more other races (universe: total population, table X2, 7 fields); D05: Hispanic or Latino and race (universe: total population, table X3, 21 fields), and; D06: Citizen voting age population (universe: citizen, 18 and over, table X5, 8 fields). The US Census geodemographic data are based on the 2013 TigerLines across multiple geographies. The spatial geographies were merged with ACS data tables. See full documentation at the OCACS project github page (https://github.com/ktalexan/OCACS-Geodemographics).
- **Terms of Use**: Original datasets from US Census TigerLine Geography (https://www.census.gov/geo/maps-data/data/tiger-line.html), and American FactFinder (https://factfinder.census.gov/) for the selected tables of the American Community Survey (ACS, 2013). Linking and merging geographic with demographic tables along with final production of the merged spatial geodatabase and online datasets are performed by Orange County Public Works, OC Survey Geospatial Services, Dr. Kostas Alexandridis, GISP.
- **Map**: https://data-ocpw.opendata.arcgis.com/maps/ocacs-2013-demographic-characteristics-for-urban-areas
- **Web**: https://data-ocpw.opendata.arcgis.com/datasets/OCPW::ocacs-2013-demographic-characteristics-for-urban-areas/about
- **REST**: https://services.arcgis.com/UXmFoWC7yDHcDN5Q/arcgis/rest/services/OCACS_2013_Demographic_Characteristics_for_Urban_Areas/FeatureServer
- **Metadata**: https://www.arcgis.com/sharing/rest/content/items/39e40149930e4a3283ccee7beee72189/info/metadata/metadata.xml?format=default&output=html
- **GeoService API**: https://services.arcgis.com/UXmFoWC7yDHcDN5Q/arcgis/rest/services/OCACS_2013_Demographic_Characteristics_for_Urban_Areas/FeatureServer/1/query?outFields=*&where=1%3D1
- **GeoJSON API**: https://services.arcgis.com/UXmFoWC7yDHcDN5Q/arcgis/rest/services/OCACS_2013_Demographic_Characteristics_for_Urban_Areas/FeatureServer/1/query?outFields=*&where=1%3D1&f=geojson

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2013.1.12. Public Use Microdata Areas Demographic Characteristics

- **Name**: OCACS2013PUD
- **Title**: OCACS 2013 Public Use Microdata Areas Selected Demographic Characteristics
- **Tags**: geodemographics, Orange County, California, US Census, ACS, American Community Survey, Demographic Characteristics, Public Use Microdata Areas, PUMA, age, sex, race, Hispanic or Latino, citizen, voting
- **Summary**: Key demographic characteristics of the 2013 American Community Survey (ACS), 5-year estimates for Public Use Microdata Areas (PUMA) in Orange County, California. 
- **Description**: US Census American Community Survey (ACS) 2013, 5-year estimates of the key demographic characteristics of Public Use Microdata Areas (PUMA) geographic level in Orange County, California. The data contains 105 fields for the variable groups D01: Sex and age (universe: total population, table X1, 49 fields); D02: Median age by sex and race (universe: total population, table X1, 12 fields); D03: Race (universe: total population, table X2, 8 fields); D04: Race alone or in combination with one or more other races (universe: total population, table X2, 7 fields); D05: Hispanic or Latino and race (universe: total population, table X3, 21 fields), and; D06: Citizen voting age population (universe: citizen, 18 and over, table X5, 8 fields). The US Census geodemographic data are based on the 2013 TigerLines across multiple geographies. The spatial geographies were merged with ACS data tables. See full documentation at the OCACS project github page (https://github.com/ktalexan/OCACS-Geodemographics).
- **Terms of Use**: Original datasets from US Census TigerLine Geography (https://www.census.gov/geo/maps-data/data/tiger-line.html), and American FactFinder (https://factfinder.census.gov/) for the selected tables of the American Community Survey (ACS, 2013). Linking and merging geographic with demographic tables along with final production of the merged spatial geodatabase and online datasets are performed by Orange County Public Works, OC Survey Geospatial Services, Dr. Kostas Alexandridis, GISP.
- **Map**: https://data-ocpw.opendata.arcgis.com/maps/ocacs-2013-demographic-characteristics-for-public-use-microdata-areas
- **Web**: https://data-ocpw.opendata.arcgis.com/datasets/OCPW::ocacs-2013-demographic-characteristics-for-public-use-microdata-areas/about
- **REST**: https://services.arcgis.com/UXmFoWC7yDHcDN5Q/arcgis/rest/services/OCACS_2013_Demographic_Characteristics_for_Public_Use_Microdata_Areas/FeatureServer
- **Metadata**: https://www.arcgis.com/sharing/rest/content/items/2bbcfe2cae6e48afa5600e51af7cbd00/info/metadata/metadata.xml?format=default&output=html
- **GeoService API**: https://services.arcgis.com/UXmFoWC7yDHcDN5Q/arcgis/rest/services/OCACS_2013_Demographic_Characteristics_for_Public_Use_Microdata_Areas/FeatureServer/1/query?outFields=*&where=1%3D1
- **GeoJSON API**: https://services.arcgis.com/UXmFoWC7yDHcDN5Q/arcgis/rest/services/OCACS_2013_Demographic_Characteristics_for_Public_Use_Microdata_Areas/FeatureServer/1/query?outFields=*&where=1%3D1&f=geojson

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2013.1.13. Block Groups Demographic Characteristics

- **Name**: OCACS2013BGD
- **Title**: OCACS 2013 Block Groups Selected Demographic Characteristics
- **Tags**: geodemographics, Orange County, California, US Census, ACS, American Community Survey, Demographic Characteristics, Block Groups, age, sex, race, Hispanic or Latino, citizen, voting
- **Summary**: Key demographic characteristics of the 2013 American Community Survey (ACS), 5-year estimates for Block Groups in Orange County, California. 
- **Description**: US Census American Community Survey (ACS) 2013, 5-year estimates of the key demographic characteristics of Block Groups geographic level in Orange County, California. The data contains 105 fields for the variable groups D01: Sex and age (universe: total population, table X1, 49 fields); D02: Median age by sex and race (universe: total population, table X1, 12 fields); D03: Race (universe: total population, table X2, 8 fields); D04: Race alone or in combination with one or more other races (universe: total population, table X2, 7 fields); D05: Hispanic or Latino and race (universe: total population, table X3, 21 fields), and; D06: Citizen voting age population (universe: citizen, 18 and over, table X5, 8 fields). The US Census geodemographic data are based on the 2013 TigerLines across multiple geographies. The spatial geographies were merged with ACS data tables. See full documentation at the OCACS project github page (https://github.com/ktalexan/OCACS-Geodemographics).
- **Terms of Use**: Original datasets from US Census TigerLine Geography (https://www.census.gov/geo/maps-data/data/tiger-line.html), and American FactFinder (https://factfinder.census.gov/) for the selected tables of the American Community Survey (ACS, 2013). Linking and merging geographic with demographic tables along with final production of the merged spatial geodatabase and online datasets are performed by Orange County Public Works, OC Survey Geospatial Services, Dr. Kostas Alexandridis, GISP.
- **Map**: https://data-ocpw.opendata.arcgis.com/maps/ocacs-2013-demographic-characteristics-for-block-groups
- **Web**: https://data-ocpw.opendata.arcgis.com/datasets/OCPW::ocacs-2013-demographic-characteristics-for-block-groups/about
- **REST**: https://services.arcgis.com/UXmFoWC7yDHcDN5Q/arcgis/rest/services/OCACS_2013_Demographic_Characteristics_for_Block_Groups/FeatureServer
- **Metadata**: https://www.arcgis.com/sharing/rest/content/items/0e115145f2404ba88d1a5694b7855551/info/metadata/metadata.xml?format=default&output=html
- **GeoService API**: https://services.arcgis.com/UXmFoWC7yDHcDN5Q/arcgis/rest/services/OCACS_2013_Demographic_Characteristics_for_Block_Groups/FeatureServer/1/query?outFields=*&where=1%3D1
- **GeoJSON API**: https://services.arcgis.com/UXmFoWC7yDHcDN5Q/arcgis/rest/services/OCACS_2013_Demographic_Characteristics_for_Block_Groups/FeatureServer/1/query?outFields=*&where=1%3D1&f=geojson

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2013.1.14. Census Tracts Demographic Characteristics

- **Name**: OCACS2013TRD
- **Title**: OCACS 2013 Census Tracts Selected Demographic Characteristics
- **Tags**: geodemographics, Orange County, California, US Census, ACS, American Community Survey, Demographic Characteristics, Census Tracts, age, sex, race, Hispanic or Latino, citizen, voting
- **Summary**: Key demographic characteristics of the 2013 American Community Survey (ACS), 5-year estimates for Census Tracts in Orange County, California. 
- **Description**: US Census American Community Survey (ACS) 2013, 5-year estimates of the key demographic characteristics of Census Tracts geographic level in Orange County, California. The data contains 105 fields for the variable groups D01: Sex and age (universe: total population, table X1, 49 fields); D02: Median age by sex and race (universe: total population, table X1, 12 fields); D03: Race (universe: total population, table X2, 8 fields); D04: Race alone or in combination with one or more other races (universe: total population, table X2, 7 fields); D05: Hispanic or Latino and race (universe: total population, table X3, 21 fields), and; D06: Citizen voting age population (universe: citizen, 18 and over, table X5, 8 fields). The US Census geodemographic data are based on the 2013 TigerLines across multiple geographies. The spatial geographies were merged with ACS data tables. See full documentation at the OCACS project github page (https://github.com/ktalexan/OCACS-Geodemographics).
- **Terms of Use**: Original datasets from US Census TigerLine Geography (https://www.census.gov/geo/maps-data/data/tiger-line.html), and American FactFinder (https://factfinder.census.gov/) for the selected tables of the American Community Survey (ACS, 2013). Linking and merging geographic with demographic tables along with final production of the merged spatial geodatabase and online datasets are performed by Orange County Public Works, OC Survey Geospatial Services, Dr. Kostas Alexandridis, GISP.
- **Map**: https://data-ocpw.opendata.arcgis.com/maps/ocacs-2013-demographic-characteristics-for-census-tracts
- **Web**: https://data-ocpw.opendata.arcgis.com/datasets/OCPW::ocacs-2013-demographic-characteristics-for-census-tracts/about
- **REST**: https://services.arcgis.com/UXmFoWC7yDHcDN5Q/arcgis/rest/services/OCACS_2013_Demographic_Characteristics_for_Census_Tracts/FeatureServer
- **Metadata**: https://www.arcgis.com/sharing/rest/content/items/af93e99841bb423a9557b1ee2c8fb53f/info/metadata/metadata.xml?format=default&output=html
- **GeoService API**: https://services.arcgis.com/UXmFoWC7yDHcDN5Q/arcgis/rest/services/OCACS_2013_Demographic_Characteristics_for_Census_Tracts/FeatureServer/1/query?outFields=*&where=1%3D1
- **GeoJSON API**: https://services.arcgis.com/UXmFoWC7yDHcDN5Q/arcgis/rest/services/OCACS_2013_Demographic_Characteristics_for_Census_Tracts/FeatureServer/1/query?outFields=*&where=1%3D1&f=geojson

[<div align="right"><< Back to Contents</div>](#contents)

---
### 2013.2. Social Characteristics
---
> #### 2013.2.1. County Level Social Characteristics

- **Name**: OCACS2013COS
- **Title**: OCACS 2013 County Level Selected Social Characteristics
- **Tags**: geodemographics, Orange County, California, US Census, ACS, American Community Survey, Social Characteristics, Orange County, households, relationship, marital status, Fertility, grandparents, school enrollment, educational attainment, veteran status, disability, residence, place of birth, citizenship, region of birth, language spoken, ancestry, computer use, internet use
- **Summary**: Key social characteristics of the 2013 American Community Survey (ACS), 5-year estimates for Orange County, California.
- **Description**: US Census American Community Survey (ACS) 2013, 5-year estimates of the key social characteristics for Orange County, California. The data contains 500 fields for the variable groups S01: Households by type (universe: total households, table X11, 17 fields); S02: Relationship (universe: population in households, table X9, 19 fields); S03: Marital status (universe: population 15 years and over, table X12, 13 fields); S04: Fertility (universe: women 15-50 years who had birth in the past 12 months, table X13, 11 fields); S05: Grandparents (universe: grandparents living or responsible for own grandchildren under 18 years, table X10, 18 fields); S06: School enrollment (universe: population 3 years old and over enrolled in school, table X14, 17 fields); S07: Educational attainment (universe: population 25 years and over, table X15, 25 fields); S08: Veteran status (universe: civilian population 18 years and over, table X21, 2 fields); S09: Disability status and type by sex and age (universe: total civilian non-institutionalized population, table X18, 77 fields); S10: Disability status by age and health insurance coverage (universe: civilian non-institutionalized population, table X18, 16 fields); S11: Residence 1 year ago (universe: population 1 year and over, table X7, 6 fields); S12: Place of birth (universe: total population, table X5, 27 fields); S13: Citizenship status by nativity in the US (universe: total population, table X5, 6 fields); S14: Year of entry (universe: population born outside the US, table X5, 21 fields); S15: World region of birth of foreign born population (universe: foreign born population, excluding population born at sea, table X5, 25 fields); S16: Language spoken in households (universe: total households, table X16, 6 fields); S17: Language spoken at home (universe: population 5 years and over, table X16, 67 fields); S18: Ancestry (universe: total population reporting ancestry, table X4, 114 fields), and; S19: Computers and internet use (universe: total population in households and total households, table X28, 13 fields). The US Census geodemographic data are based on the 2013 TigerLines across multiple geographies. The spatial geographies were merged with ACS data tables. See full documentation at the OCACS project github page (https://github.com/ktalexan/OCACS-Geodemographics).
- **Terms of Use**: Original datasets from US Census TigerLine Geography (https://www.census.gov/geo/maps-data/data/tiger-line.html), and American FactFinder (https://factfinder.census.gov/) for the selected tables of the American Community Survey (ACS, 2013). Linking and merging geographic with demographic tables along with final production of the merged spatial geodatabase and online datasets are performed by Orange County Public Works, OC Survey Geospatial Services, Dr. Kostas Alexandridis, GISP.
- **Map**: https://data-ocpw.opendata.arcgis.com/maps/ocacs-2013-social-characteristics-for-orange-county
- **Web**: https://data-ocpw.opendata.arcgis.com/datasets/OCPW::ocacs-2013-social-characteristics-for-orange-county/about
- **REST**: https://services.arcgis.com/UXmFoWC7yDHcDN5Q/arcgis/rest/services/OCACS_2013_Social_Characteristics_for_Orange_County/FeatureServer
- **Metadata**: https://www.arcgis.com/sharing/rest/content/items/03a15df1170b4e18871b503f35ad52d8/info/metadata/metadata.xml?format=default&output=html
- **GeoService API**: https://services.arcgis.com/UXmFoWC7yDHcDN5Q/arcgis/rest/services/OCACS_2013_Social_Characteristics_for_Orange_County/FeatureServer/1/query?outFields=*&where=1%3D1
- **GeoJSON API**: https://services.arcgis.com/UXmFoWC7yDHcDN5Q/arcgis/rest/services/OCACS_2013_Social_Characteristics_for_Orange_County/FeatureServer/1/query?outFields=*&where=1%3D1&f=geojson

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2013.2.2. County Subdivision Social Characteristics

- **Name**: OCACS2013CSS
- **Title**: OCACS 2013 County Subdivisions Selected Social Characteristics
- **Tags**: geodemographics, Orange County, California, US Census, ACS, American Community Survey, Social Characteristics, County Subdivisions, households, relationship, marital status, Fertility, grandparents, school enrollment, educational attainment, veteran status, disability, residence, place of birth, citizenship, region of birth, language spoken, ancestry, computer use, internet use
- **Summary**: Key social characteristics of the 2013 American Community Survey (ACS), 5-year estimates for County Subdivisions in Orange County, California.
- **Description**: US Census American Community Survey (ACS) 2013, 5-year estimates of the key social characteristics of County Subdivisions geographic level in Orange County, California. The data contains 500 fields for the variable groups S01: Households by type (universe: total households, table X11, 17 fields); S02: Relationship (universe: population in households, table X9, 19 fields); S03: Marital status (universe: population 15 years and over, table X12, 13 fields); S04: Fertility (universe: women 15-50 years who had birth in the past 12 months, table X13, 11 fields); S05: Grandparents (universe: grandparents living or responsible for own grandchildren under 18 years, table X10, 18 fields); S06: School enrollment (universe: population 3 years old and over enrolled in school, table X14, 17 fields); S07: Educational attainment (universe: population 25 years and over, table X15, 25 fields); S08: Veteran status (universe: civilian population 18 years and over, table X21, 2 fields); S09: Disability status and type by sex and age (universe: total civilian non-institutionalized population, table X18, 77 fields); S10: Disability status by age and health insurance coverage (universe: civilian non-institutionalized population, table X18, 16 fields); S11: Residence 1 year ago (universe: population 1 year and over, table X7, 6 fields); S12: Place of birth (universe: total population, table X5, 27 fields); S13: Citizenship status by nativity in the US (universe: total population, table X5, 6 fields); S14: Year of entry (universe: population born outside the US, table X5, 21 fields); S15: World region of birth of foreign born population (universe: foreign born population, excluding population born at sea, table X5, 25 fields); S16: Language spoken in households (universe: total households, table X16, 6 fields); S17: Language spoken at home (universe: population 5 years and over, table X16, 67 fields); S18: Ancestry (universe: total population reporting ancestry, table X4, 114 fields), and; S19: Computers and internet use (universe: total population in households and total households, table X28, 13 fields). The US Census geodemographic data are based on the 2013 TigerLines across multiple geographies. The spatial geographies were merged with ACS data tables. See full documentation at the OCACS project github page (https://github.com/ktalexan/OCACS-Geodemographics).
- **Terms of Use**: Original datasets from US Census TigerLine Geography (https://www.census.gov/geo/maps-data/data/tiger-line.html), and American FactFinder (https://factfinder.census.gov/) for the selected tables of the American Community Survey (ACS, 2013). Linking and merging geographic with demographic tables along with final production of the merged spatial geodatabase and online datasets are performed by Orange County Public Works, OC Survey Geospatial Services, Dr. Kostas Alexandridis, GISP.
- **Map**: https://data-ocpw.opendata.arcgis.com/maps/ocacs-2013-social-characteristics-for-county-subdivisions
- **Web**: https://data-ocpw.opendata.arcgis.com/datasets/OCPW::ocacs-2013-social-characteristics-for-county-subdivisions/about
- **REST**: https://services.arcgis.com/UXmFoWC7yDHcDN5Q/arcgis/rest/services/OCACS_2013_Social_Characteristics_for_County_Subdivisions/FeatureServer
- **Metadata**: https://www.arcgis.com/sharing/rest/content/items/29312e159f694aac853ce2f6c3845226/info/metadata/metadata.xml?format=default&output=html
- **GeoService API**: https://services.arcgis.com/UXmFoWC7yDHcDN5Q/arcgis/rest/services/OCACS_2013_Social_Characteristics_for_County_Subdivisions/FeatureServer/1/query?outFields=*&where=1%3D1
- **GeoJSON API**: https://services.arcgis.com/UXmFoWC7yDHcDN5Q/arcgis/rest/services/OCACS_2013_Social_Characteristics_for_County_Subdivisions/FeatureServer/1/query?outFields=*&where=1%3D1&f=geojson

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2013.2.3. Cities/Places Social Characteristics

- **Name**: OCACS2013PLS
- **Title**: OCACS 2013 Cities Selected Social Characteristics
- **Tags**: geodemographics, Orange County, California, US Census, ACS, American Community Survey, Social Characteristics, Cities, Places, households, relationship, marital status, Fertility, grandparents, school enrollment, educational attainment, veteran status, disability, residence, place of birth, citizenship, region of birth, language spoken, ancestry, computer use, internet use
- **Summary**: Key social characteristics of the 2013 American Community Survey (ACS), 5-year estimates for Cities/Places in Orange County, California.
- **Description**: US Census American Community Survey (ACS) 2013, 5-year estimates of the key social characteristics of Cities/Places geographic level in Orange County, California. The data contains 500 fields for the variable groups S01: Households by type (universe: total households, table X11, 17 fields); S02: Relationship (universe: population in households, table X9, 19 fields); S03: Marital status (universe: population 15 years and over, table X12, 13 fields); S04: Fertility (universe: women 15-50 years who had birth in the past 12 months, table X13, 11 fields); S05: Grandparents (universe: grandparents living or responsible for own grandchildren under 18 years, table X10, 18 fields); S06: School enrollment (universe: population 3 years old and over enrolled in school, table X14, 17 fields); S07: Educational attainment (universe: population 25 years and over, table X15, 25 fields); S08: Veteran status (universe: civilian population 18 years and over, table X21, 2 fields); S09: Disability status and type by sex and age (universe: total civilian non-institutionalized population, table X18, 77 fields); S10: Disability status by age and health insurance coverage (universe: civilian non-institutionalized population, table X18, 16 fields); S11: Residence 1 year ago (universe: population 1 year and over, table X7, 6 fields); S12: Place of birth (universe: total population, table X5, 27 fields); S13: Citizenship status by nativity in the US (universe: total population, table X5, 6 fields); S14: Year of entry (universe: population born outside the US, table X5, 21 fields); S15: World region of birth of foreign born population (universe: foreign born population, excluding population born at sea, table X5, 25 fields); S16: Language spoken in households (universe: total households, table X16, 6 fields); S17: Language spoken at home (universe: population 5 years and over, table X16, 67 fields); S18: Ancestry (universe: total population reporting ancestry, table X4, 114 fields), and; S19: Computers and internet use (universe: total population in households and total households, table X28, 13 fields). The US Census geodemographic data are based on the 2013 TigerLines across multiple geographies. The spatial geographies were merged with ACS data tables. See full documentation at the OCACS project github page (https://github.com/ktalexan/OCACS-Geodemographics).
- **Terms of Use**: Original datasets from US Census TigerLine Geography (https://www.census.gov/geo/maps-data/data/tiger-line.html), and American FactFinder (https://factfinder.census.gov/) for the selected tables of the American Community Survey (ACS, 2013). Linking and merging geographic with demographic tables along with final production of the merged spatial geodatabase and online datasets are performed by Orange County Public Works, OC Survey Geospatial Services, Dr. Kostas Alexandridis, GISP.
- **Map**: https://data-ocpw.opendata.arcgis.com/maps/ocacs-2013-social-characteristics-for-cities
- **Web**: https://data-ocpw.opendata.arcgis.com/datasets/OCPW::ocacs-2013-social-characteristics-for-cities/about
- **REST**: https://services.arcgis.com/UXmFoWC7yDHcDN5Q/arcgis/rest/services/OCACS_2013_Social_Characteristics_for_Cities/FeatureServer
- **Metadata**: https://www.arcgis.com/sharing/rest/content/items/755451e8674744f9ae8734a4619a40a6/info/metadata/metadata.xml?format=default&output=html
- **GeoService API**: https://services.arcgis.com/UXmFoWC7yDHcDN5Q/arcgis/rest/services/OCACS_2013_Social_Characteristics_for_Cities/FeatureServer/1/query?outFields=*&where=1%3D1
- **GeoJSON API**: https://services.arcgis.com/UXmFoWC7yDHcDN5Q/arcgis/rest/services/OCACS_2013_Social_Characteristics_for_Cities/FeatureServer/1/query?outFields=*&where=1%3D1&f=geojson

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2013.2.4. ZIP Code Tabulation Areas Social Characteristics

- **Name**: OCACS2013ZCS
- **Title**: OCACS 2013 ZIP Code Tabulation Areas Selected Social Characteristics
- **Tags**: geodemographics, Orange County, California, US Census, ACS, American Community Survey, Social Characteristics, ZIP Code, households, relationship, marital status, Fertility, grandparents, school enrollment, educational attainment, veteran status, disability, residence, place of birth, citizenship, region of birth, language spoken, ancestry, computer use, internet use
- **Summary**: Key social characteristics of the 2013 American Community Survey (ACS), 5-year estimates for ZIP Code Tabulation Areas in Orange County, California.
- **Description**: US Census American Community Survey (ACS) 2013, 5-year estimates of the key social characteristics of ZIP Code Tabulation Areas geographic level in Orange County, California. The data contains 500 fields for the variable groups S01: Households by type (universe: total households, table X11, 17 fields); S02: Relationship (universe: population in households, table X9, 19 fields); S03: Marital status (universe: population 15 years and over, table X12, 13 fields); S04: Fertility (universe: women 15-50 years who had birth in the past 12 months, table X13, 11 fields); S05: Grandparents (universe: grandparents living or responsible for own grandchildren under 18 years, table X10, 18 fields); S06: School enrollment (universe: population 3 years old and over enrolled in school, table X14, 17 fields); S07: Educational attainment (universe: population 25 years and over, table X15, 25 fields); S08: Veteran status (universe: civilian population 18 years and over, table X21, 2 fields); S09: Disability status and type by sex and age (universe: total civilian non-institutionalized population, table X18, 77 fields); S10: Disability status by age and health insurance coverage (universe: civilian non-institutionalized population, table X18, 16 fields); S11: Residence 1 year ago (universe: population 1 year and over, table X7, 6 fields); S12: Place of birth (universe: total population, table X5, 27 fields); S13: Citizenship status by nativity in the US (universe: total population, table X5, 6 fields); S14: Year of entry (universe: population born outside the US, table X5, 21 fields); S15: World region of birth of foreign born population (universe: foreign born population, excluding population born at sea, table X5, 25 fields); S16: Language spoken in households (universe: total households, table X16, 6 fields); S17: Language spoken at home (universe: population 5 years and over, table X16, 67 fields); S18: Ancestry (universe: total population reporting ancestry, table X4, 114 fields), and; S19: Computers and internet use (universe: total population in households and total households, table X28, 13 fields). The US Census geodemographic data are based on the 2013 TigerLines across multiple geographies. The spatial geographies were merged with ACS data tables. See full documentation at the OCACS project github page (https://github.com/ktalexan/OCACS-Geodemographics).
- **Terms of Use**: Original datasets from US Census TigerLine Geography (https://www.census.gov/geo/maps-data/data/tiger-line.html), and American FactFinder (https://factfinder.census.gov/) for the selected tables of the American Community Survey (ACS, 2013). Linking and merging geographic with demographic tables along with final production of the merged spatial geodatabase and online datasets are performed by Orange County Public Works, OC Survey Geospatial Services, Dr. Kostas Alexandridis, GISP.
- **Map**: https://data-ocpw.opendata.arcgis.com/maps/ocacs-2013-social-characteristics-for-zip-code-tabulation-areas
- **Web**: https://data-ocpw.opendata.arcgis.com/datasets/OCPW::ocacs-2013-social-characteristics-for-zip-code-tabulation-areas/about
- **REST**: https://services.arcgis.com/UXmFoWC7yDHcDN5Q/arcgis/rest/services/OCACS_2013_Social_Characteristics_for_ZIP_Code_Tabulation_Areas/FeatureServer
- **Metadata**: https://www.arcgis.com/sharing/rest/content/items/02cf6cfd262c4a6c97ffd93223c32f4b/info/metadata/metadata.xml?format=default&output=html
- **GeoService API**: https://services.arcgis.com/UXmFoWC7yDHcDN5Q/arcgis/rest/services/OCACS_2013_Social_Characteristics_for_ZIP_Code_Tabulation_Areas/FeatureServer/1/query?outFields=*&where=1%3D1
- **GeoJSON API**: https://services.arcgis.com/UXmFoWC7yDHcDN5Q/arcgis/rest/services/OCACS_2013_Social_Characteristics_for_ZIP_Code_Tabulation_Areas/FeatureServer/1/query?outFields=*&where=1%3D1&f=geojson

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2013.2.5. Congressional Districts Social Characteristics

- **Name**: OCACS2013CDS
- **Title**: OCACS 2013 Congressional Districts Selected Social Characteristics
- **Tags**: geodemographics, Orange County, California, US Census, ACS, American Community Survey, Social Characteristics, Congressional Districts, 115th US Congress, households, relationship, marital status, Fertility, grandparents, school enrollment, educational attainment, veteran status, disability, residence, place of birth, citizenship, region of birth, language spoken, ancestry, computer use, internet use
- **Summary**: Key social characteristics of the 2013 American Community Survey (ACS), 5-year estimates for Congressional Districts (115th US Congress) in Orange County, California.
- **Description**: US Census American Community Survey (ACS) 2013, 5-year estimates of the key social characteristics of Congressional Districts (115th US Congress) geographic level in Orange County, California. The data contains 500 fields for the variable groups S01: Households by type (universe: total households, table X11, 17 fields); S02: Relationship (universe: population in households, table X9, 19 fields); S03: Marital status (universe: population 15 years and over, table X12, 13 fields); S04: Fertility (universe: women 15-50 years who had birth in the past 12 months, table X13, 11 fields); S05: Grandparents (universe: grandparents living or responsible for own grandchildren under 18 years, table X10, 18 fields); S06: School enrollment (universe: population 3 years old and over enrolled in school, table X14, 17 fields); S07: Educational attainment (universe: population 25 years and over, table X15, 25 fields); S08: Veteran status (universe: civilian population 18 years and over, table X21, 2 fields); S09: Disability status and type by sex and age (universe: total civilian non-institutionalized population, table X18, 77 fields); S10: Disability status by age and health insurance coverage (universe: civilian non-institutionalized population, table X18, 16 fields); S11: Residence 1 year ago (universe: population 1 year and over, table X7, 6 fields); S12: Place of birth (universe: total population, table X5, 27 fields); S13: Citizenship status by nativity in the US (universe: total population, table X5, 6 fields); S14: Year of entry (universe: population born outside the US, table X5, 21 fields); S15: World region of birth of foreign born population (universe: foreign born population, excluding population born at sea, table X5, 25 fields); S16: Language spoken in households (universe: total households, table X16, 6 fields); S17: Language spoken at home (universe: population 5 years and over, table X16, 67 fields); S18: Ancestry (universe: total population reporting ancestry, table X4, 114 fields), and; S19: Computers and internet use (universe: total population in households and total households, table X28, 13 fields). The US Census geodemographic data are based on the 2013 TigerLines across multiple geographies. The spatial geographies were merged with ACS data tables. See full documentation at the OCACS project github page (https://github.com/ktalexan/OCACS-Geodemographics).
- **Terms of Use**: Original datasets from US Census TigerLine Geography (https://www.census.gov/geo/maps-data/data/tiger-line.html), and American FactFinder (https://factfinder.census.gov/) for the selected tables of the American Community Survey (ACS, 2013). Linking and merging geographic with demographic tables along with final production of the merged spatial geodatabase and online datasets are performed by Orange County Public Works, OC Survey Geospatial Services, Dr. Kostas Alexandridis, GISP.
- **Map**: https://data-ocpw.opendata.arcgis.com/maps/ocacs-2013-social-characteristics-for-congressional-districts-of-the-113th-us-congress
- **Web**: https://data-ocpw.opendata.arcgis.com/datasets/OCPW::ocacs-2013-social-characteristics-for-congressional-districts-of-the-113th-us-congress/about
- **REST**: https://services.arcgis.com/UXmFoWC7yDHcDN5Q/arcgis/rest/services/OCACS_2013_Social_Characteristics_for_Congressional_Districts_of_the_113th_US_Congress/FeatureServer
- **Metadata**: https://www.arcgis.com/sharing/rest/content/items/e5b62440345d44f29b6dd6120d3751db/info/metadata/metadata.xml?format=default&output=html
- **GeoService API**: https://services.arcgis.com/UXmFoWC7yDHcDN5Q/arcgis/rest/services/OCACS_2013_Social_Characteristics_for_Congressional_Districts_of_the_113th_US_Congress/FeatureServer/1/query?outFields=*&where=1%3D1
- **GeoJSON API**: https://services.arcgis.com/UXmFoWC7yDHcDN5Q/arcgis/rest/services/OCACS_2013_Social_Characteristics_for_Congressional_Districts_of_the_113th_US_Congress/FeatureServer/1/query?outFields=*&where=1%3D1&f=geojson

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2013.2.6. State Assembly Legislative Districts Social Characteristics

- **Name**: OCACS2013LLS
- **Title**: OCACS 2013 State Assembly Legislative Districts Selected Social Characteristics
- **Tags**: geodemographics, Orange County, California, US Census, ACS, American Community Survey, Social Characteristics, State Assembly, Legislative Districts, households, relationship, marital status, Fertility, grandparents, school enrollment, educational attainment, veteran status, disability, residence, place of birth, citizenship, region of birth, language spoken, ancestry, computer use, internet use
- **Summary**: Key social characteristics of the 2013 American Community Survey (ACS), 5-year estimates for State Assembly Legislative Districts (Lower) in Orange County, California.
- **Description**: US Census American Community Survey (ACS) 2013, 5-year estimates of the key social characteristics of State Assembly Legislative Districts (Lower) geographic level in Orange County, California. The data contains 500 fields for the variable groups S01: Households by type (universe: total households, table X11, 17 fields); S02: Relationship (universe: population in households, table X9, 19 fields); S03: Marital status (universe: population 15 years and over, table X12, 13 fields); S04: Fertility (universe: women 15-50 years who had birth in the past 12 months, table X13, 11 fields); S05: Grandparents (universe: grandparents living or responsible for own grandchildren under 18 years, table X10, 18 fields); S06: School enrollment (universe: population 3 years old and over enrolled in school, table X14, 17 fields); S07: Educational attainment (universe: population 25 years and over, table X15, 25 fields); S08: Veteran status (universe: civilian population 18 years and over, table X21, 2 fields); S09: Disability status and type by sex and age (universe: total civilian non-institutionalized population, table X18, 77 fields); S10: Disability status by age and health insurance coverage (universe: civilian non-institutionalized population, table X18, 16 fields); S11: Residence 1 year ago (universe: population 1 year and over, table X7, 6 fields); S12: Place of birth (universe: total population, table X5, 27 fields); S13: Citizenship status by nativity in the US (universe: total population, table X5, 6 fields); S14: Year of entry (universe: population born outside the US, table X5, 21 fields); S15: World region of birth of foreign born population (universe: foreign born population, excluding population born at sea, table X5, 25 fields); S16: Language spoken in households (universe: total households, table X16, 6 fields); S17: Language spoken at home (universe: population 5 years and over, table X16, 67 fields); S18: Ancestry (universe: total population reporting ancestry, table X4, 114 fields), and; S19: Computers and internet use (universe: total population in households and total households, table X28, 13 fields). The US Census geodemographic data are based on the 2013 TigerLines across multiple geographies. The spatial geographies were merged with ACS data tables. See full documentation at the OCACS project github page (https://github.com/ktalexan/OCACS-Geodemographics).
- **Terms of Use**: Original datasets from US Census TigerLine Geography (https://www.census.gov/geo/maps-data/data/tiger-line.html), and American FactFinder (https://factfinder.census.gov/) for the selected tables of the American Community Survey (ACS, 2013). Linking and merging geographic with demographic tables along with final production of the merged spatial geodatabase and online datasets are performed by Orange County Public Works, OC Survey Geospatial Services, Dr. Kostas Alexandridis, GISP.
- **Map**: https://data-ocpw.opendata.arcgis.com/maps/ocacs-2013-social-characteristics-for-state-assembly-legislative-districts
- **Web**: https://data-ocpw.opendata.arcgis.com/datasets/OCPW::ocacs-2013-social-characteristics-for-state-assembly-legislative-districts/about
- **REST**: https://services.arcgis.com/UXmFoWC7yDHcDN5Q/arcgis/rest/services/OCACS_2013_Social_Characteristics_for_State_Assembly_Legislative_Districts/FeatureServer
- **Metadata**: https://www.arcgis.com/sharing/rest/content/items/2682ced5a44345f8a8af5e0e144a19bd/info/metadata/metadata.xml?format=default&output=html
- **GeoService API**: https://services.arcgis.com/UXmFoWC7yDHcDN5Q/arcgis/rest/services/OCACS_2013_Social_Characteristics_for_State_Assembly_Legislative_Districts/FeatureServer/1/query?outFields=*&where=1%3D1
- **GeoJSON API**: https://services.arcgis.com/UXmFoWC7yDHcDN5Q/arcgis/rest/services/OCACS_2013_Social_Characteristics_for_State_Assembly_Legislative_Districts/FeatureServer/1/query?outFields=*&where=1%3D1&f=geojson

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2013.2.7. State Senate Legislative Districts Social Characteristics

- **Name**: OCACS2013ULS
- **Title**: OCACS 2013 State Senate Legislative Districts Selected Social Characteristics
- **Tags**: geodemographics, Orange County, California, US Census, ACS, American Community Survey, Social Characteristics, State Senate, Legislative Districts, households, relationship, marital status, Fertility, grandparents, school enrollment, educational attainment, veteran status, disability, residence, place of birth, citizenship, region of birth, language spoken, ancestry, computer use, internet use
- **Summary**: Key social characteristics of the 2013 American Community Survey (ACS), 5-year estimates for State Senate Legislative Districts (Upper) in Orange County, California.
- **Description**: US Census American Community Survey (ACS) 2013, 5-year estimates of the key social characteristics of State Senate Legislative Districts (Upper) geographic level in Orange County, California. The data contains 500 fields for the variable groups S01: Households by type (universe: total households, table X11, 17 fields); S02: Relationship (universe: population in households, table X9, 19 fields); S03: Marital status (universe: population 15 years and over, table X12, 13 fields); S04: Fertility (universe: women 15-50 years who had birth in the past 12 months, table X13, 11 fields); S05: Grandparents (universe: grandparents living or responsible for own grandchildren under 18 years, table X10, 18 fields); S06: School enrollment (universe: population 3 years old and over enrolled in school, table X14, 17 fields); S07: Educational attainment (universe: population 25 years and over, table X15, 25 fields); S08: Veteran status (universe: civilian population 18 years and over, table X21, 2 fields); S09: Disability status and type by sex and age (universe: total civilian non-institutionalized population, table X18, 77 fields); S10: Disability status by age and health insurance coverage (universe: civilian non-institutionalized population, table X18, 16 fields); S11: Residence 1 year ago (universe: population 1 year and over, table X7, 6 fields); S12: Place of birth (universe: total population, table X5, 27 fields); S13: Citizenship status by nativity in the US (universe: total population, table X5, 6 fields); S14: Year of entry (universe: population born outside the US, table X5, 21 fields); S15: World region of birth of foreign born population (universe: foreign born population, excluding population born at sea, table X5, 25 fields); S16: Language spoken in households (universe: total households, table X16, 6 fields); S17: Language spoken at home (universe: population 5 years and over, table X16, 67 fields); S18: Ancestry (universe: total population reporting ancestry, table X4, 114 fields), and; S19: Computers and internet use (universe: total population in households and total households, table X28, 13 fields). The US Census geodemographic data are based on the 2013 TigerLines across multiple geographies. The spatial geographies were merged with ACS data tables. See full documentation at the OCACS project github page (https://github.com/ktalexan/OCACS-Geodemographics).
- **Terms of Use**: Original datasets from US Census TigerLine Geography (https://www.census.gov/geo/maps-data/data/tiger-line.html), and American FactFinder (https://factfinder.census.gov/) for the selected tables of the American Community Survey (ACS, 2013). Linking and merging geographic with demographic tables along with final production of the merged spatial geodatabase and online datasets are performed by Orange County Public Works, OC Survey Geospatial Services, Dr. Kostas Alexandridis, GISP.
- **Map**: https://data-ocpw.opendata.arcgis.com/maps/ocacs-2013-social-characteristics-for-state-senate-legislative-districts
- **Web**: https://data-ocpw.opendata.arcgis.com/datasets/OCPW::ocacs-2013-social-characteristics-for-state-senate-legislative-districts/about
- **REST**: https://services.arcgis.com/UXmFoWC7yDHcDN5Q/arcgis/rest/services/OCACS_2013_Social_Characteristics_for_State_Senate_Legislative_Districts/FeatureServer
- **Metadata**: https://www.arcgis.com/sharing/rest/content/items/d0b2f63ea44b4079a2db174ff1c15553/info/metadata/metadata.xml?format=default&output=html
- **GeoService API**: https://services.arcgis.com/UXmFoWC7yDHcDN5Q/arcgis/rest/services/OCACS_2013_Social_Characteristics_for_State_Senate_Legislative_Districts/FeatureServer/1/query?outFields=*&where=1%3D1
- **GeoJSON API**: https://services.arcgis.com/UXmFoWC7yDHcDN5Q/arcgis/rest/services/OCACS_2013_Social_Characteristics_for_State_Senate_Legislative_Districts/FeatureServer/1/query?outFields=*&where=1%3D1&f=geojson

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2013.2.8. Elementary School Districts Social Characteristics

- **Name**: OCACS2013EDS
- **Title**: OCACS 2013 Elementary School Districts Selected Social Characteristics
- **Tags**: geodemographics, Orange County, California, US Census, ACS, American Community Survey, Social Characteristics, Elementary School Districts, households, relationship, marital status, Fertility, grandparents, school enrollment, educational attainment, veteran status, disability, residence, place of birth, citizenship, region of birth, language spoken, ancestry, computer use, internet use
- **Summary**: Key social characteristics of the 2013 American Community Survey (ACS), 5-year estimates for Elementary School Districts in Orange County, California.
- **Description**: US Census American Community Survey (ACS) 2013, 5-year estimates of the key social characteristics of Elementary School Districts geographic level in Orange County, California. The data contains 500 fields for the variable groups S01: Households by type (universe: total households, table X11, 17 fields); S02: Relationship (universe: population in households, table X9, 19 fields); S03: Marital status (universe: population 15 years and over, table X12, 13 fields); S04: Fertility (universe: women 15-50 years who had birth in the past 12 months, table X13, 11 fields); S05: Grandparents (universe: grandparents living or responsible for own grandchildren under 18 years, table X10, 18 fields); S06: School enrollment (universe: population 3 years old and over enrolled in school, table X14, 17 fields); S07: Educational attainment (universe: population 25 years and over, table X15, 25 fields); S08: Veteran status (universe: civilian population 18 years and over, table X21, 2 fields); S09: Disability status and type by sex and age (universe: total civilian non-institutionalized population, table X18, 77 fields); S10: Disability status by age and health insurance coverage (universe: civilian non-institutionalized population, table X18, 16 fields); S11: Residence 1 year ago (universe: population 1 year and over, table X7, 6 fields); S12: Place of birth (universe: total population, table X5, 27 fields); S13: Citizenship status by nativity in the US (universe: total population, table X5, 6 fields); S14: Year of entry (universe: population born outside the US, table X5, 21 fields); S15: World region of birth of foreign born population (universe: foreign born population, excluding population born at sea, table X5, 25 fields); S16: Language spoken in households (universe: total households, table X16, 6 fields); S17: Language spoken at home (universe: population 5 years and over, table X16, 67 fields); S18: Ancestry (universe: total population reporting ancestry, table X4, 114 fields), and; S19: Computers and internet use (universe: total population in households and total households, table X28, 13 fields). The US Census geodemographic data are based on the 2013 TigerLines across multiple geographies. The spatial geographies were merged with ACS data tables. See full documentation at the OCACS project github page (https://github.com/ktalexan/OCACS-Geodemographics).
- **Terms of Use**: Original datasets from US Census TigerLine Geography (https://www.census.gov/geo/maps-data/data/tiger-line.html), and American FactFinder (https://factfinder.census.gov/) for the selected tables of the American Community Survey (ACS, 2013). Linking and merging geographic with demographic tables along with final production of the merged spatial geodatabase and online datasets are performed by Orange County Public Works, OC Survey Geospatial Services, Dr. Kostas Alexandridis, GISP.
- **Map**: https://data-ocpw.opendata.arcgis.com/maps/ocacs-2013-social-characteristics-for-elementary-school-districts
- **Web**: https://data-ocpw.opendata.arcgis.com/datasets/OCPW::ocacs-2013-social-characteristics-for-elementary-school-districts/about
- **REST**: https://services.arcgis.com/UXmFoWC7yDHcDN5Q/arcgis/rest/services/OCACS_2013_Social_Characteristics_for_Elementary_School_Districts/FeatureServer
- **Metadata**: https://www.arcgis.com/sharing/rest/content/items/58b0b56bd0a64029b49f823a282126d8/info/metadata/metadata.xml?format=default&output=html
- **GeoService API**: https://services.arcgis.com/UXmFoWC7yDHcDN5Q/arcgis/rest/services/OCACS_2013_Social_Characteristics_for_Elementary_School_Districts/FeatureServer/1/query?outFields=*&where=1%3D1
- **GeoJSON API**: https://services.arcgis.com/UXmFoWC7yDHcDN5Q/arcgis/rest/services/OCACS_2013_Social_Characteristics_for_Elementary_School_Districts/FeatureServer/1/query?outFields=*&where=1%3D1&f=geojson

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2013.2.9. Secondary School Districts Social Characteristics

- **Name**: OCACS2013SDS
- **Title**: OCACS 2013 Secondary School Districts Selected Social Characteristics
- **Tags**: geodemographics, Orange County, California, US Census, ACS, American Community Survey, Social Characteristics, Secondary School Districts, households, relationship, marital status, Fertility, grandparents, school enrollment, educational attainment, veteran status, disability, residence, place of birth, citizenship, region of birth, language spoken, ancestry, computer use, internet use
- **Summary**: Key social characteristics of the 2013 American Community Survey (ACS), 5-year estimates for Secondary School Districts in Orange County, California.
- **Description**: US Census American Community Survey (ACS) 2013, 5-year estimates of the key social characteristics of Secondary School Districts geographic level in Orange County, California. The data contains 500 fields for the variable groups S01: Households by type (universe: total households, table X11, 17 fields); S02: Relationship (universe: population in households, table X9, 19 fields); S03: Marital status (universe: population 15 years and over, table X12, 13 fields); S04: Fertility (universe: women 15-50 years who had birth in the past 12 months, table X13, 11 fields); S05: Grandparents (universe: grandparents living or responsible for own grandchildren under 18 years, table X10, 18 fields); S06: School enrollment (universe: population 3 years old and over enrolled in school, table X14, 17 fields); S07: Educational attainment (universe: population 25 years and over, table X15, 25 fields); S08: Veteran status (universe: civilian population 18 years and over, table X21, 2 fields); S09: Disability status and type by sex and age (universe: total civilian non-institutionalized population, table X18, 77 fields); S10: Disability status by age and health insurance coverage (universe: civilian non-institutionalized population, table X18, 16 fields); S11: Residence 1 year ago (universe: population 1 year and over, table X7, 6 fields); S12: Place of birth (universe: total population, table X5, 27 fields); S13: Citizenship status by nativity in the US (universe: total population, table X5, 6 fields); S14: Year of entry (universe: population born outside the US, table X5, 21 fields); S15: World region of birth of foreign born population (universe: foreign born population, excluding population born at sea, table X5, 25 fields); S16: Language spoken in households (universe: total households, table X16, 6 fields); S17: Language spoken at home (universe: population 5 years and over, table X16, 67 fields); S18: Ancestry (universe: total population reporting ancestry, table X4, 114 fields), and; S19: Computers and internet use (universe: total population in households and total households, table X28, 13 fields). The US Census geodemographic data are based on the 2013 TigerLines across multiple geographies. The spatial geographies were merged with ACS data tables. See full documentation at the OCACS project github page (https://github.com/ktalexan/OCACS-Geodemographics).
- **Terms of Use**: Original datasets from US Census TigerLine Geography (https://www.census.gov/geo/maps-data/data/tiger-line.html), and American FactFinder (https://factfinder.census.gov/) for the selected tables of the American Community Survey (ACS, 2013). Linking and merging geographic with demographic tables along with final production of the merged spatial geodatabase and online datasets are performed by Orange County Public Works, OC Survey Geospatial Services, Dr. Kostas Alexandridis, GISP.
- **Map**: https://data-ocpw.opendata.arcgis.com/maps/ocacs-2013-social-characteristics-for-secondary-school-districts
- **Web**: https://data-ocpw.opendata.arcgis.com/datasets/OCPW::ocacs-2013-social-characteristics-for-secondary-school-districts/about
- **REST**: https://services.arcgis.com/UXmFoWC7yDHcDN5Q/arcgis/rest/services/OCACS_2013_Social_Characteristics_for_Secondary_School_Districts/FeatureServer
- **Metadata**: https://www.arcgis.com/sharing/rest/content/items/bff62c8aa8614a92b71de9d185914ce9/info/metadata/metadata.xml?format=default&output=html
- **GeoService API**: https://services.arcgis.com/UXmFoWC7yDHcDN5Q/arcgis/rest/services/OCACS_2013_Social_Characteristics_for_Secondary_School_Districts/FeatureServer/1/query?outFields=*&where=1%3D1
- **GeoJSON API**: https://services.arcgis.com/UXmFoWC7yDHcDN5Q/arcgis/rest/services/OCACS_2013_Social_Characteristics_for_Secondary_School_Districts/FeatureServer/1/query?outFields=*&where=1%3D1&f=geojson

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2013.2.10. Unified School Districts Social Characteristics

- **Name**: OCACS2013UDS
- **Title**: OCACS 2013 Unified School Districts Selected Social Characteristics
- **Tags**: geodemographics, Orange County, California, US Census, ACS, American Community Survey, Social Characteristics, Unified School Districts, households, relationship, marital status, Fertility, grandparents, school enrollment, educational attainment, veteran status, disability, residence, place of birth, citizenship, region of birth, language spoken, ancestry, computer use, internet use
- **Summary**: Key social characteristics of the 2013 American Community Survey (ACS), 5-year estimates for Unified School Districts in Orange County, California.
- **Description**: US Census American Community Survey (ACS) 2013, 5-year estimates of the key social characteristics of Unified School Districts geographic level in Orange County, California. The data contains 500 fields for the variable groups S01: Households by type (universe: total households, table X11, 17 fields); S02: Relationship (universe: population in households, table X9, 19 fields); S03: Marital status (universe: population 15 years and over, table X12, 13 fields); S04: Fertility (universe: women 15-50 years who had birth in the past 12 months, table X13, 11 fields); S05: Grandparents (universe: grandparents living or responsible for own grandchildren under 18 years, table X10, 18 fields); S06: School enrollment (universe: population 3 years old and over enrolled in school, table X14, 17 fields); S07: Educational attainment (universe: population 25 years and over, table X15, 25 fields); S08: Veteran status (universe: civilian population 18 years and over, table X21, 2 fields); S09: Disability status and type by sex and age (universe: total civilian non-institutionalized population, table X18, 77 fields); S10: Disability status by age and health insurance coverage (universe: civilian non-institutionalized population, table X18, 16 fields); S11: Residence 1 year ago (universe: population 1 year and over, table X7, 6 fields); S12: Place of birth (universe: total population, table X5, 27 fields); S13: Citizenship status by nativity in the US (universe: total population, table X5, 6 fields); S14: Year of entry (universe: population born outside the US, table X5, 21 fields); S15: World region of birth of foreign born population (universe: foreign born population, excluding population born at sea, table X5, 25 fields); S16: Language spoken in households (universe: total households, table X16, 6 fields); S17: Language spoken at home (universe: population 5 years and over, table X16, 67 fields); S18: Ancestry (universe: total population reporting ancestry, table X4, 114 fields), and; S19: Computers and internet use (universe: total population in households and total households, table X28, 13 fields). The US Census geodemographic data are based on the 2013 TigerLines across multiple geographies. The spatial geographies were merged with ACS data tables. See full documentation at the OCACS project github page (https://github.com/ktalexan/OCACS-Geodemographics).
- **Terms of Use**: Original datasets from US Census TigerLine Geography (https://www.census.gov/geo/maps-data/data/tiger-line.html), and American FactFinder (https://factfinder.census.gov/) for the selected tables of the American Community Survey (ACS, 2013). Linking and merging geographic with demographic tables along with final production of the merged spatial geodatabase and online datasets are performed by Orange County Public Works, OC Survey Geospatial Services, Dr. Kostas Alexandridis, GISP.
- **Map**: https://data-ocpw.opendata.arcgis.com/maps/ocacs-2013-social-characteristics-for-unified-school-districts
- **Web**: https://data-ocpw.opendata.arcgis.com/datasets/OCPW::ocacs-2013-social-characteristics-for-unified-school-districts/about
- **REST**: https://services.arcgis.com/UXmFoWC7yDHcDN5Q/arcgis/rest/services/OCACS_2013_Social_Characteristics_for_Unified_School_Districts/FeatureServer
- **Metadata**: https://www.arcgis.com/sharing/rest/content/items/98ddfdb42f8d4a1e8dc4b41bff8a002a/info/metadata/metadata.xml?format=default&output=html
- **GeoService API**: https://services.arcgis.com/UXmFoWC7yDHcDN5Q/arcgis/rest/services/OCACS_2013_Social_Characteristics_for_Unified_School_Districts/FeatureServer/1/query?outFields=*&where=1%3D1
- **GeoJSON API**: https://services.arcgis.com/UXmFoWC7yDHcDN5Q/arcgis/rest/services/OCACS_2013_Social_Characteristics_for_Unified_School_Districts/FeatureServer/1/query?outFields=*&where=1%3D1&f=geojson

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2013.2.11. Urban Areas Social Characteristics

- **Name**: OCACS2013UAS
- **Title**: OCACS 2013 Urban Areas Selected Social Characteristics
- **Tags**: geodemographics, Orange County, California, US Census, ACS, American Community Survey, Social Characteristics, Urban Areas, households, relationship, marital status, Fertility, grandparents, school enrollment, educational attainment, veteran status, disability, residence, place of birth, citizenship, region of birth, language spoken, ancestry, computer use, internet use
- **Summary**: Key social characteristics of the 2013 American Community Survey (ACS), 5-year estimates for Urban Areas in Orange County, California.
- **Description**: US Census American Community Survey (ACS) 2013, 5-year estimates of the key social characteristics of Urban Areas geographic level in Orange County, California. The data contains 500 fields for the variable groups S01: Households by type (universe: total households, table X11, 17 fields); S02: Relationship (universe: population in households, table X9, 19 fields); S03: Marital status (universe: population 15 years and over, table X12, 13 fields); S04: Fertility (universe: women 15-50 years who had birth in the past 12 months, table X13, 11 fields); S05: Grandparents (universe: grandparents living or responsible for own grandchildren under 18 years, table X10, 18 fields); S06: School enrollment (universe: population 3 years old and over enrolled in school, table X14, 17 fields); S07: Educational attainment (universe: population 25 years and over, table X15, 25 fields); S08: Veteran status (universe: civilian population 18 years and over, table X21, 2 fields); S09: Disability status and type by sex and age (universe: total civilian non-institutionalized population, table X18, 77 fields); S10: Disability status by age and health insurance coverage (universe: civilian non-institutionalized population, table X18, 16 fields); S11: Residence 1 year ago (universe: population 1 year and over, table X7, 6 fields); S12: Place of birth (universe: total population, table X5, 27 fields); S13: Citizenship status by nativity in the US (universe: total population, table X5, 6 fields); S14: Year of entry (universe: population born outside the US, table X5, 21 fields); S15: World region of birth of foreign born population (universe: foreign born population, excluding population born at sea, table X5, 25 fields); S16: Language spoken in households (universe: total households, table X16, 6 fields); S17: Language spoken at home (universe: population 5 years and over, table X16, 67 fields); S18: Ancestry (universe: total population reporting ancestry, table X4, 114 fields), and; S19: Computers and internet use (universe: total population in households and total households, table X28, 13 fields). The US Census geodemographic data are based on the 2013 TigerLines across multiple geographies. The spatial geographies were merged with ACS data tables. See full documentation at the OCACS project github page (https://github.com/ktalexan/OCACS-Geodemographics).
- **Terms of Use**: Original datasets from US Census TigerLine Geography (https://www.census.gov/geo/maps-data/data/tiger-line.html), and American FactFinder (https://factfinder.census.gov/) for the selected tables of the American Community Survey (ACS, 2013). Linking and merging geographic with demographic tables along with final production of the merged spatial geodatabase and online datasets are performed by Orange County Public Works, OC Survey Geospatial Services, Dr. Kostas Alexandridis, GISP.
- **Map**: https://data-ocpw.opendata.arcgis.com/maps/ocacs-2013-social-characteristics-for-urban-areas
- **Web**: https://data-ocpw.opendata.arcgis.com/datasets/OCPW::ocacs-2013-social-characteristics-for-urban-areas/about
- **REST**: https://services.arcgis.com/UXmFoWC7yDHcDN5Q/arcgis/rest/services/OCACS_2013_Social_Characteristics_for_Urban_Areas/FeatureServer
- **Metadata**: https://www.arcgis.com/sharing/rest/content/items/884592c81d91472da8755f67e70b353d/info/metadata/metadata.xml?format=default&output=html
- **GeoService API**: https://services.arcgis.com/UXmFoWC7yDHcDN5Q/arcgis/rest/services/OCACS_2013_Social_Characteristics_for_Urban_Areas/FeatureServer/1/query?outFields=*&where=1%3D1
- **GeoJSON API**: https://services.arcgis.com/UXmFoWC7yDHcDN5Q/arcgis/rest/services/OCACS_2013_Social_Characteristics_for_Urban_Areas/FeatureServer/1/query?outFields=*&where=1%3D1&f=geojson

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2013.2.12. Public Use Microdata Areas Social Characteristics

- **Name**: OCACS2013PUS
- **Title**: OCACS 2013 Public Use Microdata Areas Selected Social Characteristics
- **Tags**: geodemographics, Orange County, California, US Census, ACS, American Community Survey, Social Characteristics, Public Use Microdata Areas, PUMA, households, relationship, marital status, Fertility, grandparents, school enrollment, educational attainment, veteran status, disability, residence, place of birth, citizenship, region of birth, language spoken, ancestry, computer use, internet use
- **Summary**: Key social characteristics of the 2013 American Community Survey (ACS), 5-year estimates for Public Use Microdata Areas (PUMA) in Orange County, California.
- **Description**: US Census American Community Survey (ACS) 2013, 5-year estimates of the key social characteristics of Public Use Microdata Areas (PUMA) geographic level in Orange County, California. The data contains 500 fields for the variable groups S01: Households by type (universe: total households, table X11, 17 fields); S02: Relationship (universe: population in households, table X9, 19 fields); S03: Marital status (universe: population 15 years and over, table X12, 13 fields); S04: Fertility (universe: women 15-50 years who had birth in the past 12 months, table X13, 11 fields); S05: Grandparents (universe: grandparents living or responsible for own grandchildren under 18 years, table X10, 18 fields); S06: School enrollment (universe: population 3 years old and over enrolled in school, table X14, 17 fields); S07: Educational attainment (universe: population 25 years and over, table X15, 25 fields); S08: Veteran status (universe: civilian population 18 years and over, table X21, 2 fields); S09: Disability status and type by sex and age (universe: total civilian non-institutionalized population, table X18, 77 fields); S10: Disability status by age and health insurance coverage (universe: civilian non-institutionalized population, table X18, 16 fields); S11: Residence 1 year ago (universe: population 1 year and over, table X7, 6 fields); S12: Place of birth (universe: total population, table X5, 27 fields); S13: Citizenship status by nativity in the US (universe: total population, table X5, 6 fields); S14: Year of entry (universe: population born outside the US, table X5, 21 fields); S15: World region of birth of foreign born population (universe: foreign born population, excluding population born at sea, table X5, 25 fields); S16: Language spoken in households (universe: total households, table X16, 6 fields); S17: Language spoken at home (universe: population 5 years and over, table X16, 67 fields); S18: Ancestry (universe: total population reporting ancestry, table X4, 114 fields), and; S19: Computers and internet use (universe: total population in households and total households, table X28, 13 fields). The US Census geodemographic data are based on the 2013 TigerLines across multiple geographies. The spatial geographies were merged with ACS data tables. See full documentation at the OCACS project github page (https://github.com/ktalexan/OCACS-Geodemographics).
- **Terms of Use**: Original datasets from US Census TigerLine Geography (https://www.census.gov/geo/maps-data/data/tiger-line.html), and American FactFinder (https://factfinder.census.gov/) for the selected tables of the American Community Survey (ACS, 2013). Linking and merging geographic with demographic tables along with final production of the merged spatial geodatabase and online datasets are performed by Orange County Public Works, OC Survey Geospatial Services, Dr. Kostas Alexandridis, GISP.
- **Map**: https://data-ocpw.opendata.arcgis.com/maps/ocacs-2013-social-characteristics-for-public-use-microdata-areas
- **Web**: https://data-ocpw.opendata.arcgis.com/datasets/OCPW::ocacs-2013-social-characteristics-for-public-use-microdata-areas/about
- **REST**: https://services.arcgis.com/UXmFoWC7yDHcDN5Q/arcgis/rest/services/OCACS_2013_Social_Characteristics_for_Public_Use_Microdata_Areas/FeatureServer
- **Metadata**: https://www.arcgis.com/sharing/rest/content/items/c2098f9e120f418494701d60e1a7da95/info/metadata/metadata.xml?format=default&output=html
- **GeoService API**: https://services.arcgis.com/UXmFoWC7yDHcDN5Q/arcgis/rest/services/OCACS_2013_Social_Characteristics_for_Public_Use_Microdata_Areas/FeatureServer/1/query?outFields=*&where=1%3D1
- **GeoJSON API**: https://services.arcgis.com/UXmFoWC7yDHcDN5Q/arcgis/rest/services/OCACS_2013_Social_Characteristics_for_Public_Use_Microdata_Areas/FeatureServer/1/query?outFields=*&where=1%3D1&f=geojson

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2013.2.13. Block Groups Social Characteristics

- **Name**: OCACS2013BGS
- **Title**: OCACS 2013 Block Groups Selected Social Characteristics
- **Tags**: geodemographics, Orange County, California, US Census, ACS, American Community Survey, Social Characteristics, Block Groups, households, relationship, marital status, Fertility, grandparents, school enrollment, educational attainment, veteran status, disability, residence, place of birth, citizenship, region of birth, language spoken, ancestry, computer use, internet use
- **Summary**: Key social characteristics of the 2013 American Community Survey (ACS), 5-year estimates for Block Groups in Orange County, California.
- **Description**: US Census American Community Survey (ACS) 2013, 5-year estimates of the key social characteristics of Block Groups geographic level in Orange County, California. The data contains 500 fields for the variable groups S01: Households by type (universe: total households, table X11, 17 fields); S02: Relationship (universe: population in households, table X9, 19 fields); S03: Marital status (universe: population 15 years and over, table X12, 13 fields); S04: Fertility (universe: women 15-50 years who had birth in the past 12 months, table X13, 11 fields); S05: Grandparents (universe: grandparents living or responsible for own grandchildren under 18 years, table X10, 18 fields); S06: School enrollment (universe: population 3 years old and over enrolled in school, table X14, 17 fields); S07: Educational attainment (universe: population 25 years and over, table X15, 25 fields); S08: Veteran status (universe: civilian population 18 years and over, table X21, 2 fields); S09: Disability status and type by sex and age (universe: total civilian non-institutionalized population, table X18, 77 fields); S10: Disability status by age and health insurance coverage (universe: civilian non-institutionalized population, table X18, 16 fields); S11: Residence 1 year ago (universe: population 1 year and over, table X7, 6 fields); S12: Place of birth (universe: total population, table X5, 27 fields); S13: Citizenship status by nativity in the US (universe: total population, table X5, 6 fields); S14: Year of entry (universe: population born outside the US, table X5, 21 fields); S15: World region of birth of foreign born population (universe: foreign born population, excluding population born at sea, table X5, 25 fields); S16: Language spoken in households (universe: total households, table X16, 6 fields); S17: Language spoken at home (universe: population 5 years and over, table X16, 67 fields); S18: Ancestry (universe: total population reporting ancestry, table X4, 114 fields), and; S19: Computers and internet use (universe: total population in households and total households, table X28, 13 fields). The US Census geodemographic data are based on the 2013 TigerLines across multiple geographies. The spatial geographies were merged with ACS data tables. See full documentation at the OCACS project github page (https://github.com/ktalexan/OCACS-Geodemographics).
- **Terms of Use**: Original datasets from US Census TigerLine Geography (https://www.census.gov/geo/maps-data/data/tiger-line.html), and American FactFinder (https://factfinder.census.gov/) for the selected tables of the American Community Survey (ACS, 2013). Linking and merging geographic with demographic tables along with final production of the merged spatial geodatabase and online datasets are performed by Orange County Public Works, OC Survey Geospatial Services, Dr. Kostas Alexandridis, GISP.
- **Map**: https://data-ocpw.opendata.arcgis.com/maps/ocacs-2013-social-characteristics-for-block-groups
- **Web**: https://data-ocpw.opendata.arcgis.com/datasets/OCPW::ocacs-2013-social-characteristics-for-block-groups/about
- **REST**: https://services.arcgis.com/UXmFoWC7yDHcDN5Q/arcgis/rest/services/OCACS_2013_Social_Characteristics_for_Block_Groups/FeatureServer
- **Metadata**: https://www.arcgis.com/sharing/rest/content/items/b6bf717a154f45f6b6a07875e720997e/info/metadata/metadata.xml?format=default&output=html
- **GeoService API**: https://services.arcgis.com/UXmFoWC7yDHcDN5Q/arcgis/rest/services/OCACS_2013_Social_Characteristics_for_Block_Groups/FeatureServer/1/query?outFields=*&where=1%3D1
- **GeoJSON API**: https://services.arcgis.com/UXmFoWC7yDHcDN5Q/arcgis/rest/services/OCACS_2013_Social_Characteristics_for_Block_Groups/FeatureServer/1/query?outFields=*&where=1%3D1&f=geojson

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2013.2.14. Census Tracts Social Characteristics

- **Name**: OCACS2013TRS
- **Title**: OCACS 2013 Census Tracts Selected Social Characteristics
- **Tags**: geodemographics, Orange County, California, US Census, ACS, American Community Survey, Social Characteristics, Census Tracts, households, relationship, marital status, Fertility, grandparents, school enrollment, educational attainment, veteran status, disability, residence, place of birth, citizenship, region of birth, language spoken, ancestry, computer use, internet use
- **Summary**:  Key social characteristics of the 2013 American Community Survey (ACS), 5-year estimates for Census Tracts in Orange County, California.
- **Description**: US Census American Community Survey (ACS) 2013, 5-year estimates of the key social characteristics of Census Tract geographic level in Orange County, California. The data contains 500 fields for the variable groups S01: Households by type (universe: total households, table X11, 17 fields); S02: Relationship (universe: population in households, table X9, 19 fields); S03: Marital status (universe: population 15 years and over, table X12, 13 fields); S04: Fertility (universe: women 15-50 years who had birth in the past 12 months, table X13, 11 fields); S05: Grandparents (universe: grandparents living or responsible for own grandchildren under 18 years, table X10, 18 fields); S06: School enrollment (universe: population 3 years old and over enrolled in school, table X14, 17 fields); S07: Educational attainment (universe: population 25 years and over, table X15, 25 fields); S08: Veteran status (universe: civilian population 18 years and over, table X21, 2 fields); S09: Disability status and type by sex and age (universe: total civilian non-institutionalized population, table X18, 77 fields); S10: Disability status by age and health insurance coverage (universe: civilian non-institutionalized population, table X18, 16 fields); S11: Residence 1 year ago (universe: population 1 year and over, table X7, 6 fields); S12: Place of birth (universe: total population, table X5, 27 fields); S13: Citizenship status by nativity in the US (universe: total population, table X5, 6 fields); S14: Year of entry (universe: population born outside the US, table X5, 21 fields); S15: World region of birth of foreign born population (universe: foreign born population, excluding population born at sea, table X5, 25 fields); S16: Language spoken in households (universe: total households, table X16, 6 fields); S17: Language spoken at home (universe: population 5 years and over, table X16, 67 fields); S18: Ancestry (universe: total population reporting ancestry, table X4, 114 fields), and; S19: Computers and internet use (universe: total population in households and total households, table X28, 13 fields). The US Census geodemographic data are based on the 2013 TigerLines across multiple geographies. The spatial geographies were merged with ACS data tables. See full documentation at the OCACS project github page (https://github.com/ktalexan/OCACS-Geodemographics).
- **Terms of Use**: Original datasets from US Census TigerLine Geography (https://www.census.gov/geo/maps-data/data/tiger-line.html), and American FactFinder (https://factfinder.census.gov/) for the selected tables of the American Community Survey (ACS, 2013). Linking and merging geographic with demographic tables along with final production of the merged spatial geodatabase and online datasets are performed by Orange County Public Works, OC Survey Geospatial Services, Dr. Kostas Alexandridis, GISP.
- **Map**: https://data-ocpw.opendata.arcgis.com/maps/ocacs-2013-social-characteristics-for-census-tracts
- **Web**: https://data-ocpw.opendata.arcgis.com/datasets/OCPW::ocacs-2013-social-characteristics-for-census-tracts/about
- **REST**: https://services.arcgis.com/UXmFoWC7yDHcDN5Q/arcgis/rest/services/OCACS_2013_Social_Characteristics_for_Census_Tracts/FeatureServer
- **Metadata**: https://www.arcgis.com/sharing/rest/content/items/a4e704cfbed04190973cb29b94c247e3/info/metadata/metadata.xml?format=default&output=html
- **GeoService API**: https://services.arcgis.com/UXmFoWC7yDHcDN5Q/arcgis/rest/services/OCACS_2013_Social_Characteristics_for_Census_Tracts/FeatureServer/1/query?outFields=*&where=1%3D1
- **GeoJSON API**: https://services.arcgis.com/UXmFoWC7yDHcDN5Q/arcgis/rest/services/OCACS_2013_Social_Characteristics_for_Census_Tracts/FeatureServer/1/query?outFields=*&where=1%3D1&f=geojson

[<div align="right"><< Back to Contents</div>](#contents)

---
### 2013.3. Economic Characteristics
---
> #### 2013.3.1. County Level Economic Characteristics

- **Name**: OCACS2013COE
- **Title**: OCACS 2013 County Level Selected Economic Characteristics
- **Tags**: geodemographics, Orange County, California, US Census, ACS, American Community Survey, Economic Characteristics, Orange County, employment status, work status, worker, commuting, travel time, vehicles, transportation, occupation, industry, class of worker, income, earnings, health insurance, poverty
- **Summary**: Key economic characteristics of the 2013 American Community Survey (ACS), 5-year estimates in Orange County, California. 
- **Description**: US Census American Community Survey (ACS) 2013, 5-year estimates of the key economic characteristics in Orange County, California. The data contains 397 fields for the variable groups E01: Employment status (universe: population 16 years and over, table X23, 7 fields); E02: Work status by age of worker (universe: population 16 years and over, table X23, 36 fields); E03: Commuting to work (universe: workers 16 years and over, table X8, 8 fields); E04: Travel time to work (universe: workers 16 years and over who did not work at home, table X8, 14 fields); E05: Number of vehicles available for workers (universe: workers 16 years and over in households, table X8, 8 fields); E06: Median age by means of transportation to work (universe: median age, workers 16 years and over, table X8, 7 fields); E07: Means of transportation to work by race (universe: workers 16 years and over, table X8, 64 fields); E08: Occupation (universe: civilian employed population 16 years and over, table X24, 53 fields); E09: Industry (universe: civilian employed population 16 years and over, table X24, 43 fields); E10: Class of worker (universe: civilian employed population 16 years and over, table X24, 19 fields); E11: Household income and earnings in the past 12 months (universe: total households, table X19, 37 fields); E12: Income and earnings in dollars (universe: inflation-adjusted dollars, tables X19-X20, 31 fields); E13: Family income in dollars (universe: total families, table X19, 17 fields); E14: Health insurance coverage (universe: total families, table X19, 17 fields); E15: Ratio of income to Poverty level (universe: total population for whom Poverty level is determined, table X17,  8 fields); E16: Poverty in population in the past 12 months (universe: total population for whom Poverty level is determined, table X17, 7 fields); E17: Poverty in households in the past 12 months (universe: total households, table X17, 9 fields); E18: Percentage of families and people whose income in the past 12 months is below the poverty level (universe: families, population, table X17, 8 fields), and; X19: Poverty and income deficit (dollars) in the past 12 months for families (universe: families with income below Poverty level in the past 12 months, table X17, 4 fields). The US Census geodemographic data are based on the 2013 TigerLines across multiple geographies. The spatial geographies were merged with ACS data tables. See full documentation at the OCACS project github page (https://github.com/ktalexan/OCACS-Geodemographics).
- **Terms of Use**: Original datasets from US Census TigerLine Geography (https://www.census.gov/geo/maps-data/data/tiger-line.html), and American FactFinder (https://factfinder.census.gov/) for the selected tables of the American Community Survey (ACS, 2013). Linking and merging geographic with demographic tables along with final production of the merged spatial geodatabase and online datasets are performed by Orange County Public Works, OC Survey Geospatial Services, Dr. Kostas Alexandridis, GISP.
- **Map**: https://data-ocpw.opendata.arcgis.com/maps/ocacs-2013-economic-characteristics-for-orange-county
- **Web**: https://data-ocpw.opendata.arcgis.com/datasets/OCPW::ocacs-2013-economic-characteristics-for-orange-county/about
- **REST**: https://services.arcgis.com/UXmFoWC7yDHcDN5Q/arcgis/rest/services/OCACS_2013_Economic_Characteristics_for_Orange_County/FeatureServer
- **Metadata**: https://www.arcgis.com/sharing/rest/content/items/c63a202c8a594f2184024b38e8acbb3a/info/metadata/metadata.xml?format=default&output=html
- **GeoService API**: https://services.arcgis.com/UXmFoWC7yDHcDN5Q/arcgis/rest/services/OCACS_2013_Economic_Characteristics_for_Orange_County/FeatureServer/1/query?outFields=*&where=1%3D1
- **GeoJSON API**: https://services.arcgis.com/UXmFoWC7yDHcDN5Q/arcgis/rest/services/OCACS_2013_Economic_Characteristics_for_Orange_County/FeatureServer/1/query?outFields=*&where=1%3D1&f=geojson

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2013.3.2. County Subdivision Economic Characteristics

- **Name**: OCACS2013CSE
- **Title**: OCACS 2013 County Subdivisions Selected Economic Characteristics
- **Tags**: geodemographics, Orange County, California, US Census, ACS, American Community Survey, Economic Characteristics, County Subdivisions, employment status, work status, worker, commuting, travel time, vehicles, transportation, occupation, industry, class of worker, income, earnings, health insurance, poverty
- **Summary**: Key economic characteristics of the 2013 American Community Survey (ACS), 5-year estimates for County Subdivisions in Orange County, California. 
- **Description**: US Census American Community Survey (ACS) 2013, 5-year estimates of the key economic characteristics of County Subdivisions geographic level in Orange County, California. The data contains 397 fields for the variable groups E01: Employment status (universe: population 16 years and over, table X23, 7 fields); E02: Work status by age of worker (universe: population 16 years and over, table X23, 36 fields); E03: Commuting to work (universe: workers 16 years and over, table X8, 8 fields); E04: Travel time to work (universe: workers 16 years and over who did not work at home, table X8, 14 fields); E05: Number of vehicles available for workers (universe: workers 16 years and over in households, table X8, 8 fields); E06: Median age by means of transportation to work (universe: median age, workers 16 years and over, table X8, 7 fields); E07: Means of transportation to work by race (universe: workers 16 years and over, table X8, 64 fields); E08: Occupation (universe: civilian employed population 16 years and over, table X24, 53 fields); E09: Industry (universe: civilian employed population 16 years and over, table X24, 43 fields); E10: Class of worker (universe: civilian employed population 16 years and over, table X24, 19 fields); E11: Household income and earnings in the past 12 months (universe: total households, table X19, 37 fields); E12: Income and earnings in dollars (universe: inflation-adjusted dollars, tables X19-X20, 31 fields); E13: Family income in dollars (universe: total families, table X19, 17 fields); E14: Health insurance coverage (universe: total families, table X19, 17 fields); E15: Ratio of income to Poverty level (universe: total population for whom Poverty level is determined, table X17,  8 fields); E16: Poverty in population in the past 12 months (universe: total population for whom Poverty level is determined, table X17, 7 fields); E17: Poverty in households in the past 12 months (universe: total households, table X17, 9 fields); E18: Percentage of families and people whose income in the past 12 months is below the poverty level (universe: families, population, table X17, 8 fields), and; X19: Poverty and income deficit (dollars) in the past 12 months for families (universe: families with income below Poverty level in the past 12 months, table X17, 4 fields). The US Census geodemographic data are based on the 2013 TigerLines across multiple geographies. The spatial geographies were merged with ACS data tables. See full documentation at the OCACS project github page (https://github.com/ktalexan/OCACS-Geodemographics).
- **Terms of Use**: Original datasets from US Census TigerLine Geography (https://www.census.gov/geo/maps-data/data/tiger-line.html), and American FactFinder (https://factfinder.census.gov/) for the selected tables of the American Community Survey (ACS, 2013). Linking and merging geographic with demographic tables along with final production of the merged spatial geodatabase and online datasets are performed by Orange County Public Works, OC Survey Geospatial Services, Dr. Kostas Alexandridis, GISP.
- **Map**: https://data-ocpw.opendata.arcgis.com/maps/ocacs-2013-economic-characteristics-for-county-subdivisions
- **Web**: https://data-ocpw.opendata.arcgis.com/datasets/OCPW::ocacs-2013-economic-characteristics-for-county-subdivisions/about
- **REST**: https://services.arcgis.com/UXmFoWC7yDHcDN5Q/arcgis/rest/services/OCACS_2013_Economic_Characteristics_for_County_Subdivisions/FeatureServer
- **Metadata**: https://www.arcgis.com/sharing/rest/content/items/b947ce3ea04942938376a8c26b721a8f/info/metadata/metadata.xml?format=default&output=html
- **GeoService API**: https://services.arcgis.com/UXmFoWC7yDHcDN5Q/arcgis/rest/services/OCACS_2013_Economic_Characteristics_for_County_Subdivisions/FeatureServer/1/query?outFields=*&where=1%3D1
- **GeoJSON API**: https://services.arcgis.com/UXmFoWC7yDHcDN5Q/arcgis/rest/services/OCACS_2013_Economic_Characteristics_for_County_Subdivisions/FeatureServer/1/query?outFields=*&where=1%3D1&f=geojson

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2013.3.3. Cities/Places Economic Characteristics

- **Name**: OCACS2013PLE
- **Title**: OCACS 2013 Cities Selected Economic Characteristics
- **Tags**: geodemographics, Orange County, California, US Census, ACS, American Community Survey, Economic Characteristics, Cities, Places, employment status, work status, worker, commuting, travel time, vehicles, transportation, occupation, industry, class of worker, income, earnings, health insurance, poverty
- **Summary**: Key economic characteristics of the 2013 American Community Survey (ACS), 5-year estimates for Cities/Places in Orange County, California. 
- **Description**: US Census American Community Survey (ACS) 2013, 5-year estimates of the key economic characteristics of Cities/Places geographic level in Orange County, California. The data contains 397 fields for the variable groups E01: Employment status (universe: population 16 years and over, table X23, 7 fields); E02: Work status by age of worker (universe: population 16 years and over, table X23, 36 fields); E03: Commuting to work (universe: workers 16 years and over, table X8, 8 fields); E04: Travel time to work (universe: workers 16 years and over who did not work at home, table X8, 14 fields); E05: Number of vehicles available for workers (universe: workers 16 years and over in households, table X8, 8 fields); E06: Median age by means of transportation to work (universe: median age, workers 16 years and over, table X8, 7 fields); E07: Means of transportation to work by race (universe: workers 16 years and over, table X8, 64 fields); E08: Occupation (universe: civilian employed population 16 years and over, table X24, 53 fields); E09: Industry (universe: civilian employed population 16 years and over, table X24, 43 fields); E10: Class of worker (universe: civilian employed population 16 years and over, table X24, 19 fields); E11: Household income and earnings in the past 12 months (universe: total households, table X19, 37 fields); E12: Income and earnings in dollars (universe: inflation-adjusted dollars, tables X19-X20, 31 fields); E13: Family income in dollars (universe: total families, table X19, 17 fields); E14: Health insurance coverage (universe: total families, table X19, 17 fields); E15: Ratio of income to Poverty level (universe: total population for whom Poverty level is determined, table X17,  8 fields); E16: Poverty in population in the past 12 months (universe: total population for whom Poverty level is determined, table X17, 7 fields); E17: Poverty in households in the past 12 months (universe: total households, table X17, 9 fields); E18: Percentage of families and people whose income in the past 12 months is below the poverty level (universe: families, population, table X17, 8 fields), and; X19: Poverty and income deficit (dollars) in the past 12 months for families (universe: families with income below Poverty level in the past 12 months, table X17, 4 fields). The US Census geodemographic data are based on the 2013 TigerLines across multiple geographies. The spatial geographies were merged with ACS data tables. See full documentation at the OCACS project github page (https://github.com/ktalexan/OCACS-Geodemographics).
- **Terms of Use**: Original datasets from US Census TigerLine Geography (https://www.census.gov/geo/maps-data/data/tiger-line.html), and American FactFinder (https://factfinder.census.gov/) for the selected tables of the American Community Survey (ACS, 2013). Linking and merging geographic with demographic tables along with final production of the merged spatial geodatabase and online datasets are performed by Orange County Public Works, OC Survey Geospatial Services, Dr. Kostas Alexandridis, GISP.
- **Map**: https://data-ocpw.opendata.arcgis.com/maps/ocacs-2013-economic-characteristics-for-cities
- **Web**: https://data-ocpw.opendata.arcgis.com/datasets/OCPW::ocacs-2013-economic-characteristics-for-cities/about
- **REST**: https://services.arcgis.com/UXmFoWC7yDHcDN5Q/arcgis/rest/services/OCACS_2013_Economic_Characteristics_for_Cities/FeatureServer
- **Metadata**: https://www.arcgis.com/sharing/rest/content/items/15c0bd4bb19a4b518bced674721f6937/info/metadata/metadata.xml?format=default&output=html 
- **GeoService API**: https://services.arcgis.com/UXmFoWC7yDHcDN5Q/arcgis/rest/services/OCACS_2013_Economic_Characteristics_for_Cities/FeatureServer/1/query?outFields=*&where=1%3D1
- **GeoJSON API**: https://services.arcgis.com/UXmFoWC7yDHcDN5Q/arcgis/rest/services/OCACS_2013_Economic_Characteristics_for_Cities/FeatureServer/1/query?outFields=*&where=1%3D1&f=geojson

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2013.3.4. ZIP Code Tabulation Areas Economic Characteristics

- **Name**: OCACS2013ZCE
- **Title**: OCACS 2013 ZIP Code Tabulation Areas Selected Economic Characteristics
- **Tags**: geodemographics, Orange County, California, US Census, ACS, American Community Survey, Economic Characteristics, ZIP Code, employment status, work status, worker, commuting, travel time, vehicles, transportation, occupation, industry, class of worker, income, earnings, health insurance, poverty
- **Summary**: Key economic characteristics of the 2013 American Community Survey (ACS), 5-year estimates for ZIP Code Tabulation Areas in Orange County, California. 
- **Description**: US Census American Community Survey (ACS) 2013, 5-year estimates of the key economic characteristics of ZIP Code Tabulation Areas geographic level in Orange County, California. The data contains 397 fields for the variable groups E01: Employment status (universe: population 16 years and over, table X23, 7 fields); E02: Work status by age of worker (universe: population 16 years and over, table X23, 36 fields); E03: Commuting to work (universe: workers 16 years and over, table X8, 8 fields); E04: Travel time to work (universe: workers 16 years and over who did not work at home, table X8, 14 fields); E05: Number of vehicles available for workers (universe: workers 16 years and over in households, table X8, 8 fields); E06: Median age by means of transportation to work (universe: median age, workers 16 years and over, table X8, 7 fields); E07: Means of transportation to work by race (universe: workers 16 years and over, table X8, 64 fields); E08: Occupation (universe: civilian employed population 16 years and over, table X24, 53 fields); E09: Industry (universe: civilian employed population 16 years and over, table X24, 43 fields); E10: Class of worker (universe: civilian employed population 16 years and over, table X24, 19 fields); E11: Household income and earnings in the past 12 months (universe: total households, table X19, 37 fields); E12: Income and earnings in dollars (universe: inflation-adjusted dollars, tables X19-X20, 31 fields); E13: Family income in dollars (universe: total families, table X19, 17 fields); E14: Health insurance coverage (universe: total families, table X19, 17 fields); E15: Ratio of income to Poverty level (universe: total population for whom Poverty level is determined, table X17,  8 fields); E16: Poverty in population in the past 12 months (universe: total population for whom Poverty level is determined, table X17, 7 fields); E17: Poverty in households in the past 12 months (universe: total households, table X17, 9 fields); E18: Percentage of families and people whose income in the past 12 months is below the poverty level (universe: families, population, table X17, 8 fields), and; X19: Poverty and income deficit (dollars) in the past 12 months for families (universe: families with income below Poverty level in the past 12 months, table X17, 4 fields). The US Census geodemographic data are based on the 2013 TigerLines across multiple geographies. The spatial geographies were merged with ACS data tables. See full documentation at the OCACS project github page (https://github.com/ktalexan/OCACS-Geodemographics).
- **Terms of Use**: Original datasets from US Census TigerLine Geography (https://www.census.gov/geo/maps-data/data/tiger-line.html), and American FactFinder (https://factfinder.census.gov/) for the selected tables of the American Community Survey (ACS, 2013). Linking and merging geographic with demographic tables along with final production of the merged spatial geodatabase and online datasets are performed by Orange County Public Works, OC Survey Geospatial Services, Dr. Kostas Alexandridis, GISP.
- **Map**: https://data-ocpw.opendata.arcgis.com/maps/ocacs-2013-economic-characteristics-for-zip-code-tabulation-areas
- **Web**: https://data-ocpw.opendata.arcgis.com/datasets/OCPW::ocacs-2013-economic-characteristics-for-zip-code-tabulation-areas/about
- **REST**: https://services.arcgis.com/UXmFoWC7yDHcDN5Q/arcgis/rest/services/OCACS_2013_Economic_Characteristics_for_ZIP_Code_Tabulation_Areas/FeatureServer
- **Metadata**: https://www.arcgis.com/sharing/rest/content/items/67be7bfb95944292a2200b327b23817c/info/metadata/metadata.xml?format=default&output=html
- **GeoService API**: https://services.arcgis.com/UXmFoWC7yDHcDN5Q/arcgis/rest/services/OCACS_2013_Economic_Characteristics_for_ZIP_Code_Tabulation_Areas/FeatureServer/1/query?outFields=*&where=1%3D1
- **GeoJSON API**: https://services.arcgis.com/UXmFoWC7yDHcDN5Q/arcgis/rest/services/OCACS_2013_Economic_Characteristics_for_ZIP_Code_Tabulation_Areas/FeatureServer/1/query?outFields=*&where=1%3D1&f=geojson

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2013.3.5. Congressional Districts Economic Characteristics

- **Name**: OCACS2013CDE
- **Title**: OCACS 2013 Congressional Districts Selected Economic Characteristics
- **Tags**: geodemographics, Orange County, California, US Census, ACS, American Community Survey, Economic Characteristics, Congressional Districts, 115th US Congress, employment status, work status, worker, commuting, travel time, vehicles, transportation, occupation, industry, class of worker, income, earnings, health insurance, poverty
- **Summary**: Key economic characteristics of the 2013 American Community Survey (ACS), 5-year estimates for Congressional Districts (115th US Congress) in Orange County, California. 
- **Description**: US Census American Community Survey (ACS) 2013, 5-year estimates of the key economic characteristics of Congressional Districts (115th US Congress) geographic level in Orange County, California. The data contains 397 fields for the variable groups E01: Employment status (universe: population 16 years and over, table X23, 7 fields); E02: Work status by age of worker (universe: population 16 years and over, table X23, 36 fields); E03: Commuting to work (universe: workers 16 years and over, table X8, 8 fields); E04: Travel time to work (universe: workers 16 years and over who did not work at home, table X8, 14 fields); E05: Number of vehicles available for workers (universe: workers 16 years and over in households, table X8, 8 fields); E06: Median age by means of transportation to work (universe: median age, workers 16 years and over, table X8, 7 fields); E07: Means of transportation to work by race (universe: workers 16 years and over, table X8, 64 fields); E08: Occupation (universe: civilian employed population 16 years and over, table X24, 53 fields); E09: Industry (universe: civilian employed population 16 years and over, table X24, 43 fields); E10: Class of worker (universe: civilian employed population 16 years and over, table X24, 19 fields); E11: Household income and earnings in the past 12 months (universe: total households, table X19, 37 fields); E12: Income and earnings in dollars (universe: inflation-adjusted dollars, tables X19-X20, 31 fields); E13: Family income in dollars (universe: total families, table X19, 17 fields); E14: Health insurance coverage (universe: total families, table X19, 17 fields); E15: Ratio of income to Poverty level (universe: total population for whom Poverty level is determined, table X17,  8 fields); E16: Poverty in population in the past 12 months (universe: total population for whom Poverty level is determined, table X17, 7 fields); E17: Poverty in households in the past 12 months (universe: total households, table X17, 9 fields); E18: Percentage of families and people whose income in the past 12 months is below the poverty level (universe: families, population, table X17, 8 fields), and; X19: Poverty and income deficit (dollars) in the past 12 months for families (universe: families with income below Poverty level in the past 12 months, table X17, 4 fields). The US Census geodemographic data are based on the 2013 TigerLines across multiple geographies. The spatial geographies were merged with ACS data tables. See full documentation at the OCACS project github page (https://github.com/ktalexan/OCACS-Geodemographics).
- **Terms of Use**: Original datasets from US Census TigerLine Geography (https://www.census.gov/geo/maps-data/data/tiger-line.html), and American FactFinder (https://factfinder.census.gov/) for the selected tables of the American Community Survey (ACS, 2013). Linking and merging geographic with demographic tables along with final production of the merged spatial geodatabase and online datasets are performed by Orange County Public Works, OC Survey Geospatial Services, Dr. Kostas Alexandridis, GISP.
- **Map**: https://data-ocpw.opendata.arcgis.com/maps/ocacs-2013-economic-characteristics-for-congressional-districts-of-the-113th-us-congress
- **Web**: https://data-ocpw.opendata.arcgis.com/datasets/OCPW::ocacs-2013-economic-characteristics-for-congressional-districts-of-the-113th-us-congress/about
- **REST**: https://services.arcgis.com/UXmFoWC7yDHcDN5Q/arcgis/rest/services/OCACS_2013_Economic_Characteristics_for_Congressional_Districts_of_the_113th_US_Congress/FeatureServer
- **Metadata**: https://www.arcgis.com/sharing/rest/content/items/08d7f2ce0fe54fef8c58cfc9e5f40d05/info/metadata/metadata.xml?format=default&output=html
- **GeoService API**: https://services.arcgis.com/UXmFoWC7yDHcDN5Q/arcgis/rest/services/OCACS_2013_Economic_Characteristics_for_Congressional_Districts_of_the_113th_US_Congress/FeatureServer/1/query?outFields=*&where=1%3D1
- **GeoJSON API**: https://services.arcgis.com/UXmFoWC7yDHcDN5Q/arcgis/rest/services/OCACS_2013_Economic_Characteristics_for_Congressional_Districts_of_the_113th_US_Congress/FeatureServer/1/query?outFields=*&where=1%3D1&f=geojson

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2013.3.6. State Assembly Legislative Districts Economic Characteristics

- **Name**: OCACS2013LLE
- **Title**: OCACS 2013 State Assembly Legislative Districts Selected Economic Characteristics
- **Tags**: geodemographics, Orange County, California, US Census, ACS, American Community Survey, Economic Characteristics, State Assembly, Legislative Districts, employment status, work status, worker, commuting, travel time, vehicles, transportation, occupation, industry, class of worker, income, earnings, health insurance, poverty
- **Summary**: Key economic characteristics of the 2013 American Community Survey (ACS), 5-year estimates for State Assembly Legislative Districts (Lower) in Orange County, California. 
- **Description**: US Census American Community Survey (ACS) 2013, 5-year estimates of the key economic characteristics of State Assembly Legislative Districts (Lower) geographic level in Orange County, California. The data contains 397 fields for the variable groups E01: Employment status (universe: population 16 years and over, table X23, 7 fields); E02: Work status by age of worker (universe: population 16 years and over, table X23, 36 fields); E03: Commuting to work (universe: workers 16 years and over, table X8, 8 fields); E04: Travel time to work (universe: workers 16 years and over who did not work at home, table X8, 14 fields); E05: Number of vehicles available for workers (universe: workers 16 years and over in households, table X8, 8 fields); E06: Median age by means of transportation to work (universe: median age, workers 16 years and over, table X8, 7 fields); E07: Means of transportation to work by race (universe: workers 16 years and over, table X8, 64 fields); E08: Occupation (universe: civilian employed population 16 years and over, table X24, 53 fields); E09: Industry (universe: civilian employed population 16 years and over, table X24, 43 fields); E10: Class of worker (universe: civilian employed population 16 years and over, table X24, 19 fields); E11: Household income and earnings in the past 12 months (universe: total households, table X19, 37 fields); E12: Income and earnings in dollars (universe: inflation-adjusted dollars, tables X19-X20, 31 fields); E13: Family income in dollars (universe: total families, table X19, 17 fields); E14: Health insurance coverage (universe: total families, table X19, 17 fields); E15: Ratio of income to Poverty level (universe: total population for whom Poverty level is determined, table X17,  8 fields); E16: Poverty in population in the past 12 months (universe: total population for whom Poverty level is determined, table X17, 7 fields); E17: Poverty in households in the past 12 months (universe: total households, table X17, 9 fields); E18: Percentage of families and people whose income in the past 12 months is below the poverty level (universe: families, population, table X17, 8 fields), and; X19: Poverty and income deficit (dollars) in the past 12 months for families (universe: families with income below Poverty level in the past 12 months, table X17, 4 fields). The US Census geodemographic data are based on the 2013 TigerLines across multiple geographies. The spatial geographies were merged with ACS data tables. See full documentation at the OCACS project github page (https://github.com/ktalexan/OCACS-Geodemographics).
- **Terms of Use**: Original datasets from US Census TigerLine Geography (https://www.census.gov/geo/maps-data/data/tiger-line.html), and American FactFinder (https://factfinder.census.gov/) for the selected tables of the American Community Survey (ACS, 2013). Linking and merging geographic with demographic tables along with final production of the merged spatial geodatabase and online datasets are performed by Orange County Public Works, OC Survey Geospatial Services, Dr. Kostas Alexandridis, GISP.
- **Map**: https://data-ocpw.opendata.arcgis.com/maps/ocacs-2013-economic-characteristics-for-state-assembly-legislative-districts
- **Web**: https://data-ocpw.opendata.arcgis.com/datasets/OCPW::ocacs-2013-economic-characteristics-for-state-assembly-legislative-districts/about
- **REST**: https://services.arcgis.com/UXmFoWC7yDHcDN5Q/arcgis/rest/services/OCACS_2013_Economic_Characteristics_for_State_Assembly_Legislative_Districts/FeatureServer
- **Metadata**: https://www.arcgis.com/sharing/rest/content/items/cbff055806e44c1e88d9da84d7aae4e2/info/metadata/metadata.xml?format=default&output=html
- **GeoService API**: https://services.arcgis.com/UXmFoWC7yDHcDN5Q/arcgis/rest/services/OCACS_2013_Economic_Characteristics_for_State_Assembly_Legislative_Districts/FeatureServer/1/query?outFields=*&where=1%3D1
- **GeoJSON API**: https://services.arcgis.com/UXmFoWC7yDHcDN5Q/arcgis/rest/services/OCACS_2013_Economic_Characteristics_for_State_Assembly_Legislative_Districts/FeatureServer/1/query?outFields=*&where=1%3D1&f=geojson

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2013.3.7. State Senate Legislative Districts Economic Characteristics

- **Name**: OCACS2013ULE
- **Title**: OCACS 2013 State Senate Legislative Districts Selected Economic Characteristics
- **Tags**: geodemographics, Orange County, California, US Census, ACS, American Community Survey, Economic Characteristics, State Senate, Legislative Districts, employment status, work status, worker, commuting, travel time, vehicles, transportation, occupation, industry, class of worker, income, earnings, health insurance, poverty
- **Summary**: Key economic characteristics of the 2013 American Community Survey (ACS), 5-year estimates for State Senate Legislative Districts (Upper) in Orange County, California. 
- **Description**: US Census American Community Survey (ACS) 2013, 5-year estimates of the key economic characteristics of State Senate Legislative District (Upper) geographic level in Orange County, California. The data contains 397 fields for the variable groups E01: Employment status (universe: population 16 years and over, table X23, 7 fields); E02: Work status by age of worker (universe: population 16 years and over, table X23, 36 fields); E03: Commuting to work (universe: workers 16 years and over, table X8, 8 fields); E04: Travel time to work (universe: workers 16 years and over who did not work at home, table X8, 14 fields); E05: Number of vehicles available for workers (universe: workers 16 years and over in households, table X8, 8 fields); E06: Median age by means of transportation to work (universe: median age, workers 16 years and over, table X8, 7 fields); E07: Means of transportation to work by race (universe: workers 16 years and over, table X8, 64 fields); E08: Occupation (universe: civilian employed population 16 years and over, table X24, 53 fields); E09: Industry (universe: civilian employed population 16 years and over, table X24, 43 fields); E10: Class of worker (universe: civilian employed population 16 years and over, table X24, 19 fields); E11: Household income and earnings in the past 12 months (universe: total households, table X19, 37 fields); E12: Income and earnings in dollars (universe: inflation-adjusted dollars, tables X19-X20, 31 fields); E13: Family income in dollars (universe: total families, table X19, 17 fields); E14: Health insurance coverage (universe: total families, table X19, 17 fields); E15: Ratio of income to Poverty level (universe: total population for whom Poverty level is determined, table X17,  8 fields); E16: Poverty in population in the past 12 months (universe: total population for whom Poverty level is determined, table X17, 7 fields); E17: Poverty in households in the past 12 months (universe: total households, table X17, 9 fields); E18: Percentage of families and people whose income in the past 12 months is below the poverty level (universe: families, population, table X17, 8 fields), and; X19: Poverty and income deficit (dollars) in the past 12 months for families (universe: families with income below Poverty level in the past 12 months, table X17, 4 fields). The US Census geodemographic data are based on the 2013 TigerLines across multiple geographies. The spatial geographies were merged with ACS data tables. See full documentation at the OCACS project github page (https://github.com/ktalexan/OCACS-Geodemographics).
- **Terms of Use**: Original datasets from US Census TigerLine Geography (https://www.census.gov/geo/maps-data/data/tiger-line.html), and American FactFinder (https://factfinder.census.gov/) for the selected tables of the American Community Survey (ACS, 2013). Linking and merging geographic with demographic tables along with final production of the merged spatial geodatabase and online datasets are performed by Orange County Public Works, OC Survey Geospatial Services, Dr. Kostas Alexandridis, GISP.
- **Map**: https://data-ocpw.opendata.arcgis.com/maps/ocacs-2013-economic-characteristics-for-state-senate-legislative-districts
- **Web**: https://data-ocpw.opendata.arcgis.com/datasets/OCPW::ocacs-2013-economic-characteristics-for-state-senate-legislative-districts/about
- **REST**: https://services.arcgis.com/UXmFoWC7yDHcDN5Q/arcgis/rest/services/OCACS_2013_Economic_Characteristics_for_State_Senate_Legislative_Districts/FeatureServer
- **Metadata**: https://www.arcgis.com/sharing/rest/content/items/16e56339e519406b9d6b59934aeb9088/info/metadata/metadata.xml?format=default&output=html
- **GeoService API**: https://services.arcgis.com/UXmFoWC7yDHcDN5Q/arcgis/rest/services/OCACS_2013_Economic_Characteristics_for_State_Senate_Legislative_Districts/FeatureServer/1/query?outFields=*&where=1%3D1
- **GeoJSON API**: https://services.arcgis.com/UXmFoWC7yDHcDN5Q/arcgis/rest/services/OCACS_2013_Economic_Characteristics_for_State_Senate_Legislative_Districts/FeatureServer/1/query?outFields=*&where=1%3D1&f=geojson

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2013.3.8. Elementary School Districts Economic Characteristics

- **Name**: OCACS2013EDE
- **Title**: OCACS 2013 Elementary School Districts Selected Economic Characteristics
- **Tags**: geodemographics, Orange County, California, US Census, ACS, American Community Survey, Economic Characteristics, Elementary School Districts, employment status, work status, worker, commuting, travel time, vehicles, transportation, occupation, industry, class of worker, income, earnings, health insurance, poverty
- **Summary**: Key economic characteristics of the 2013 American Community Survey (ACS), 5-year estimates for Elementary School Districts in Orange County, California. 
- **Description**: US Census American Community Survey (ACS) 2013, 5-year estimates of the key economic characteristics of Elementary School Districts geographic level in Orange County, California. The data contains 397 fields for the variable groups E01: Employment status (universe: population 16 years and over, table X23, 7 fields); E02: Work status by age of worker (universe: population 16 years and over, table X23, 36 fields); E03: Commuting to work (universe: workers 16 years and over, table X8, 8 fields); E04: Travel time to work (universe: workers 16 years and over who did not work at home, table X8, 14 fields); E05: Number of vehicles available for workers (universe: workers 16 years and over in households, table X8, 8 fields); E06: Median age by means of transportation to work (universe: median age, workers 16 years and over, table X8, 7 fields); E07: Means of transportation to work by race (universe: workers 16 years and over, table X8, 64 fields); E08: Occupation (universe: civilian employed population 16 years and over, table X24, 53 fields); E09: Industry (universe: civilian employed population 16 years and over, table X24, 43 fields); E10: Class of worker (universe: civilian employed population 16 years and over, table X24, 19 fields); E11: Household income and earnings in the past 12 months (universe: total households, table X19, 37 fields); E12: Income and earnings in dollars (universe: inflation-adjusted dollars, tables X19-X20, 31 fields); E13: Family income in dollars (universe: total families, table X19, 17 fields); E14: Health insurance coverage (universe: total families, table X19, 17 fields); E15: Ratio of income to Poverty level (universe: total population for whom Poverty level is determined, table X17,  8 fields); E16: Poverty in population in the past 12 months (universe: total population for whom Poverty level is determined, table X17, 7 fields); E17: Poverty in households in the past 12 months (universe: total households, table X17, 9 fields); E18: Percentage of families and people whose income in the past 12 months is below the poverty level (universe: families, population, table X17, 8 fields), and; X19: Poverty and income deficit (dollars) in the past 12 months for families (universe: families with income below Poverty level in the past 12 months, table X17, 4 fields). The US Census geodemographic data are based on the 2013 TigerLines across multiple geographies. The spatial geographies were merged with ACS data tables. See full documentation at the OCACS project github page (https://github.com/ktalexan/OCACS-Geodemographics).
- **Terms of Use**: Original datasets from US Census TigerLine Geography (https://www.census.gov/geo/maps-data/data/tiger-line.html), and American FactFinder (https://factfinder.census.gov/) for the selected tables of the American Community Survey (ACS, 2013). Linking and merging geographic with demographic tables along with final production of the merged spatial geodatabase and online datasets are performed by Orange County Public Works, OC Survey Geospatial Services, Dr. Kostas Alexandridis, GISP.
- **Map**: https://data-ocpw.opendata.arcgis.com/maps/ocacs-2013-economic-characteristics-for-elementary-school-districts
- **Web**: https://data-ocpw.opendata.arcgis.com/datasets/OCPW::ocacs-2013-economic-characteristics-for-elementary-school-districts/about
- **REST**: https://services.arcgis.com/UXmFoWC7yDHcDN5Q/arcgis/rest/services/OCACS_2013_Economic_Characteristics_for_Elementary_School_Districts/FeatureServer
- **Metadata**: https://www.arcgis.com/sharing/rest/content/items/e183d85e3181480581857523aefa7e8f/info/metadata/metadata.xml?format=default&output=html
- **GeoService API**: https://services.arcgis.com/UXmFoWC7yDHcDN5Q/arcgis/rest/services/OCACS_2013_Economic_Characteristics_for_Elementary_School_Districts/FeatureServer/1/query?outFields=*&where=1%3D1
- **GeoJSON API**: https://services.arcgis.com/UXmFoWC7yDHcDN5Q/arcgis/rest/services/OCACS_2013_Economic_Characteristics_for_Elementary_School_Districts/FeatureServer/1/query?outFields=*&where=1%3D1&f=geojson

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2013.3.9. Secondary School Districts Economic Characteristics

- **Name**: OCACS2013SDE
- **Title**: OCACS 2013 Secondary School Districts Selected Economic Characteristics
- **Tags**: geodemographics, Orange County, California, US Census, ACS, American Community Survey, Economic Characteristics, Secondary School Districts, employment status, work status, worker, commuting, travel time, vehicles, transportation, occupation, industry, class of worker, income, earnings, health insurance, poverty
- **Summary**: Key economic characteristics of the 2013 American Community Survey (ACS), 5-year estimates for Secondary School Districts in Orange County, California. 
- **Description**: US Census American Community Survey (ACS) 2013, 5-year estimates of the key economic characteristics of Secondary School Districts geographic level in Orange County, California. The data contains 397 fields for the variable groups E01: Employment status (universe: population 16 years and over, table X23, 7 fields); E02: Work status by age of worker (universe: population 16 years and over, table X23, 36 fields); E03: Commuting to work (universe: workers 16 years and over, table X8, 8 fields); E04: Travel time to work (universe: workers 16 years and over who did not work at home, table X8, 14 fields); E05: Number of vehicles available for workers (universe: workers 16 years and over in households, table X8, 8 fields); E06: Median age by means of transportation to work (universe: median age, workers 16 years and over, table X8, 7 fields); E07: Means of transportation to work by race (universe: workers 16 years and over, table X8, 64 fields); E08: Occupation (universe: civilian employed population 16 years and over, table X24, 53 fields); E09: Industry (universe: civilian employed population 16 years and over, table X24, 43 fields); E10: Class of worker (universe: civilian employed population 16 years and over, table X24, 19 fields); E11: Household income and earnings in the past 12 months (universe: total households, table X19, 37 fields); E12: Income and earnings in dollars (universe: inflation-adjusted dollars, tables X19-X20, 31 fields); E13: Family income in dollars (universe: total families, table X19, 17 fields); E14: Health insurance coverage (universe: total families, table X19, 17 fields); E15: Ratio of income to Poverty level (universe: total population for whom Poverty level is determined, table X17,  8 fields); E16: Poverty in population in the past 12 months (universe: total population for whom Poverty level is determined, table X17, 7 fields); E17: Poverty in households in the past 12 months (universe: total households, table X17, 9 fields); E18: Percentage of families and people whose income in the past 12 months is below the poverty level (universe: families, population, table X17, 8 fields), and; X19: Poverty and income deficit (dollars) in the past 12 months for families (universe: families with income below Poverty level in the past 12 months, table X17, 4 fields). The US Census geodemographic data are based on the 2013 TigerLines across multiple geographies. The spatial geographies were merged with ACS data tables. See full documentation at the OCACS project github page (https://github.com/ktalexan/OCACS-Geodemographics).
- **Terms of Use**: Original datasets from US Census TigerLine Geography (https://www.census.gov/geo/maps-data/data/tiger-line.html), and American FactFinder (https://factfinder.census.gov/) for the selected tables of the American Community Survey (ACS, 2013). Linking and merging geographic with demographic tables along with final production of the merged spatial geodatabase and online datasets are performed by Orange County Public Works, OC Survey Geospatial Services, Dr. Kostas Alexandridis, GISP.
- **Map**: https://data-ocpw.opendata.arcgis.com/maps/ocacs-2013-economic-characteristics-for-secondary-school-districts
- **Web**: https://data-ocpw.opendata.arcgis.com/datasets/OCPW::ocacs-2013-economic-characteristics-for-secondary-school-districts/about
- **REST**: https://services.arcgis.com/UXmFoWC7yDHcDN5Q/arcgis/rest/services/OCACS_2013_Economic_Characteristics_for_Secondary_School_Districts/FeatureServer
- **Metadata**: https://www.arcgis.com/sharing/rest/content/items/92280cb7d4d94a959a777c78950bf347/info/metadata/metadata.xml?format=default&output=html
- **GeoService API**: https://services.arcgis.com/UXmFoWC7yDHcDN5Q/arcgis/rest/services/OCACS_2013_Economic_Characteristics_for_Secondary_School_Districts/FeatureServer/1/query?outFields=*&where=1%3D1
- **GeoJSON API**: https://services.arcgis.com/UXmFoWC7yDHcDN5Q/arcgis/rest/services/OCACS_2013_Economic_Characteristics_for_Secondary_School_Districts/FeatureServer/1/query?outFields=*&where=1%3D1&f=geojson

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2013.3.10. Unified School Districts Economic Characteristics

- **Name**: OCACS2013UDE
- **Title**: OCACS 2013 Unified School Districts Selected Economic Characteristics
- **Tags**: geodemographics, Orange County, California, US Census, ACS, American Community Survey, Economic Characteristics, Unified School Districts, employment status, work status, worker, commuting, travel time, vehicles, transportation, occupation, industry, class of worker, income, earnings, health insurance, poverty
- **Summary**: Key economic characteristics of the 2013 American Community Survey (ACS), 5-year estimates for Unified School Districts in Orange County, California. 
- **Description**: US Census American Community Survey (ACS) 2013, 5-year estimates of the key economic characteristics of Unified School Districts geographic level in Orange County, California. The data contains 397 fields for the variable groups E01: Employment status (universe: population 16 years and over, table X23, 7 fields); E02: Work status by age of worker (universe: population 16 years and over, table X23, 36 fields); E03: Commuting to work (universe: workers 16 years and over, table X8, 8 fields); E04: Travel time to work (universe: workers 16 years and over who did not work at home, table X8, 14 fields); E05: Number of vehicles available for workers (universe: workers 16 years and over in households, table X8, 8 fields); E06: Median age by means of transportation to work (universe: median age, workers 16 years and over, table X8, 7 fields); E07: Means of transportation to work by race (universe: workers 16 years and over, table X8, 64 fields); E08: Occupation (universe: civilian employed population 16 years and over, table X24, 53 fields); E09: Industry (universe: civilian employed population 16 years and over, table X24, 43 fields); E10: Class of worker (universe: civilian employed population 16 years and over, table X24, 19 fields); E11: Household income and earnings in the past 12 months (universe: total households, table X19, 37 fields); E12: Income and earnings in dollars (universe: inflation-adjusted dollars, tables X19-X20, 31 fields); E13: Family income in dollars (universe: total families, table X19, 17 fields); E14: Health insurance coverage (universe: total families, table X19, 17 fields); E15: Ratio of income to Poverty level (universe: total population for whom Poverty level is determined, table X17,  8 fields); E16: Poverty in population in the past 12 months (universe: total population for whom Poverty level is determined, table X17, 7 fields); E17: Poverty in households in the past 12 months (universe: total households, table X17, 9 fields); E18: Percentage of families and people whose income in the past 12 months is below the poverty level (universe: families, population, table X17, 8 fields), and; X19: Poverty and income deficit (dollars) in the past 12 months for families (universe: families with income below Poverty level in the past 12 months, table X17, 4 fields). The US Census geodemographic data are based on the 2013 TigerLines across multiple geographies. The spatial geographies were merged with ACS data tables. See full documentation at the OCACS project github page (https://github.com/ktalexan/OCACS-Geodemographics).
- **Terms of Use**: Original datasets from US Census TigerLine Geography (https://www.census.gov/geo/maps-data/data/tiger-line.html), and American FactFinder (https://factfinder.census.gov/) for the selected tables of the American Community Survey (ACS, 2013). Linking and merging geographic with demographic tables along with final production of the merged spatial geodatabase and online datasets are performed by Orange County Public Works, OC Survey Geospatial Services, Dr. Kostas Alexandridis, GISP.
- **Map**: https://data-ocpw.opendata.arcgis.com/maps/ocacs-2013-economic-characteristics-for-unified-school-districts
- **Web**: https://data-ocpw.opendata.arcgis.com/datasets/OCPW::ocacs-2013-economic-characteristics-for-unified-school-districts/about
- **REST**: https://services.arcgis.com/UXmFoWC7yDHcDN5Q/arcgis/rest/services/OCACS_2013_Economic_Characteristics_for_Unified_School_Districts/FeatureServer
- **Metadata**: https://www.arcgis.com/sharing/rest/content/items/10ae3cbaa4a74ed78b210234014a6bf4/info/metadata/metadata.xml?format=default&output=html
- **GeoService API**: https://services.arcgis.com/UXmFoWC7yDHcDN5Q/arcgis/rest/services/OCACS_2013_Economic_Characteristics_for_Unified_School_Districts/FeatureServer/1/query?outFields=*&where=1%3D1
- **GeoJSON API**: https://services.arcgis.com/UXmFoWC7yDHcDN5Q/arcgis/rest/services/OCACS_2013_Economic_Characteristics_for_Unified_School_Districts/FeatureServer/1/query?outFields=*&where=1%3D1&f=geojson

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2013.3.11. Urban Areas Economic Characteristics

- **Name**: OCACS2013UAE
- **Title**: OCACS 2013 Urban Areas Selected Economic Characteristics
- **Tags**: geodemographics, Orange County, California, US Census, ACS, American Community Survey, Economic Characteristics, Urban Areas, employment status, work status, worker, commuting, travel time, vehicles, transportation, occupation, industry, class of worker, income, earnings, health insurance, poverty
- **Summary**: Key economic characteristics of the 2013 American Community Survey (ACS), 5-year estimates for Urban Areas in Orange County, California. 
- **Description**: US Census American Community Survey (ACS) 2013, 5-year estimates of the key economic characteristics of Urban Areas geographic level in Orange County, California. The data contains 397 fields for the variable groups E01: Employment status (universe: population 16 years and over, table X23, 7 fields); E02: Work status by age of worker (universe: population 16 years and over, table X23, 36 fields); E03: Commuting to work (universe: workers 16 years and over, table X8, 8 fields); E04: Travel time to work (universe: workers 16 years and over who did not work at home, table X8, 14 fields); E05: Number of vehicles available for workers (universe: workers 16 years and over in households, table X8, 8 fields); E06: Median age by means of transportation to work (universe: median age, workers 16 years and over, table X8, 7 fields); E07: Means of transportation to work by race (universe: workers 16 years and over, table X8, 64 fields); E08: Occupation (universe: civilian employed population 16 years and over, table X24, 53 fields); E09: Industry (universe: civilian employed population 16 years and over, table X24, 43 fields); E10: Class of worker (universe: civilian employed population 16 years and over, table X24, 19 fields); E11: Household income and earnings in the past 12 months (universe: total households, table X19, 37 fields); E12: Income and earnings in dollars (universe: inflation-adjusted dollars, tables X19-X20, 31 fields); E13: Family income in dollars (universe: total families, table X19, 17 fields); E14: Health insurance coverage (universe: total families, table X19, 17 fields); E15: Ratio of income to Poverty level (universe: total population for whom Poverty level is determined, table X17,  8 fields); E16: Poverty in population in the past 12 months (universe: total population for whom Poverty level is determined, table X17, 7 fields); E17: Poverty in households in the past 12 months (universe: total households, table X17, 9 fields); E18: Percentage of families and people whose income in the past 12 months is below the poverty level (universe: families, population, table X17, 8 fields), and; X19: Poverty and income deficit (dollars) in the past 12 months for families (universe: families with income below Poverty level in the past 12 months, table X17, 4 fields). The US Census geodemographic data are based on the 2013 TigerLines across multiple geographies. The spatial geographies were merged with ACS data tables. See full documentation at the OCACS project github page (https://github.com/ktalexan/OCACS-Geodemographics).
- **Terms of Use**: Original datasets from US Census TigerLine Geography (https://www.census.gov/geo/maps-data/data/tiger-line.html), and American FactFinder (https://factfinder.census.gov/) for the selected tables of the American Community Survey (ACS, 2013). Linking and merging geographic with demographic tables along with final production of the merged spatial geodatabase and online datasets are performed by Orange County Public Works, OC Survey Geospatial Services, Dr. Kostas Alexandridis, GISP.
- **Map**: https://data-ocpw.opendata.arcgis.com/maps/ocacs-2013-economic-characteristics-for-urban-areas
- **Web**: https://data-ocpw.opendata.arcgis.com/datasets/OCPW::ocacs-2013-economic-characteristics-for-urban-areas/about
- **REST**: https://services.arcgis.com/UXmFoWC7yDHcDN5Q/arcgis/rest/services/OCACS_2013_Economic_Characteristics_for_Urban_Areas/FeatureServer
- **Metadata**: https://www.arcgis.com/sharing/rest/content/items/2aab05780b074189b1ac5dedd8bfa263/info/metadata/metadata.xml?format=default&output=html
- **GeoService API**: https://services.arcgis.com/UXmFoWC7yDHcDN5Q/arcgis/rest/services/OCACS_2013_Economic_Characteristics_for_Urban_Areas/FeatureServer/1/query?outFields=*&where=1%3D1
- **GeoJSON API**: https://services.arcgis.com/UXmFoWC7yDHcDN5Q/arcgis/rest/services/OCACS_2013_Economic_Characteristics_for_Urban_Areas/FeatureServer/1/query?outFields=*&where=1%3D1&f=geojson

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2013.3.12. Public Use Microdata Areas Economic Characteristics

- **Name**: OCACS2013PUE
- **Title**: OCACS 2013 Public Use Microdata Areas Selected Economic Characteristics
- **Tags**: geodemographics, Orange County, California, US Census, ACS, American Community Survey, Economic Characteristics, Public Use Microdata Areas, PUMA, employment status, work status, worker, commuting, travel time, vehicles, transportation, occupation, industry, class of worker, income, earnings, health insurance, poverty
- **Summary**: Key economic characteristics of the 2013 American Community Survey (ACS), 5-year estimates for Public Use Microdata Areas (PUMA) in Orange County, California. 
- **Description**: US Census American Community Survey (ACS) 2013, 5-year estimates of the key economic characteristics of Public Use Microdata Areas (PUMA) geographic level in Orange County, California. The data contains 397 fields for the variable groups E01: Employment status (universe: population 16 years and over, table X23, 7 fields); E02: Work status by age of worker (universe: population 16 years and over, table X23, 36 fields); E03: Commuting to work (universe: workers 16 years and over, table X8, 8 fields); E04: Travel time to work (universe: workers 16 years and over who did not work at home, table X8, 14 fields); E05: Number of vehicles available for workers (universe: workers 16 years and over in households, table X8, 8 fields); E06: Median age by means of transportation to work (universe: median age, workers 16 years and over, table X8, 7 fields); E07: Means of transportation to work by race (universe: workers 16 years and over, table X8, 64 fields); E08: Occupation (universe: civilian employed population 16 years and over, table X24, 53 fields); E09: Industry (universe: civilian employed population 16 years and over, table X24, 43 fields); E10: Class of worker (universe: civilian employed population 16 years and over, table X24, 19 fields); E11: Household income and earnings in the past 12 months (universe: total households, table X19, 37 fields); E12: Income and earnings in dollars (universe: inflation-adjusted dollars, tables X19-X20, 31 fields); E13: Family income in dollars (universe: total families, table X19, 17 fields); E14: Health insurance coverage (universe: total families, table X19, 17 fields); E15: Ratio of income to Poverty level (universe: total population for whom Poverty level is determined, table X17,  8 fields); E16: Poverty in population in the past 12 months (universe: total population for whom Poverty level is determined, table X17, 7 fields); E17: Poverty in households in the past 12 months (universe: total households, table X17, 9 fields); E18: Percentage of families and people whose income in the past 12 months is below the poverty level (universe: families, population, table X17, 8 fields), and; X19: Poverty and income deficit (dollars) in the past 12 months for families (universe: families with income below Poverty level in the past 12 months, table X17, 4 fields). The US Census geodemographic data are based on the 2013 TigerLines across multiple geographies. The spatial geographies were merged with ACS data tables. See full documentation at the OCACS project github page (https://github.com/ktalexan/OCACS-Geodemographics).
- **Terms of Use**: Original datasets from US Census TigerLine Geography (https://www.census.gov/geo/maps-data/data/tiger-line.html), and American FactFinder (https://factfinder.census.gov/) for the selected tables of the American Community Survey (ACS, 2013). Linking and merging geographic with demographic tables along with final production of the merged spatial geodatabase and online datasets are performed by Orange County Public Works, OC Survey Geospatial Services, Dr. Kostas Alexandridis, GISP.
- **Map**: https://data-ocpw.opendata.arcgis.com/maps/ocacs-2013-economic-characteristics-for-public-use-microdata-areas
- **Web**: https://data-ocpw.opendata.arcgis.com/datasets/OCPW::ocacs-2013-economic-characteristics-for-public-use-microdata-areas/about
- **REST**: https://services.arcgis.com/UXmFoWC7yDHcDN5Q/arcgis/rest/services/OCACS_2013_Economic_Characteristics_for_Public_Use_Microdata_Areas/FeatureServer
- **Metadata**: https://www.arcgis.com/sharing/rest/content/items/e0e7976030684380a156930c3726656f/info/metadata/metadata.xml?format=default&output=html
- **GeoService API**: https://services.arcgis.com/UXmFoWC7yDHcDN5Q/arcgis/rest/services/OCACS_2013_Economic_Characteristics_for_Public_Use_Microdata_Areas/FeatureServer/1/query?outFields=*&where=1%3D1
- **GeoJSON API**: https://services.arcgis.com/UXmFoWC7yDHcDN5Q/arcgis/rest/services/OCACS_2013_Economic_Characteristics_for_Public_Use_Microdata_Areas/FeatureServer/1/query?outFields=*&where=1%3D1&f=geojson

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2013.3.13. Block Groups Economic Characteristics

- **Name**: OCACS2013BGE
- **Title**: OCACS 2013 Block Groups Selected Economic Characteristics
- **Tags**: geodemographics, Orange County, California, US Census, ACS, American Community Survey, Economic Characteristics, Block Groups, employment status, work status, worker, commuting, travel time, vehicles, transportation, occupation, industry, class of worker, income, earnings, health insurance, poverty
- **Summary**: Key economic characteristics of the 2013 American Community Survey (ACS), 5-year estimates for Block Groups in Orange County, California. 
- **Description**: US Census American Community Survey (ACS) 2013, 5-year estimates of the key economic characteristics of Block Groups geographic level in Orange County, California. The data contains 397 fields for the variable groups E01: Employment status (universe: population 16 years and over, table X23, 7 fields); E02: Work status by age of worker (universe: population 16 years and over, table X23, 36 fields); E03: Commuting to work (universe: workers 16 years and over, table X8, 8 fields); E04: Travel time to work (universe: workers 16 years and over who did not work at home, table X8, 14 fields); E05: Number of vehicles available for workers (universe: workers 16 years and over in households, table X8, 8 fields); E06: Median age by means of transportation to work (universe: median age, workers 16 years and over, table X8, 7 fields); E07: Means of transportation to work by race (universe: workers 16 years and over, table X8, 64 fields); E08: Occupation (universe: civilian employed population 16 years and over, table X24, 53 fields); E09: Industry (universe: civilian employed population 16 years and over, table X24, 43 fields); E10: Class of worker (universe: civilian employed population 16 years and over, table X24, 19 fields); E11: Household income and earnings in the past 12 months (universe: total households, table X19, 37 fields); E12: Income and earnings in dollars (universe: inflation-adjusted dollars, tables X19-X20, 31 fields); E13: Family income in dollars (universe: total families, table X19, 17 fields); E14: Health insurance coverage (universe: total families, table X19, 17 fields); E15: Ratio of income to Poverty level (universe: total population for whom Poverty level is determined, table X17,  8 fields); E16: Poverty in population in the past 12 months (universe: total population for whom Poverty level is determined, table X17, 7 fields); E17: Poverty in households in the past 12 months (universe: total households, table X17, 9 fields); E18: Percentage of families and people whose income in the past 12 months is below the poverty level (universe: families, population, table X17, 8 fields), and; X19: Poverty and income deficit (dollars) in the past 12 months for families (universe: families with income below Poverty level in the past 12 months, table X17, 4 fields). The US Census geodemographic data are based on the 2013 TigerLines across multiple geographies. The spatial geographies were merged with ACS data tables. See full documentation at the OCACS project github page (https://github.com/ktalexan/OCACS-Geodemographics).
- **Terms of Use**: Original datasets from US Census TigerLine Geography (https://www.census.gov/geo/maps-data/data/tiger-line.html), and American FactFinder (https://factfinder.census.gov/) for the selected tables of the American Community Survey (ACS, 2013). Linking and merging geographic with demographic tables along with final production of the merged spatial geodatabase and online datasets are performed by Orange County Public Works, OC Survey Geospatial Services, Dr. Kostas Alexandridis, GISP.
- **Map**: https://data-ocpw.opendata.arcgis.com/maps/ocacs-2013-economic-characteristics-for-block-groups
- **Web**: https://data-ocpw.opendata.arcgis.com/datasets/OCPW::ocacs-2013-economic-characteristics-for-block-groups/about
- **REST**: https://services.arcgis.com/UXmFoWC7yDHcDN5Q/arcgis/rest/services/OCACS_2013_Economic_Characteristics_for_Block_Groups/FeatureServer
- **Metadata**: https://www.arcgis.com/sharing/rest/content/items/5c139a90ad5048c286ad818c59de0a6a/info/metadata/metadata.xml?format=default&output=html
- **GeoService API**: https://services.arcgis.com/UXmFoWC7yDHcDN5Q/arcgis/rest/services/OCACS_2013_Economic_Characteristics_for_Block_Groups/FeatureServer/1/query?outFields=*&where=1%3D1
- **GeoJSON API**: https://services.arcgis.com/UXmFoWC7yDHcDN5Q/arcgis/rest/services/OCACS_2013_Economic_Characteristics_for_Block_Groups/FeatureServer/1/query?outFields=*&where=1%3D1&f=geojson

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2013.3.14. Census Tracts Economic Characteristics

- **Name**: OCACS2013TRE
- **Title**: OCACS 2013 Census Tracts Selected Economic Characteristics
- **Tags**: geodemographics, Orange County, California, US Census, ACS, American Community Survey, Economic Characteristics, Census Tracts, employment status, work status, worker, commuting, travel time, vehicles, transportation, occupation, industry, class of worker, income, earnings, health insurance, poverty
- **Summary**: Key economic characteristics of the 2013 American Community Survey (ACS), 5-year estimates for Census Tracts in Orange County, California. 
- **Description**: US Census American Community Survey (ACS) 2013, 5-year estimates of the key economic characteristics of Census Tracts geographic level in Orange County, California. The data contains 397 fields for the variable groups E01: Employment status (universe: population 16 years and over, table X23, 7 fields); E02: Work status by age of worker (universe: population 16 years and over, table X23, 36 fields); E03: Commuting to work (universe: workers 16 years and over, table X8, 8 fields); E04: Travel time to work (universe: workers 16 years and over who did not work at home, table X8, 14 fields); E05: Number of vehicles available for workers (universe: workers 16 years and over in households, table X8, 8 fields); E06: Median age by means of transportation to work (universe: median age, workers 16 years and over, table X8, 7 fields); E07: Means of transportation to work by race (universe: workers 16 years and over, table X8, 64 fields); E08: Occupation (universe: civilian employed population 16 years and over, table X24, 53 fields); E09: Industry (universe: civilian employed population 16 years and over, table X24, 43 fields); E10: Class of worker (universe: civilian employed population 16 years and over, table X24, 19 fields); E11: Household income and earnings in the past 12 months (universe: total households, table X19, 37 fields); E12: Income and earnings in dollars (universe: inflation-adjusted dollars, tables X19-X20, 31 fields); E13: Family income in dollars (universe: total families, table X19, 17 fields); E14: Health insurance coverage (universe: total families, table X19, 17 fields); E15: Ratio of income to Poverty level (universe: total population for whom Poverty level is determined, table X17,  8 fields); E16: Poverty in population in the past 12 months (universe: total population for whom Poverty level is determined, table X17, 7 fields); E17: Poverty in households in the past 12 months (universe: total households, table X17, 9 fields); E18: Percentage of families and people whose income in the past 12 months is below the poverty level (universe: families, population, table X17, 8 fields), and; X19: Poverty and income deficit (dollars) in the past 12 months for families (universe: families with income below Poverty level in the past 12 months, table X17, 4 fields). The US Census geodemographic data are based on the 2013 TigerLines across multiple geographies. The spatial geographies were merged with ACS data tables. See full documentation at the OCACS project github page (https://github.com/ktalexan/OCACS-Geodemographics).
- **Terms of Use**: Original datasets from US Census TigerLine Geography (https://www.census.gov/geo/maps-data/data/tiger-line.html), and American FactFinder (https://factfinder.census.gov/) for the selected tables of the American Community Survey (ACS, 2013). Linking and merging geographic with demographic tables along with final production of the merged spatial geodatabase and online datasets are performed by Orange County Public Works, OC Survey Geospatial Services, Dr. Kostas Alexandridis, GISP.
- **Map**: https://data-ocpw.opendata.arcgis.com/maps/ocacs-2013-economic-characteristics-for-census-tracts
- **Web**: https://data-ocpw.opendata.arcgis.com/datasets/OCPW::ocacs-2013-economic-characteristics-for-census-tracts/about
- **REST**: https://services.arcgis.com/UXmFoWC7yDHcDN5Q/arcgis/rest/services/OCACS_2013_Economic_Characteristics_for_Census_Tracts/FeatureServer
- **Metadata**: https://www.arcgis.com/sharing/rest/content/items/68a2ebed510a48079c343fc4099e106c/info/metadata/metadata.xml?format=default&output=html
- **GeoService API**: https://services.arcgis.com/UXmFoWC7yDHcDN5Q/arcgis/rest/services/OCACS_2013_Economic_Characteristics_for_Census_Tracts/FeatureServer/1/query?outFields=*&where=1%3D1
- **GeoJSON API**: https://services.arcgis.com/UXmFoWC7yDHcDN5Q/arcgis/rest/services/OCACS_2013_Economic_Characteristics_for_Census_Tracts/FeatureServer/1/query?outFields=*&where=1%3D1&f=geojson

[<div align="right"><< Back to Contents</div>](#contents)

---
### 2013.4. Housing Characteristics
---
> #### 2013.4.1. County Level Housing Characteristics

- **Name**: OCACS2013COH
- **Title**: OCACS 2013 County Level Selected Housing Characteristics
- **Tags**: geodemographics, Orange County, California, US Census, ACS, American Community Survey, Housing Characteristics, Orange County, housing occupancy, units, tenure, year built, rooms, bedrooms, vacancy status, vehicles, heating fuel, kitchen, plumbing, occupants, housing value, price asked, mortgage status, owner costs, rent value, gross rent
- **Summary**: Key housing characteristics of the 2013 American Community Survey (ACS), 5-year estimates for Orange County, California. 
- **Description**: US Census American Community Survey (ACS) 2013, 5-year estimates of the key housing characteristics for Orange County, California. The data contains 406 fields for the variable groups H01: Housing occupancy (universe: total housing units, table X25, 3 fields); H02: Units in structure (universe: total housing units, table X25, 11 fields); H03: Population in occupied housing units by tenure by units in structure (universe: total population in occupied housing units, table X25, 13 fields); H04: Year structure built (universe: total housing units, table X25, 15 fields); H05: Rooms (universe: total housing units, table X25, 18 fields); H06: Bedrooms (universe: total housing units, table X25, 21 fields); H07: Housing tenure by race of householder (universe: occupied housing units, table X25, 51 fields); H08: Total population in occupied housing units by tenure (universe: total population in occupied housing units, table X25, 3 fields); H09: Vacancy status (universe: vacant housing units, table X25, 8 fields); H10: Occupied housing units by race of householder (universe: occupied housing units, table X25, 8 fields); H11: Year householder moved into unit (universe: occupied housing units, table X25, 18 fields); H12: Vehicles available (universe: occupied housing units, table X25, 18 fields); H13: Housing heating fuel (universe: occupied housing units, table X25, 10 fields); H14: Selected housing characteristics (universe: occupied housing units, table X25, 9 fields); H15: Occupants per room (universe: occupied housing units, table X25, 13 fields); H16: Housing value (universe: owner-occupied units, table X25, 32 fields); H17: Price asked for vacant for sale only, and sold not occupied housing units (universe: vacant for sale only, and sold not occupied housing units, table X25, 28 fields); H18: Mortgage status (universe: owner-occupied units, table X25, 10 fields); H19: Selected monthly owner costs, SMOC (universe: owner-occupied housing units with or without a mortgage, table X25, 45 fields); H20: Selected monthly owner costs as a percentage of household income, SMOCAPI (universe: owner-occupied housing units with or without a mortgage, table X25, 26 fields); H21: Contract rent distribution and rent asked distribution in dollars (universe: renter-occupied housing units paying cash rent and vacant, for rent, and rented not occupied housing units, table X25, 7 fields); H22: Gross rent (universe: occupied units paying rent, table X25, 28 fields), and; X23: Gross rent as percentage of household income (universe: occupied units paying rent, table X25, 11 fields). The US Census geodemographic data are based on the 2013 TigerLines across multiple geographies. The spatial geographies were merged with ACS data tables. See full documentation at the OCACS project github page (https://github.com/ktalexan/OCACS-Geodemographics).
- **Terms of Use**: Original datasets from US Census TigerLine Geography (https://www.census.gov/geo/maps-data/data/tiger-line.html), and American FactFinder (https://factfinder.census.gov/) for the selected tables of the American Community Survey (ACS, 2013). Linking and merging geographic with demographic tables along with final production of the merged spatial geodatabase and online datasets are performed by Orange County Public Works, OC Survey Geospatial Services, Dr. Kostas Alexandridis, GISP.
- **Map**: https://data-ocpw.opendata.arcgis.com/maps/ocacs-2013-housing-characteristics-for-orange-county
- **Web**: https://data-ocpw.opendata.arcgis.com/datasets/OCPW::ocacs-2013-housing-characteristics-for-orange-county/about
- **REST**: https://services.arcgis.com/UXmFoWC7yDHcDN5Q/arcgis/rest/services/OCACS_2013_Housing_Characteristics_for_Orange_County/FeatureServer
- **Metadata**: https://www.arcgis.com/sharing/rest/content/items/8879d406cbd24571b69af3de345e7a86/info/metadata/metadata.xml?format=default&output=html
- **GeoService API**: https://services.arcgis.com/UXmFoWC7yDHcDN5Q/arcgis/rest/services/OCACS_2013_Housing_Characteristics_for_Orange_County/FeatureServer/1/query?outFields=*&where=1%3D1
- **GeoJSON API**: https://services.arcgis.com/UXmFoWC7yDHcDN5Q/arcgis/rest/services/OCACS_2013_Housing_Characteristics_for_Orange_County/FeatureServer/1/query?outFields=*&where=1%3D1&f=geojson

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2013.4.2. County Subdivision Housing Characteristics

- **Name**: OCACS2013CSH
- **Title**: OCACS 2013 County Subdivisions Selected Housing Characteristics
- **Tags**: geodemographics, Orange County, California, US Census, ACS, American Community Survey, Housing Characteristics, County Subdivisions, housing occupancy, units, tenure, year built, rooms, bedrooms, vacancy status, vehicles, heating fuel, kitchen, plumbing, occupants, housing value, price asked, mortgage status, owner costs, rent value, gross rent
- **Summary**: Key housing characteristics of the 2013 American Community Survey (ACS), 5-year estimates for County Subdivisions in Orange County, California. 
- **Description**: US Census American Community Survey (ACS) 2013, 5-year estimates of the key housing characteristics of County Subdivisions geographic level in Orange County, California. The data contains 406 fields for the variable groups H01: Housing occupancy (universe: total housing units, table X25, 3 fields); H02: Units in structure (universe: total housing units, table X25, 11 fields); H03: Population in occupied housing units by tenure by units in structure (universe: total population in occupied housing units, table X25, 13 fields); H04: Year structure built (universe: total housing units, table X25, 15 fields); H05: Rooms (universe: total housing units, table X25, 18 fields); H06: Bedrooms (universe: total housing units, table X25, 21 fields); H07: Housing tenure by race of householder (universe: occupied housing units, table X25, 51 fields); H08: Total population in occupied housing units by tenure (universe: total population in occupied housing units, table X25, 3 fields); H09: Vacancy status (universe: vacant housing units, table X25, 8 fields); H10: Occupied housing units by race of householder (universe: occupied housing units, table X25, 8 fields); H11: Year householder moved into unit (universe: occupied housing units, table X25, 18 fields); H12: Vehicles available (universe: occupied housing units, table X25, 18 fields); H13: Housing heating fuel (universe: occupied housing units, table X25, 10 fields); H14: Selected housing characteristics (universe: occupied housing units, table X25, 9 fields); H15: Occupants per room (universe: occupied housing units, table X25, 13 fields); H16: Housing value (universe: owner-occupied units, table X25, 32 fields); H17: Price asked for vacant for sale only, and sold not occupied housing units (universe: vacant for sale only, and sold not occupied housing units, table X25, 28 fields); H18: Mortgage status (universe: owner-occupied units, table X25, 10 fields); H19: Selected monthly owner costs, SMOC (universe: owner-occupied housing units with or without a mortgage, table X25, 45 fields); H20: Selected monthly owner costs as a percentage of household income, SMOCAPI (universe: owner-occupied housing units with or without a mortgage, table X25, 26 fields); H21: Contract rent distribution and rent asked distribution in dollars (universe: renter-occupied housing units paying cash rent and vacant, for rent, and rented not occupied housing units, table X25, 7 fields); H22: Gross rent (universe: occupied units paying rent, table X25, 28 fields), and; X23: Gross rent as percentage of household income (universe: occupied units paying rent, table X25, 11 fields). The US Census geodemographic data are based on the 2013 TigerLines across multiple geographies. The spatial geographies were merged with ACS data tables. See full documentation at the OCACS project github page (https://github.com/ktalexan/OCACS-Geodemographics).
- **Terms of Use**: Original datasets from US Census TigerLine Geography (https://www.census.gov/geo/maps-data/data/tiger-line.html), and American FactFinder (https://factfinder.census.gov/) for the selected tables of the American Community Survey (ACS, 2013). Linking and merging geographic with demographic tables along with final production of the merged spatial geodatabase and online datasets are performed by Orange County Public Works, OC Survey Geospatial Services, Dr. Kostas Alexandridis, GISP.
- **Map**: https://data-ocpw.opendata.arcgis.com/maps/ocacs-2013-housing-characteristics-for-county-subdivisions
- **Web**: https://data-ocpw.opendata.arcgis.com/datasets/OCPW::ocacs-2013-housing-characteristics-for-county-subdivisions/about
- **REST**: https://services.arcgis.com/UXmFoWC7yDHcDN5Q/arcgis/rest/services/OCACS_2013_Housing_Characteristics_for_County_Subdivisions/FeatureServer
- **Metadata**: https://www.arcgis.com/sharing/rest/content/items/b0b0333214404a80b153333786233ec6/info/metadata/metadata.xml?format=default&output=html
- **GeoService API**: https://services.arcgis.com/UXmFoWC7yDHcDN5Q/arcgis/rest/services/OCACS_2013_Housing_Characteristics_for_County_Subdivisions/FeatureServer/1/query?outFields=*&where=1%3D1
- **GeoJSON API**: https://services.arcgis.com/UXmFoWC7yDHcDN5Q/arcgis/rest/services/OCACS_2013_Housing_Characteristics_for_County_Subdivisions/FeatureServer/1/query?outFields=*&where=1%3D1&f=geojson

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2013.4.3. Cities/Places Housing Characteristics

- **Name**: OCACS2013PLH
- **Title**: OCACS 2013 Cities Selected Housing Characteristics
- **Tags**: geodemographics, Orange County, California, US Census, ACS, American Community Survey, Housing Characteristics, Cities, Places, housing occupancy, units, tenure, year built, rooms, bedrooms, vacancy status, vehicles, heating fuel, kitchen, plumbing, occupants, housing value, price asked, mortgage status, owner costs, rent value, gross rent
- **Summary**: Key housing characteristics of the 2013 American Community Survey (ACS), 5-year estimates for Cities/Places in Orange County, California. 
- **Description**: US Census American Community Survey (ACS) 2013, 5-year estimates of the key housing characteristics of Cities/Places geographic level in Orange County, California. The data contains 406 fields for the variable groups H01: Housing occupancy (universe: total housing units, table X25, 3 fields); H02: Units in structure (universe: total housing units, table X25, 11 fields); H03: Population in occupied housing units by tenure by units in structure (universe: total population in occupied housing units, table X25, 13 fields); H04: Year structure built (universe: total housing units, table X25, 15 fields); H05: Rooms (universe: total housing units, table X25, 18 fields); H06: Bedrooms (universe: total housing units, table X25, 21 fields); H07: Housing tenure by race of householder (universe: occupied housing units, table X25, 51 fields); H08: Total population in occupied housing units by tenure (universe: total population in occupied housing units, table X25, 3 fields); H09: Vacancy status (universe: vacant housing units, table X25, 8 fields); H10: Occupied housing units by race of householder (universe: occupied housing units, table X25, 8 fields); H11: Year householder moved into unit (universe: occupied housing units, table X25, 18 fields); H12: Vehicles available (universe: occupied housing units, table X25, 18 fields); H13: Housing heating fuel (universe: occupied housing units, table X25, 10 fields); H14: Selected housing characteristics (universe: occupied housing units, table X25, 9 fields); H15: Occupants per room (universe: occupied housing units, table X25, 13 fields); H16: Housing value (universe: owner-occupied units, table X25, 32 fields); H17: Price asked for vacant for sale only, and sold not occupied housing units (universe: vacant for sale only, and sold not occupied housing units, table X25, 28 fields); H18: Mortgage status (universe: owner-occupied units, table X25, 10 fields); H19: Selected monthly owner costs, SMOC (universe: owner-occupied housing units with or without a mortgage, table X25, 45 fields); H20: Selected monthly owner costs as a percentage of household income, SMOCAPI (universe: owner-occupied housing units with or without a mortgage, table X25, 26 fields); H21: Contract rent distribution and rent asked distribution in dollars (universe: renter-occupied housing units paying cash rent and vacant, for rent, and rented not occupied housing units, table X25, 7 fields); H22: Gross rent (universe: occupied units paying rent, table X25, 28 fields), and; X23: Gross rent as percentage of household income (universe: occupied units paying rent, table X25, 11 fields). The US Census geodemographic data are based on the 2013 TigerLines across multiple geographies. The spatial geographies were merged with ACS data tables. See full documentation at the OCACS project github page (https://github.com/ktalexan/OCACS-Geodemographics).
- **Terms of Use**: Original datasets from US Census TigerLine Geography (https://www.census.gov/geo/maps-data/data/tiger-line.html), and American FactFinder (https://factfinder.census.gov/) for the selected tables of the American Community Survey (ACS, 2013). Linking and merging geographic with demographic tables along with final production of the merged spatial geodatabase and online datasets are performed by Orange County Public Works, OC Survey Geospatial Services, Dr. Kostas Alexandridis, GISP.
- **Map**: https://data-ocpw.opendata.arcgis.com/maps/ocacs-2013-housing-characteristics-for-cities
- **Web**: https://data-ocpw.opendata.arcgis.com/datasets/OCPW::ocacs-2013-housing-characteristics-for-cities/about
- **REST**: https://services.arcgis.com/UXmFoWC7yDHcDN5Q/arcgis/rest/services/OCACS_2013_Housing_Characteristics_for_Cities/FeatureServer
- **Metadata**: https://www.arcgis.com/sharing/rest/content/items/9b3a83cfcd0b4e6cb6c5965aeaa340ff/info/metadata/metadata.xml?format=default&output=html
- **GeoService API**: https://services.arcgis.com/UXmFoWC7yDHcDN5Q/arcgis/rest/services/OCACS_2013_Housing_Characteristics_for_Cities/FeatureServer/1/query?outFields=*&where=1%3D1
- **GeoJSON API**: https://services.arcgis.com/UXmFoWC7yDHcDN5Q/arcgis/rest/services/OCACS_2013_Housing_Characteristics_for_Cities/FeatureServer/1/query?outFields=*&where=1%3D1&f=geojson

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2013.4.4. ZIP Code Tabulation Areas Housing Characteristics

- **Name**: OCACS2013ZCH
- **Title**: OCACS 2013 ZIP Code Tabulation Areas Selected Housing Characteristics
- **Tags**: geodemographics, Orange County, California, US Census, ACS, American Community Survey, Housing Characteristics, ZIP Code, housing occupancy, units, tenure, year built, rooms, bedrooms, vacancy status, vehicles, heating fuel, kitchen, plumbing, occupants, housing value, price asked, mortgage status, owner costs, rent value, gross rent
- **Summary**: Key housing characteristics of the 2013 American Community Survey (ACS), 5-year estimates for ZIP Code Tabulation Areas in Orange County, California. 
- **Description**: US Census American Community Survey (ACS) 2013, 5-year estimates of the key housing characteristics of ZIP Code Tabulation Areas geographic level in Orange County, California. The data contains 406 fields for the variable groups H01: Housing occupancy (universe: total housing units, table X25, 3 fields); H02: Units in structure (universe: total housing units, table X25, 11 fields); H03: Population in occupied housing units by tenure by units in structure (universe: total population in occupied housing units, table X25, 13 fields); H04: Year structure built (universe: total housing units, table X25, 15 fields); H05: Rooms (universe: total housing units, table X25, 18 fields); H06: Bedrooms (universe: total housing units, table X25, 21 fields); H07: Housing tenure by race of householder (universe: occupied housing units, table X25, 51 fields); H08: Total population in occupied housing units by tenure (universe: total population in occupied housing units, table X25, 3 fields); H09: Vacancy status (universe: vacant housing units, table X25, 8 fields); H10: Occupied housing units by race of householder (universe: occupied housing units, table X25, 8 fields); H11: Year householder moved into unit (universe: occupied housing units, table X25, 18 fields); H12: Vehicles available (universe: occupied housing units, table X25, 18 fields); H13: Housing heating fuel (universe: occupied housing units, table X25, 10 fields); H14: Selected housing characteristics (universe: occupied housing units, table X25, 9 fields); H15: Occupants per room (universe: occupied housing units, table X25, 13 fields); H16: Housing value (universe: owner-occupied units, table X25, 32 fields); H17: Price asked for vacant for sale only, and sold not occupied housing units (universe: vacant for sale only, and sold not occupied housing units, table X25, 28 fields); H18: Mortgage status (universe: owner-occupied units, table X25, 10 fields); H19: Selected monthly owner costs, SMOC (universe: owner-occupied housing units with or without a mortgage, table X25, 45 fields); H20: Selected monthly owner costs as a percentage of household income, SMOCAPI (universe: owner-occupied housing units with or without a mortgage, table X25, 26 fields); H21: Contract rent distribution and rent asked distribution in dollars (universe: renter-occupied housing units paying cash rent and vacant, for rent, and rented not occupied housing units, table X25, 7 fields); H22: Gross rent (universe: occupied units paying rent, table X25, 28 fields), and; X23: Gross rent as percentage of household income (universe: occupied units paying rent, table X25, 11 fields). The US Census geodemographic data are based on the 2013 TigerLines across multiple geographies. The spatial geographies were merged with ACS data tables. See full documentation at the OCACS project github page (https://github.com/ktalexan/OCACS-Geodemographics).
- **Terms of Use**: Original datasets from US Census TigerLine Geography (https://www.census.gov/geo/maps-data/data/tiger-line.html), and American FactFinder (https://factfinder.census.gov/) for the selected tables of the American Community Survey (ACS, 2013). Linking and merging geographic with demographic tables along with final production of the merged spatial geodatabase and online datasets are performed by Orange County Public Works, OC Survey Geospatial Services, Dr. Kostas Alexandridis, GISP.
- **Map**: https://data-ocpw.opendata.arcgis.com/maps/ocacs-2013-housing-characteristics-for-zip-code-tabulation-areas
- **Web**: https://data-ocpw.opendata.arcgis.com/datasets/OCPW::ocacs-2013-housing-characteristics-for-zip-code-tabulation-areas/about
- **REST**: https://services.arcgis.com/UXmFoWC7yDHcDN5Q/arcgis/rest/services/OCACS_2013_Housing_Characteristics_for_ZIP_Code_Tabulation_Areas/FeatureServer
- **Metadata**: https://www.arcgis.com/sharing/rest/content/items/a4aa9b25f63d4690b873778f9aca272e/info/metadata/metadata.xml?format=default&output=html
- **GeoService API**: https://services.arcgis.com/UXmFoWC7yDHcDN5Q/arcgis/rest/services/OCACS_2013_Housing_Characteristics_for_ZIP_Code_Tabulation_Areas/FeatureServer/1/query?outFields=*&where=1%3D1
- **GeoJSON API**: https://services.arcgis.com/UXmFoWC7yDHcDN5Q/arcgis/rest/services/OCACS_2013_Housing_Characteristics_for_ZIP_Code_Tabulation_Areas/FeatureServer/1/query?outFields=*&where=1%3D1&f=geojson

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2013.4.5. Congressional Districts Housing Characteristics

- **Name**: OCACS2013CDH
- **Title**: OCACS 2013 Congressional Districts Selected Housing Characteristics
- **Tags**: geodemographics, Orange County, California, US Census, ACS, American Community Survey, Housing Characteristics, Congressional Districts, 115th US Congress, housing occupancy, units, tenure, year built, rooms, bedrooms, vacancy status, vehicles, heating fuel, kitchen, plumbing, occupants, housing value, price asked, mortgage status, owner costs, rent value, gross rent
- **Summary**: Key housing characteristics of the 2013 American Community Survey (ACS), 5-year estimates for Congressional Districts (115th US Congress) in Orange County, California. 
- **Description**: US Census American Community Survey (ACS) 2013, 5-year estimates of the key housing characteristics of Congressional Districts (115th US Congress) geographic level in Orange County, California. The data contains 406 fields for the variable groups H01: Housing occupancy (universe: total housing units, table X25, 3 fields); H02: Units in structure (universe: total housing units, table X25, 11 fields); H03: Population in occupied housing units by tenure by units in structure (universe: total population in occupied housing units, table X25, 13 fields); H04: Year structure built (universe: total housing units, table X25, 15 fields); H05: Rooms (universe: total housing units, table X25, 18 fields); H06: Bedrooms (universe: total housing units, table X25, 21 fields); H07: Housing tenure by race of householder (universe: occupied housing units, table X25, 51 fields); H08: Total population in occupied housing units by tenure (universe: total population in occupied housing units, table X25, 3 fields); H09: Vacancy status (universe: vacant housing units, table X25, 8 fields); H10: Occupied housing units by race of householder (universe: occupied housing units, table X25, 8 fields); H11: Year householder moved into unit (universe: occupied housing units, table X25, 18 fields); H12: Vehicles available (universe: occupied housing units, table X25, 18 fields); H13: Housing heating fuel (universe: occupied housing units, table X25, 10 fields); H14: Selected housing characteristics (universe: occupied housing units, table X25, 9 fields); H15: Occupants per room (universe: occupied housing units, table X25, 13 fields); H16: Housing value (universe: owner-occupied units, table X25, 32 fields); H17: Price asked for vacant for sale only, and sold not occupied housing units (universe: vacant for sale only, and sold not occupied housing units, table X25, 28 fields); H18: Mortgage status (universe: owner-occupied units, table X25, 10 fields); H19: Selected monthly owner costs, SMOC (universe: owner-occupied housing units with or without a mortgage, table X25, 45 fields); H20: Selected monthly owner costs as a percentage of household income, SMOCAPI (universe: owner-occupied housing units with or without a mortgage, table X25, 26 fields); H21: Contract rent distribution and rent asked distribution in dollars (universe: renter-occupied housing units paying cash rent and vacant, for rent, and rented not occupied housing units, table X25, 7 fields); H22: Gross rent (universe: occupied units paying rent, table X25, 28 fields), and; X23: Gross rent as percentage of household income (universe: occupied units paying rent, table X25, 11 fields). The US Census geodemographic data are based on the 2013 TigerLines across multiple geographies. The spatial geographies were merged with ACS data tables. See full documentation at the OCACS project github page (https://github.com/ktalexan/OCACS-Geodemographics).
- **Terms of Use**: Original datasets from US Census TigerLine Geography (https://www.census.gov/geo/maps-data/data/tiger-line.html), and American FactFinder (https://factfinder.census.gov/) for the selected tables of the American Community Survey (ACS, 2013). Linking and merging geographic with demographic tables along with final production of the merged spatial geodatabase and online datasets are performed by Orange County Public Works, OC Survey Geospatial Services, Dr. Kostas Alexandridis, GISP.
- **Map**: https://data-ocpw.opendata.arcgis.com/maps/ocacs-2013-housing-characteristics-for-congressional-districts-of-the-113th-us-congress
- **Web**: https://data-ocpw.opendata.arcgis.com/datasets/OCPW::ocacs-2013-housing-characteristics-for-congressional-districts-of-the-113th-us-congress/about
- **REST**: https://services.arcgis.com/UXmFoWC7yDHcDN5Q/arcgis/rest/services/OCACS_2013_Housing_Characteristics_for_Congressional_Districts_of_the_113th_US_Congress/FeatureServer
- **Metadata**: https://www.arcgis.com/sharing/rest/content/items/e406d65ef75c46a887f789d4245ab7fc/info/metadata/metadata.xml?format=default&output=html
- **GeoService API**: https://services.arcgis.com/UXmFoWC7yDHcDN5Q/arcgis/rest/services/OCACS_2013_Housing_Characteristics_for_Congressional_Districts_of_the_113th_US_Congress/FeatureServer/1/query?outFields=*&where=1%3D1
- **GeoJSON API**: https://services.arcgis.com/UXmFoWC7yDHcDN5Q/arcgis/rest/services/OCACS_2013_Housing_Characteristics_for_Congressional_Districts_of_the_113th_US_Congress/FeatureServer/1/query?outFields=*&where=1%3D1&f=geojson

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2013.4.6. State Assembly Legislative Districts Housing Characteristics

- **Name**: OCACS2013LLH
- **Title**: OCACS 2013 State Assembly Legislative Districts Selected Housing Characteristics
- **Tags**: geodemographics, Orange County, California, US Census, ACS, American Community Survey, Housing Characteristics, State Assembly, Legislative Districts, housing occupancy, units, tenure, year built, rooms, bedrooms, vacancy status, vehicles, heating fuel, kitchen, plumbing, occupants, housing value, price asked, mortgage status, owner costs, rent value, gross rent
- **Summary**: Key housing characteristics of the 2013 American Community Survey (ACS), 5-year estimates for State Assembly Legislative Districts (Lower) in Orange County, California. 
- **Description**: US Census American Community Survey (ACS) 2013, 5-year estimates of the key housing characteristics of State Assembly Legislative Districts (Lower) geographic level in Orange County, California. The data contains 406 fields for the variable groups H01: Housing occupancy (universe: total housing units, table X25, 3 fields); H02: Units in structure (universe: total housing units, table X25, 11 fields); H03: Population in occupied housing units by tenure by units in structure (universe: total population in occupied housing units, table X25, 13 fields); H04: Year structure built (universe: total housing units, table X25, 15 fields); H05: Rooms (universe: total housing units, table X25, 18 fields); H06: Bedrooms (universe: total housing units, table X25, 21 fields); H07: Housing tenure by race of householder (universe: occupied housing units, table X25, 51 fields); H08: Total population in occupied housing units by tenure (universe: total population in occupied housing units, table X25, 3 fields); H09: Vacancy status (universe: vacant housing units, table X25, 8 fields); H10: Occupied housing units by race of householder (universe: occupied housing units, table X25, 8 fields); H11: Year householder moved into unit (universe: occupied housing units, table X25, 18 fields); H12: Vehicles available (universe: occupied housing units, table X25, 18 fields); H13: Housing heating fuel (universe: occupied housing units, table X25, 10 fields); H14: Selected housing characteristics (universe: occupied housing units, table X25, 9 fields); H15: Occupants per room (universe: occupied housing units, table X25, 13 fields); H16: Housing value (universe: owner-occupied units, table X25, 32 fields); H17: Price asked for vacant for sale only, and sold not occupied housing units (universe: vacant for sale only, and sold not occupied housing units, table X25, 28 fields); H18: Mortgage status (universe: owner-occupied units, table X25, 10 fields); H19: Selected monthly owner costs, SMOC (universe: owner-occupied housing units with or without a mortgage, table X25, 45 fields); H20: Selected monthly owner costs as a percentage of household income, SMOCAPI (universe: owner-occupied housing units with or without a mortgage, table X25, 26 fields); H21: Contract rent distribution and rent asked distribution in dollars (universe: renter-occupied housing units paying cash rent and vacant, for rent, and rented not occupied housing units, table X25, 7 fields); H22: Gross rent (universe: occupied units paying rent, table X25, 28 fields), and; X23: Gross rent as percentage of household income (universe: occupied units paying rent, table X25, 11 fields). The US Census geodemographic data are based on the 2013 TigerLines across multiple geographies. The spatial geographies were merged with ACS data tables. See full documentation at the OCACS project github page (https://github.com/ktalexan/OCACS-Geodemographics).
- **Terms of Use**: Original datasets from US Census TigerLine Geography (https://www.census.gov/geo/maps-data/data/tiger-line.html), and American FactFinder (https://factfinder.census.gov/) for the selected tables of the American Community Survey (ACS, 2013). Linking and merging geographic with demographic tables along with final production of the merged spatial geodatabase and online datasets are performed by Orange County Public Works, OC Survey Geospatial Services, Dr. Kostas Alexandridis, GISP.
- **Map**: https://data-ocpw.opendata.arcgis.com/maps/ocacs-2013-housing-characteristics-for-state-assembly-legislative-districts
- **Web**: https://data-ocpw.opendata.arcgis.com/datasets/OCPW::ocacs-2013-housing-characteristics-for-state-assembly-legislative-districts/about
- **REST**: https://services.arcgis.com/UXmFoWC7yDHcDN5Q/arcgis/rest/services/OCACS_2013_Housing_Characteristics_for_State_Assembly_Legislative_Districts/FeatureServer
- **Metadata**: https://www.arcgis.com/sharing/rest/content/items/6a0951a767694b6daecea623100ce00b/info/metadata/metadata.xml?format=default&output=html
- **GeoService API**: https://services.arcgis.com/UXmFoWC7yDHcDN5Q/arcgis/rest/services/OCACS_2013_Housing_Characteristics_for_State_Assembly_Legislative_Districts/FeatureServer/1/query?outFields=*&where=1%3D1
- **GeoJSON API**: https://services.arcgis.com/UXmFoWC7yDHcDN5Q/arcgis/rest/services/OCACS_2013_Housing_Characteristics_for_State_Assembly_Legislative_Districts/FeatureServer/1/query?outFields=*&where=1%3D1&f=geojson

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2013.4.7. State Senate Legislative Districts Housing Characteristics

- **Name**: OCACS2013ULH
- **Title**: OCACS 2013 State Senate Legislative Districts Selected Housing Characteristics
- **Tags**: geodemographics, Orange County, California, US Census, ACS, American Community Survey, Housing Characteristics, State Senate, Legislative Districts, housing occupancy, units, tenure, year built, rooms, bedrooms, vacancy status, vehicles, heating fuel, kitchen, plumbing, occupants, housing value, price asked, mortgage status, owner costs, rent value, gross rent
- **Summary**: Key housing characteristics of the 2013 American Community Survey (ACS), 5-year estimates for State Senate Legislative Districts (Upper) in Orange County, California. 
- **Description**: US Census American Community Survey (ACS) 2013, 5-year estimates of the key housing characteristics of State Senate Legislative Districts (Upper) geographic level in Orange County, California. The data contains 406 fields for the variable groups H01: Housing occupancy (universe: total housing units, table X25, 3 fields); H02: Units in structure (universe: total housing units, table X25, 11 fields); H03: Population in occupied housing units by tenure by units in structure (universe: total population in occupied housing units, table X25, 13 fields); H04: Year structure built (universe: total housing units, table X25, 15 fields); H05: Rooms (universe: total housing units, table X25, 18 fields); H06: Bedrooms (universe: total housing units, table X25, 21 fields); H07: Housing tenure by race of householder (universe: occupied housing units, table X25, 51 fields); H08: Total population in occupied housing units by tenure (universe: total population in occupied housing units, table X25, 3 fields); H09: Vacancy status (universe: vacant housing units, table X25, 8 fields); H10: Occupied housing units by race of householder (universe: occupied housing units, table X25, 8 fields); H11: Year householder moved into unit (universe: occupied housing units, table X25, 18 fields); H12: Vehicles available (universe: occupied housing units, table X25, 18 fields); H13: Housing heating fuel (universe: occupied housing units, table X25, 10 fields); H14: Selected housing characteristics (universe: occupied housing units, table X25, 9 fields); H15: Occupants per room (universe: occupied housing units, table X25, 13 fields); H16: Housing value (universe: owner-occupied units, table X25, 32 fields); H17: Price asked for vacant for sale only, and sold not occupied housing units (universe: vacant for sale only, and sold not occupied housing units, table X25, 28 fields); H18: Mortgage status (universe: owner-occupied units, table X25, 10 fields); H19: Selected monthly owner costs, SMOC (universe: owner-occupied housing units with or without a mortgage, table X25, 45 fields); H20: Selected monthly owner costs as a percentage of household income, SMOCAPI (universe: owner-occupied housing units with or without a mortgage, table X25, 26 fields); H21: Contract rent distribution and rent asked distribution in dollars (universe: renter-occupied housing units paying cash rent and vacant, for rent, and rented not occupied housing units, table X25, 7 fields); H22: Gross rent (universe: occupied units paying rent, table X25, 28 fields), and; X23: Gross rent as percentage of household income (universe: occupied units paying rent, table X25, 11 fields). The US Census geodemographic data are based on the 2013 TigerLines across multiple geographies. The spatial geographies were merged with ACS data tables. See full documentation at the OCACS project github page (https://github.com/ktalexan/OCACS-Geodemographics).
- **Terms of Use**: Original datasets from US Census TigerLine Geography (https://www.census.gov/geo/maps-data/data/tiger-line.html), and American FactFinder (https://factfinder.census.gov/) for the selected tables of the American Community Survey (ACS, 2013). Linking and merging geographic with demographic tables along with final production of the merged spatial geodatabase and online datasets are performed by Orange County Public Works, OC Survey Geospatial Services, Dr. Kostas Alexandridis, GISP.
- **Map**: https://data-ocpw.opendata.arcgis.com/maps/ocacs-2013-housing-characteristics-for-state-senate-legislative-districts
- **Web**: https://data-ocpw.opendata.arcgis.com/datasets/OCPW::ocacs-2013-housing-characteristics-for-state-senate-legislative-districts/about
- **REST**: https://services.arcgis.com/UXmFoWC7yDHcDN5Q/arcgis/rest/services/OCACS_2013_Housing_Characteristics_for_State_Senate_Legislative_Districts/FeatureServer
- **Metadata**: https://www.arcgis.com/sharing/rest/content/items/d81b6e09b12c4ca1976d38e51523f1cb/info/metadata/metadata.xml?format=default&output=html
- **GeoService API**: https://services.arcgis.com/UXmFoWC7yDHcDN5Q/arcgis/rest/services/OCACS_2013_Housing_Characteristics_for_State_Senate_Legislative_Districts/FeatureServer/1/query?outFields=*&where=1%3D1
- **GeoJSON API**: https://services.arcgis.com/UXmFoWC7yDHcDN5Q/arcgis/rest/services/OCACS_2013_Housing_Characteristics_for_State_Senate_Legislative_Districts/FeatureServer/1/query?outFields=*&where=1%3D1&f=geojson

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2013.4.8. Elementary School Districts Housing Characteristics

- **Name**: OCACS2013EDH
- **Title**: OCACS 2013 Elementary School Districts Selected Housing Characteristics
- **Tags**: geodemographics, Orange County, California, US Census, ACS, American Community Survey, Housing Characteristics, Elementary School Districts, housing occupancy, units, tenure, year built, rooms, bedrooms, vacancy status, vehicles, heating fuel, kitchen, plumbing, occupants, housing value, price asked, mortgage status, owner costs, rent value, gross rent
- **Summary**: Key housing characteristics of the 2013 American Community Survey (ACS), 5-year estimates for Elementary School Districts in Orange County, California. 
- **Description**: US Census American Community Survey (ACS) 2013, 5-year estimates of the key housing characteristics of Elementary School Districts geographic level in Orange County, California. The data contains 406 fields for the variable groups H01: Housing occupancy (universe: total housing units, table X25, 3 fields); H02: Units in structure (universe: total housing units, table X25, 11 fields); H03: Population in occupied housing units by tenure by units in structure (universe: total population in occupied housing units, table X25, 13 fields); H04: Year structure built (universe: total housing units, table X25, 15 fields); H05: Rooms (universe: total housing units, table X25, 18 fields); H06: Bedrooms (universe: total housing units, table X25, 21 fields); H07: Housing tenure by race of householder (universe: occupied housing units, table X25, 51 fields); H08: Total population in occupied housing units by tenure (universe: total population in occupied housing units, table X25, 3 fields); H09: Vacancy status (universe: vacant housing units, table X25, 8 fields); H10: Occupied housing units by race of householder (universe: occupied housing units, table X25, 8 fields); H11: Year householder moved into unit (universe: occupied housing units, table X25, 18 fields); H12: Vehicles available (universe: occupied housing units, table X25, 18 fields); H13: Housing heating fuel (universe: occupied housing units, table X25, 10 fields); H14: Selected housing characteristics (universe: occupied housing units, table X25, 9 fields); H15: Occupants per room (universe: occupied housing units, table X25, 13 fields); H16: Housing value (universe: owner-occupied units, table X25, 32 fields); H17: Price asked for vacant for sale only, and sold not occupied housing units (universe: vacant for sale only, and sold not occupied housing units, table X25, 28 fields); H18: Mortgage status (universe: owner-occupied units, table X25, 10 fields); H19: Selected monthly owner costs, SMOC (universe: owner-occupied housing units with or without a mortgage, table X25, 45 fields); H20: Selected monthly owner costs as a percentage of household income, SMOCAPI (universe: owner-occupied housing units with or without a mortgage, table X25, 26 fields); H21: Contract rent distribution and rent asked distribution in dollars (universe: renter-occupied housing units paying cash rent and vacant, for rent, and rented not occupied housing units, table X25, 7 fields); H22: Gross rent (universe: occupied units paying rent, table X25, 28 fields), and; X23: Gross rent as percentage of household income (universe: occupied units paying rent, table X25, 11 fields). The US Census geodemographic data are based on the 2013 TigerLines across multiple geographies. The spatial geographies were merged with ACS data tables. See full documentation at the OCACS project github page (https://github.com/ktalexan/OCACS-Geodemographics).
- **Terms of Use**: Original datasets from US Census TigerLine Geography (https://www.census.gov/geo/maps-data/data/tiger-line.html), and American FactFinder (https://factfinder.census.gov/) for the selected tables of the American Community Survey (ACS, 2013). Linking and merging geographic with demographic tables along with final production of the merged spatial geodatabase and online datasets are performed by Orange County Public Works, OC Survey Geospatial Services, Dr. Kostas Alexandridis, GISP.
- **Map**: https://data-ocpw.opendata.arcgis.com/maps/ocacs-2013-housing-characteristics-for-elementary-school-districts
- **Web**: <https://data-ocpw.opendata.arcgis.com/datasets/OCPW::ocacs-2013-housing-characteristics-for-elementary-school-districts/about>

- **REST**: https://services.arcgis.com/UXmFoWC7yDHcDN5Q/arcgis/rest/services/OCACS_2013_Housing_Characteristics_for_Elementary_School_Districts/FeatureServer
- **Metadata**: https://www.arcgis.com/sharing/rest/content/items/5b5277fed86c4a13b374da4d26a68046/info/metadata/metadata.xml?format=default&output=html
- **GeoService API**: https://services.arcgis.com/UXmFoWC7yDHcDN5Q/arcgis/rest/services/OCACS_2013_Housing_Characteristics_for_Elementary_School_Districts/FeatureServer/1/query?outFields=*&where=1%3D1
- **GeoJSON API**: https://services.arcgis.com/UXmFoWC7yDHcDN5Q/arcgis/rest/services/OCACS_2013_Housing_Characteristics_for_Elementary_School_Districts/FeatureServer/1/query?outFields=*&where=1%3D1&f=geojson

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2013.4.9. Secondary School Districts Housing Characteristics

- **Name**: OCACS2013SDH
- **Title**: OCACS 2013 Secondary School Districts Selected Housing Characteristics
- **Tags**: geodemographics, Orange County, California, US Census, ACS, American Community Survey, Housing Characteristics, Secondary School Districts, housing occupancy, units, tenure, year built, rooms, bedrooms, vacancy status, vehicles, heating fuel, kitchen, plumbing, occupants, housing value, price asked, mortgage status, owner costs, rent value, gross rent
- **Summary**: Key housing characteristics of the 2013 American Community Survey (ACS), 5-year estimates for Secondary School Districts in Orange County, California.
- **Description**: US Census American Community Survey (ACS) 2013, 5-year estimates of the key housing characteristics of Secondary School Districts geographic level in Orange County, California. The data contains 406 fields for the variable groups H01: Housing occupancy (universe: total housing units, table X25, 3 fields); H02: Units in structure (universe: total housing units, table X25, 11 fields); H03: Population in occupied housing units by tenure by units in structure (universe: total population in occupied housing units, table X25, 13 fields); H04: Year structure built (universe: total housing units, table X25, 15 fields); H05: Rooms (universe: total housing units, table X25, 18 fields); H06: Bedrooms (universe: total housing units, table X25, 21 fields); H07: Housing tenure by race of householder (universe: occupied housing units, table X25, 51 fields); H08: Total population in occupied housing units by tenure (universe: total population in occupied housing units, table X25, 3 fields); H09: Vacancy status (universe: vacant housing units, table X25, 8 fields); H10: Occupied housing units by race of householder (universe: occupied housing units, table X25, 8 fields); H11: Year householder moved into unit (universe: occupied housing units, table X25, 18 fields); H12: Vehicles available (universe: occupied housing units, table X25, 18 fields); H13: Housing heating fuel (universe: occupied housing units, table X25, 10 fields); H14: Selected housing characteristics (universe: occupied housing units, table X25, 9 fields); H15: Occupants per room (universe: occupied housing units, table X25, 13 fields); H16: Housing value (universe: owner-occupied units, table X25, 32 fields); H17: Price asked for vacant for sale only, and sold not occupied housing units (universe: vacant for sale only, and sold not occupied housing units, table X25, 28 fields); H18: Mortgage status (universe: owner-occupied units, table X25, 10 fields); H19: Selected monthly owner costs, SMOC (universe: owner-occupied housing units with or without a mortgage, table X25, 45 fields); H20: Selected monthly owner costs as a percentage of household income, SMOCAPI (universe: owner-occupied housing units with or without a mortgage, table X25, 26 fields); H21: Contract rent distribution and rent asked distribution in dollars (universe: renter-occupied housing units paying cash rent and vacant, for rent, and rented not occupied housing units, table X25, 7 fields); H22: Gross rent (universe: occupied units paying rent, table X25, 28 fields), and; X23: Gross rent as percentage of household income (universe: occupied units paying rent, table X25, 11 fields). The US Census geodemographic data are based on the 2013 TigerLines across multiple geographies. The spatial geographies were merged with ACS data tables. See full documentation at the OCACS project github page (https://github.com/ktalexan/OCACS-Geodemographics).
- **Terms of Use**: Original datasets from US Census TigerLine Geography (https://www.census.gov/geo/maps-data/data/tiger-line.html), and American FactFinder (https://factfinder.census.gov/) for the selected tables of the American Community Survey (ACS, 2013). Linking and merging geographic with demographic tables along with final production of the merged spatial geodatabase and online datasets are performed by Orange County Public Works, OC Survey Geospatial Services, Dr. Kostas Alexandridis, GISP.
- **Map**: https://data-ocpw.opendata.arcgis.com/maps/ocacs-2013-housing-characteristics-for-secondary-school-districts
- **Web**: https://data-ocpw.opendata.arcgis.com/datasets/OCPW::ocacs-2013-housing-characteristics-for-secondary-school-districts/about
- **REST**: https://services.arcgis.com/UXmFoWC7yDHcDN5Q/arcgis/rest/services/OCACS_2013_Housing_Characteristics_for_Secondary_School_Districts/FeatureServer
- **Metadata**: https://www.arcgis.com/sharing/rest/content/items/b294c080a0d646309a0ec1bb91880a82/info/metadata/metadata.xml?format=default&output=html
- **GeoService API**: https://services.arcgis.com/UXmFoWC7yDHcDN5Q/arcgis/rest/services/OCACS_2013_Housing_Characteristics_for_Secondary_School_Districts/FeatureServer/1/query?outFields=*&where=1%3D1
- **GeoJSON API**: https://services.arcgis.com/UXmFoWC7yDHcDN5Q/arcgis/rest/services/OCACS_2013_Housing_Characteristics_for_Secondary_School_Districts/FeatureServer/1/query?outFields=*&where=1%3D1&f=geojson

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2013.4.10. Unified School Districts Housing Characteristics

- **Name**: OCACS2013UDH
- **Title**: OCACS 2013 Unified School Districts Selected Housing Characteristics
- **Tags**: geodemographics, Orange County, California, US Census, ACS, American Community Survey, Housing Characteristics, Unified School Districts, housing occupancy, units, tenure, year built, rooms, bedrooms, vacancy status, vehicles, heating fuel, kitchen, plumbing, occupants, housing value, price asked, mortgage status, owner costs, rent value, gross rent
- **Summary**: Key housing characteristics of the 2013 American Community Survey (ACS), 5-year estimates for Unified School Districts in Orange County, California.
- **Description**: US Census American Community Survey (ACS) 2013, 5-year estimates of the key housing characteristics of Unified School Districts geographic level in Orange County, California. The data contains 406 fields for the variable groups H01: Housing occupancy (universe: total housing units, table X25, 3 fields); H02: Units in structure (universe: total housing units, table X25, 11 fields); H03: Population in occupied housing units by tenure by units in structure (universe: total population in occupied housing units, table X25, 13 fields); H04: Year structure built (universe: total housing units, table X25, 15 fields); H05: Rooms (universe: total housing units, table X25, 18 fields); H06: Bedrooms (universe: total housing units, table X25, 21 fields); H07: Housing tenure by race of householder (universe: occupied housing units, table X25, 51 fields); H08: Total population in occupied housing units by tenure (universe: total population in occupied housing units, table X25, 3 fields); H09: Vacancy status (universe: vacant housing units, table X25, 8 fields); H10: Occupied housing units by race of householder (universe: occupied housing units, table X25, 8 fields); H11: Year householder moved into unit (universe: occupied housing units, table X25, 18 fields); H12: Vehicles available (universe: occupied housing units, table X25, 18 fields); H13: Housing heating fuel (universe: occupied housing units, table X25, 10 fields); H14: Selected housing characteristics (universe: occupied housing units, table X25, 9 fields); H15: Occupants per room (universe: occupied housing units, table X25, 13 fields); H16: Housing value (universe: owner-occupied units, table X25, 32 fields); H17: Price asked for vacant for sale only, and sold not occupied housing units (universe: vacant for sale only, and sold not occupied housing units, table X25, 28 fields); H18: Mortgage status (universe: owner-occupied units, table X25, 10 fields); H19: Selected monthly owner costs, SMOC (universe: owner-occupied housing units with or without a mortgage, table X25, 45 fields); H20: Selected monthly owner costs as a percentage of household income, SMOCAPI (universe: owner-occupied housing units with or without a mortgage, table X25, 26 fields); H21: Contract rent distribution and rent asked distribution in dollars (universe: renter-occupied housing units paying cash rent and vacant, for rent, and rented not occupied housing units, table X25, 7 fields); H22: Gross rent (universe: occupied units paying rent, table X25, 28 fields), and; X23: Gross rent as percentage of household income (universe: occupied units paying rent, table X25, 11 fields). The US Census geodemographic data are based on the 2013 TigerLines across multiple geographies. The spatial geographies were merged with ACS data tables. See full documentation at the OCACS project github page (https://github.com/ktalexan/OCACS-Geodemographics).
- **Terms of Use**: Original datasets from US Census TigerLine Geography (https://www.census.gov/geo/maps-data/data/tiger-line.html), and American FactFinder (https://factfinder.census.gov/) for the selected tables of the American Community Survey (ACS, 2013). Linking and merging geographic with demographic tables along with final production of the merged spatial geodatabase and online datasets are performed by Orange County Public Works, OC Survey Geospatial Services, Dr. Kostas Alexandridis, GISP.
- **Map**: https://data-ocpw.opendata.arcgis.com/maps/ocacs-2013-housing-characteristics-for-unified-school-districts
- **Web**: https://data-ocpw.opendata.arcgis.com/datasets/OCPW::ocacs-2013-housing-characteristics-for-unified-school-districts/about
- **REST**: https://services.arcgis.com/UXmFoWC7yDHcDN5Q/arcgis/rest/services/OCACS_2013_Housing_Characteristics_for_Unified_School_Districts/FeatureServer
- **Metadata**: https://www.arcgis.com/sharing/rest/content/items/661c87a9a04948638841c838f265b4df/info/metadata/metadata.xml?format=default&output=html
- **GeoService API**: https://services.arcgis.com/UXmFoWC7yDHcDN5Q/arcgis/rest/services/OCACS_2013_Housing_Characteristics_for_Unified_School_Districts/FeatureServer/1/query?outFields=*&where=1%3D1
- **GeoJSON API**: https://services.arcgis.com/UXmFoWC7yDHcDN5Q/arcgis/rest/services/OCACS_2013_Housing_Characteristics_for_Unified_School_Districts/FeatureServer/1/query?outFields=*&where=1%3D1&f=geojson

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2013.4.11. Urban Areas Housing Characteristics

- **Name**: OCACS2013UAH
- **Title**: OCACS 2013 Urban Areas Selected Housing Characteristics
- **Tags**: geodemographics, Orange County, California, US Census, ACS, American Community Survey, Housing Characteristics, Urban Areas, housing occupancy, units, tenure, year built, rooms, bedrooms, vacancy status, vehicles, heating fuel, kitchen, plumbing, occupants, housing value, price asked, mortgage status, owner costs, rent value, gross rent
- **Summary**: Key housing characteristics of the 2013 American Community Survey (ACS), 5-year estimates for Urban Areas in Orange County, California.
- **Description**: US Census American Community Survey (ACS) 2013, 5-year estimates of the key housing characteristics of Urban Areas geographic level in Orange County, California. The data contains 406 fields for the variable groups H01: Housing occupancy (universe: total housing units, table X25, 3 fields); H02: Units in structure (universe: total housing units, table X25, 11 fields); H03: Population in occupied housing units by tenure by units in structure (universe: total population in occupied housing units, table X25, 13 fields); H04: Year structure built (universe: total housing units, table X25, 15 fields); H05: Rooms (universe: total housing units, table X25, 18 fields); H06: Bedrooms (universe: total housing units, table X25, 21 fields); H07: Housing tenure by race of householder (universe: occupied housing units, table X25, 51 fields); H08: Total population in occupied housing units by tenure (universe: total population in occupied housing units, table X25, 3 fields); H09: Vacancy status (universe: vacant housing units, table X25, 8 fields); H10: Occupied housing units by race of householder (universe: occupied housing units, table X25, 8 fields); H11: Year householder moved into unit (universe: occupied housing units, table X25, 18 fields); H12: Vehicles available (universe: occupied housing units, table X25, 18 fields); H13: Housing heating fuel (universe: occupied housing units, table X25, 10 fields); H14: Selected housing characteristics (universe: occupied housing units, table X25, 9 fields); H15: Occupants per room (universe: occupied housing units, table X25, 13 fields); H16: Housing value (universe: owner-occupied units, table X25, 32 fields); H17: Price asked for vacant for sale only, and sold not occupied housing units (universe: vacant for sale only, and sold not occupied housing units, table X25, 28 fields); H18: Mortgage status (universe: owner-occupied units, table X25, 10 fields); H19: Selected monthly owner costs, SMOC (universe: owner-occupied housing units with or without a mortgage, table X25, 45 fields); H20: Selected monthly owner costs as a percentage of household income, SMOCAPI (universe: owner-occupied housing units with or without a mortgage, table X25, 26 fields); H21: Contract rent distribution and rent asked distribution in dollars (universe: renter-occupied housing units paying cash rent and vacant, for rent, and rented not occupied housing units, table X25, 7 fields); H22: Gross rent (universe: occupied units paying rent, table X25, 28 fields), and; X23: Gross rent as percentage of household income (universe: occupied units paying rent, table X25, 11 fields). The US Census geodemographic data are based on the 2013 TigerLines across multiple geographies. The spatial geographies were merged with ACS data tables. See full documentation at the OCACS project github page (https://github.com/ktalexan/OCACS-Geodemographics).
- **Terms of Use**: Original datasets from US Census TigerLine Geography (https://www.census.gov/geo/maps-data/data/tiger-line.html), and American FactFinder (https://factfinder.census.gov/) for the selected tables of the American Community Survey (ACS, 2013). Linking and merging geographic with demographic tables along with final production of the merged spatial geodatabase and online datasets are performed by Orange County Public Works, OC Survey Geospatial Services, Dr. Kostas Alexandridis, GISP.
- **Map**: https://data-ocpw.opendata.arcgis.com/maps/ocacs-2013-housing-characteristics-for-urban-areas
- **Web**: https://data-ocpw.opendata.arcgis.com/datasets/OCPW::ocacs-2013-housing-characteristics-for-urban-areas/about
- **REST**: https://services.arcgis.com/UXmFoWC7yDHcDN5Q/arcgis/rest/services/OCACS_2013_Housing_Characteristics_for_Urban_Areas/FeatureServer
- **Metadata**: https://www.arcgis.com/sharing/rest/content/items/f5db27ebd6ca45c9bdcd5d3221a01f26/info/metadata/metadata.xml?format=default&output=html
- **GeoService API**: https://services.arcgis.com/UXmFoWC7yDHcDN5Q/arcgis/rest/services/OCACS_2013_Housing_Characteristics_for_Urban_Areas/FeatureServer/1/query?outFields=*&where=1%3D1
- **GeoJSON API**: https://services.arcgis.com/UXmFoWC7yDHcDN5Q/arcgis/rest/services/OCACS_2013_Housing_Characteristics_for_Urban_Areas/FeatureServer/1/query?outFields=*&where=1%3D1&f=geojson

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2013.4.12. Public Use Microdata Areas Housing Characteristics

- **Name**: OCACS2013PUH
- **Title**: OCACS 2013 Public Use Microdata Areas Selected Housing Characteristics
- **Tags**: geodemographics, Orange County, California, US Census, ACS, American Community Survey, Housing Characteristics, Public Use Microdata Areas, PUMA, housing occupancy, units, tenure, year built, rooms, bedrooms, vacancy status, vehicles, heating fuel, kitchen, plumbing, occupants, housing value, price asked, mortgage status, owner costs, rent value, gross rent
- **Summary**: Key housing characteristics of the 2013 American Community Survey (ACS), 5-year estimates for Public Use Microdata Areas (PUMA) in Orange County, California.
- **Description**: US Census American Community Survey (ACS) 2013, 5-year estimates of the key housing characteristics of Public Use Microdata Areas (PUMA) geographic level in Orange County, California. The data contains 406 fields for the variable groups H01: Housing occupancy (universe: total housing units, table X25, 3 fields); H02: Units in structure (universe: total housing units, table X25, 11 fields); H03: Population in occupied housing units by tenure by units in structure (universe: total population in occupied housing units, table X25, 13 fields); H04: Year structure built (universe: total housing units, table X25, 15 fields); H05: Rooms (universe: total housing units, table X25, 18 fields); H06: Bedrooms (universe: total housing units, table X25, 21 fields); H07: Housing tenure by race of householder (universe: occupied housing units, table X25, 51 fields); H08: Total population in occupied housing units by tenure (universe: total population in occupied housing units, table X25, 3 fields); H09: Vacancy status (universe: vacant housing units, table X25, 8 fields); H10: Occupied housing units by race of householder (universe: occupied housing units, table X25, 8 fields); H11: Year householder moved into unit (universe: occupied housing units, table X25, 18 fields); H12: Vehicles available (universe: occupied housing units, table X25, 18 fields); H13: Housing heating fuel (universe: occupied housing units, table X25, 10 fields); H14: Selected housing characteristics (universe: occupied housing units, table X25, 9 fields); H15: Occupants per room (universe: occupied housing units, table X25, 13 fields); H16: Housing value (universe: owner-occupied units, table X25, 32 fields); H17: Price asked for vacant for sale only, and sold not occupied housing units (universe: vacant for sale only, and sold not occupied housing units, table X25, 28 fields); H18: Mortgage status (universe: owner-occupied units, table X25, 10 fields); H19: Selected monthly owner costs, SMOC (universe: owner-occupied housing units with or without a mortgage, table X25, 45 fields); H20: Selected monthly owner costs as a percentage of household income, SMOCAPI (universe: owner-occupied housing units with or without a mortgage, table X25, 26 fields); H21: Contract rent distribution and rent asked distribution in dollars (universe: renter-occupied housing units paying cash rent and vacant, for rent, and rented not occupied housing units, table X25, 7 fields); H22: Gross rent (universe: occupied units paying rent, table X25, 28 fields), and; X23: Gross rent as percentage of household income (universe: occupied units paying rent, table X25, 11 fields). The US Census geodemographic data are based on the 2013 TigerLines across multiple geographies. The spatial geographies were merged with ACS data tables. See full documentation at the OCACS project github page (https://github.com/ktalexan/OCACS-Geodemographics).
- **Terms of Use**: Original datasets from US Census TigerLine Geography (https://www.census.gov/geo/maps-data/data/tiger-line.html), and American FactFinder (https://factfinder.census.gov/) for the selected tables of the American Community Survey (ACS, 2013). Linking and merging geographic with demographic tables along with final production of the merged spatial geodatabase and online datasets are performed by Orange County Public Works, OC Survey Geospatial Services, Dr. Kostas Alexandridis, GISP.
- **Map**: https://data-ocpw.opendata.arcgis.com/maps/ocacs-2013-housing-characteristics-for-public-use-microdata-areas
- **Web**: https://data-ocpw.opendata.arcgis.com/datasets/OCPW::ocacs-2013-housing-characteristics-for-public-use-microdata-areas/about
- **REST**: https://services.arcgis.com/UXmFoWC7yDHcDN5Q/arcgis/rest/services/OCACS_2013_Housing_Characteristics_for_Public_Use_Microdata_Areas/FeatureServer
- **Metadata**: https://www.arcgis.com/sharing/rest/content/items/e3c056d6834e4bf7a83c9a815f66f5ac/info/metadata/metadata.xml?format=default&output=html
- **GeoService API**: https://services.arcgis.com/UXmFoWC7yDHcDN5Q/arcgis/rest/services/OCACS_2013_Housing_Characteristics_for_Public_Use_Microdata_Areas/FeatureServer/1/query?outFields=*&where=1%3D1
- **GeoJSON API**: https://services.arcgis.com/UXmFoWC7yDHcDN5Q/arcgis/rest/services/OCACS_2013_Housing_Characteristics_for_Public_Use_Microdata_Areas/FeatureServer/1/query?outFields=*&where=1%3D1&f=geojson

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2013.4.13. Block Groups Housing Characteristics

- **Name**: OCACS2013BGH
- **Title**: OCACS 2013 Block Groups Selected Housing Characteristics
- **Tags**: geodemographics, Orange County, California, US Census, ACS, American Community Survey, Housing Characteristics, Block Groups, housing occupancy, units, tenure, year built, rooms, bedrooms, vacancy status, vehicles, heating fuel, kitchen, plumbing, occupants, housing value, price asked, mortgage status, owner costs, rent value, gross rent
- **Summary**: Key housing characteristics of the 2013 American Community Survey (ACS), 5-year estimates for Block Groups in Orange County, California.
- **Description**: US Census American Community Survey (ACS) 2013, 5-year estimates of the key housing characteristics of Block Groups geographic level in Orange County, California. The data contains 406 fields for the variable groups H01: Housing occupancy (universe: total housing units, table X25, 3 fields); H02: Units in structure (universe: total housing units, table X25, 11 fields); H03: Population in occupied housing units by tenure by units in structure (universe: total population in occupied housing units, table X25, 13 fields); H04: Year structure built (universe: total housing units, table X25, 15 fields); H05: Rooms (universe: total housing units, table X25, 18 fields); H06: Bedrooms (universe: total housing units, table X25, 21 fields); H07: Housing tenure by race of householder (universe: occupied housing units, table X25, 51 fields); H08: Total population in occupied housing units by tenure (universe: total population in occupied housing units, table X25, 3 fields); H09: Vacancy status (universe: vacant housing units, table X25, 8 fields); H10: Occupied housing units by race of householder (universe: occupied housing units, table X25, 8 fields); H11: Year householder moved into unit (universe: occupied housing units, table X25, 18 fields); H12: Vehicles available (universe: occupied housing units, table X25, 18 fields); H13: Housing heating fuel (universe: occupied housing units, table X25, 10 fields); H14: Selected housing characteristics (universe: occupied housing units, table X25, 9 fields); H15: Occupants per room (universe: occupied housing units, table X25, 13 fields); H16: Housing value (universe: owner-occupied units, table X25, 32 fields); H17: Price asked for vacant for sale only, and sold not occupied housing units (universe: vacant for sale only, and sold not occupied housing units, table X25, 28 fields); H18: Mortgage status (universe: owner-occupied units, table X25, 10 fields); H19: Selected monthly owner costs, SMOC (universe: owner-occupied housing units with or without a mortgage, table X25, 45 fields); H20: Selected monthly owner costs as a percentage of household income, SMOCAPI (universe: owner-occupied housing units with or without a mortgage, table X25, 26 fields); H21: Contract rent distribution and rent asked distribution in dollars (universe: renter-occupied housing units paying cash rent and vacant, for rent, and rented not occupied housing units, table X25, 7 fields); H22: Gross rent (universe: occupied units paying rent, table X25, 28 fields), and; X23: Gross rent as percentage of household income (universe: occupied units paying rent, table X25, 11 fields). The US Census geodemographic data are based on the 2013 TigerLines across multiple geographies. The spatial geographies were merged with ACS data tables. See full documentation at the OCACS project github page (https://github.com/ktalexan/OCACS-Geodemographics).
- **Terms of Use**: Original datasets from US Census TigerLine Geography (https://www.census.gov/geo/maps-data/data/tiger-line.html), and American FactFinder (https://factfinder.census.gov/) for the selected tables of the American Community Survey (ACS, 2013). Linking and merging geographic with demographic tables along with final production of the merged spatial geodatabase and online datasets are performed by Orange County Public Works, OC Survey Geospatial Services, Dr. Kostas Alexandridis, GISP.
- **Map**: https://data-ocpw.opendata.arcgis.com/maps/ocacs-2013-housing-characteristics-for-block-groups
- **Web**: https://data-ocpw.opendata.arcgis.com/datasets/OCPW::ocacs-2013-housing-characteristics-for-block-groups/about
- **REST**: https://services.arcgis.com/UXmFoWC7yDHcDN5Q/arcgis/rest/services/OCACS_2013_Housing_Characteristics_for_Block_Groups/FeatureServer
- **Metadata**: https://www.arcgis.com/sharing/rest/content/items/fdc6684cc8a4492b8945d096f68ec92f/info/metadata/metadata.xml?format=default&output=html
- **GeoService API**: https://services.arcgis.com/UXmFoWC7yDHcDN5Q/arcgis/rest/services/OCACS_2013_Housing_Characteristics_for_Block_Groups/FeatureServer/1/query?outFields=*&where=1%3D1
- **GeoJSON API**: https://services.arcgis.com/UXmFoWC7yDHcDN5Q/arcgis/rest/services/OCACS_2013_Housing_Characteristics_for_Block_Groups/FeatureServer/1/query?outFields=*&where=1%3D1&f=geojson

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2013.4.14. Census Tracts Housing Characteristics

- **Name**: OCACS2013TRH
- **Title**: OCACS 2013 Census Tracts Selected Housing Characteristics
- **Tags**: geodemographics, Orange County, California, US Census, ACS, American Community Survey, Housing Characteristics, Census Tracts, housing occupancy, units, tenure, year built, rooms, bedrooms, vacancy status, vehicles, heating fuel, kitchen, plumbing, occupants, housing value, price asked, mortgage status, owner costs, rent value, gross rent
- **Summary**: Key housing characteristics of the 2013 American Community Survey (ACS), 5-year estimates for Census Tracts in Orange County, California.
- **Description**: US Census American Community Survey (ACS) 2013, 5-year estimates of the key housing characteristics of Census Tracts geographic level in Orange County, California. The data contains 406 fields for the variable groups H01: Housing occupancy (universe: total housing units, table X25, 3 fields); H02: Units in structure (universe: total housing units, table X25, 11 fields); H03: Population in occupied housing units by tenure by units in structure (universe: total population in occupied housing units, table X25, 13 fields); H04: Year structure built (universe: total housing units, table X25, 15 fields); H05: Rooms (universe: total housing units, table X25, 18 fields); H06: Bedrooms (universe: total housing units, table X25, 21 fields); H07: Housing tenure by race of householder (universe: occupied housing units, table X25, 51 fields); H08: Total population in occupied housing units by tenure (universe: total population in occupied housing units, table X25, 3 fields); H09: Vacancy status (universe: vacant housing units, table X25, 8 fields); H10: Occupied housing units by race of householder (universe: occupied housing units, table X25, 8 fields); H11: Year householder moved into unit (universe: occupied housing units, table X25, 18 fields); H12: Vehicles available (universe: occupied housing units, table X25, 18 fields); H13: Housing heating fuel (universe: occupied housing units, table X25, 10 fields); H14: Selected housing characteristics (universe: occupied housing units, table X25, 9 fields); H15: Occupants per room (universe: occupied housing units, table X25, 13 fields); H16: Housing value (universe: owner-occupied units, table X25, 32 fields); H17: Price asked for vacant for sale only, and sold not occupied housing units (universe: vacant for sale only, and sold not occupied housing units, table X25, 28 fields); H18: Mortgage status (universe: owner-occupied units, table X25, 10 fields); H19: Selected monthly owner costs, SMOC (universe: owner-occupied housing units with or without a mortgage, table X25, 45 fields); H20: Selected monthly owner costs as a percentage of household income, SMOCAPI (universe: owner-occupied housing units with or without a mortgage, table X25, 26 fields); H21: Contract rent distribution and rent asked distribution in dollars (universe: renter-occupied housing units paying cash rent and vacant, for rent, and rented not occupied housing units, table X25, 7 fields); H22: Gross rent (universe: occupied units paying rent, table X25, 28 fields), and; X23: Gross rent as percentage of household income (universe: occupied units paying rent, table X25, 11 fields). The US Census geodemographic data are based on the 2013 TigerLines across multiple geographies. The spatial geographies were merged with ACS data tables. See full documentation at the OCACS project github page (https://github.com/ktalexan/OCACS-Geodemographics).
- **Terms of Use**: Original datasets from US Census TigerLine Geography (https://www.census.gov/geo/maps-data/data/tiger-line.html), and American FactFinder (https://factfinder.census.gov/) for the selected tables of the American Community Survey (ACS, 2013). Linking and merging geographic with demographic tables along with final production of the merged spatial geodatabase and online datasets are performed by Orange County Public Works, OC Survey Geospatial Services, Dr. Kostas Alexandridis, GISP.
- **Map**: https://data-ocpw.opendata.arcgis.com/maps/ocacs-2013-housing-characteristics-for-census-tracts
- **Web**: https://data-ocpw.opendata.arcgis.com/datasets/OCPW::ocacs-2013-housing-characteristics-for-census-tracts/about
- **REST**: https://services.arcgis.com/UXmFoWC7yDHcDN5Q/arcgis/rest/services/OCACS_2013_Housing_Characteristics_for_Census_Tracts/FeatureServer
- **Metadata**: https://www.arcgis.com/sharing/rest/content/items/0875a0151f8f4371ba20f3f5789f435b/info/metadata/metadata.xml?format=default&output=html
- **GeoService API**: https://services.arcgis.com/UXmFoWC7yDHcDN5Q/arcgis/rest/services/OCACS_2013_Housing_Characteristics_for_Census_Tracts/FeatureServer/1/query?outFields=*&where=1%3D1
- **GeoJSON API**: https://services.arcgis.com/UXmFoWC7yDHcDN5Q/arcgis/rest/services/OCACS_2013_Housing_Characteristics_for_Census_Tracts/FeatureServer/1/query?outFields=*&where=1%3D1&f=geojson

[<div align="right"><< Back to Contents</div>](#contents)

---
## Year: 2014
---
### 2014.1. Demographic Characteristics
---
> #### 2014.1.1. County Level Demographic Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2014.1.2. County Subdivision Demographic Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2014.1.3. Cities/Places Demographic Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2014.1.4. ZIP Code Tabulation Areas Demographic Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2014.1.5. Congressional Districts Demographic Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2014.1.6. State Assembly Legislative Districts Demographic Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2014.1.7. State Senate Legislative Districts Demographic Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2014.1.8. Elementary School Districts Demographic Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2014.1.9. Secondary School Districts Demographic Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2014.1.10. Unified School Districts Demographic Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2014.1.11. Urban Areas Demographic Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2014.1.12. Public Use Microdata Areas Demographic Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2014.1.13. Block Groups Demographic Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2014.1.14. Census Tracts Demographic Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

---
### 2014.2. Social Characteristics
---
> #### 2014.2.1. County Level Social Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2014.2.2. County Subdivision Social Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2014.2.3. Cities/Places Social Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2014.2.4. ZIP Code Tabulation Areas Social Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2014.2.5. Congressional Districts Social Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2014.2.6. State Assembly Legislative Districts Social Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2014.2.7. State Senate Legislative Districts Social Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2014.2.8. Elementary School Districts Social Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2014.2.9. Secondary School Districts Social Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2014.2.10. Unified School Districts Social Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2014.2.11. Urban Areas Social Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2014.2.12. Public Use Microdata Areas Social Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2014.2.13. Block Groups Social Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2014.2.14. Census Tracts Social Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

---
### 2014.3. Economic Characteristics
---
> #### 2014.3.1. County Level Economic Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2014.3.2. County Subdivision Economic Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2014.3.3. Cities/Places Economic Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2014.3.4. ZIP Code Tabulation Areas Economic Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2014.3.5. Congressional Districts Economic Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2014.3.6. State Assembly Legislative Districts Economic Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2014.3.7. State Senate Legislative Districts Economic Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2014.3.8. Elementary School Districts Economic Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2014.3.9. Secondary School Districts Economic Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2014.3.10. Unified School Districts Economic Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2014.3.11. Urban Areas Economic Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2014.3.12. Public Use Microdata Areas Economic Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2014.3.13. Block Groups Economic Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2014.3.14. Census Tracts Economic Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

---
### 2014.4. Housing Characteristics
---
> #### 2014.4.1. County Level Housing Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2014.4.2. County Subdivision Housing Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2014.4.3. Cities/Places Housing Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2014.4.4. ZIP Code Tabulation Areas Housing Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2014.4.5. Congressional Districts Housing Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2014.4.6. State Assembly Legislative Districts Housing Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2014.4.7. State Senate Legislative Districts Housing Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2014.4.8. Elementary School Districts Housing Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2014.4.9. Secondary School Districts Housing Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2014.4.10. Unified School Districts Housing Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2014.4.11. Urban Areas Housing Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2014.4.12. Public Use Microdata Areas Housing Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2014.4.13. Block Groups Housing Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2014.4.14. Census Tracts Housing Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)


---
## Year: 2015
---
### 2015.1. Demographic Characteristics
---
> #### 2015.1.1. County Level Demographic Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2015.1.2. County Subdivision Demographic Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2015.1.3. Cities/Places Demographic Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2015.1.4. ZIP Code Tabulation Areas Demographic Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2015.1.5. Congressional Districts Demographic Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2015.1.6. State Assembly Legislative Districts Demographic Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2015.1.7. State Senate Legislative Districts Demographic Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2015.1.8. Elementary School Districts Demographic Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2015.1.9. Secondary School Districts Demographic Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2015.1.10. Unified School Districts Demographic Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2015.1.11. Urban Areas Demographic Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2015.1.12. Public Use Microdata Areas Demographic Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2015.1.13. Block Groups Demographic Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2015.1.14. Census Tracts Demographic Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

---
### 2015.2. Social Characteristics
---
> #### 2015.2.1. County Level Social Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2015.2.2. County Subdivision Social Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2015.2.3. Cities/Places Social Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2015.2.4. ZIP Code Tabulation Areas Social Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2015.2.5. Congressional Districts Social Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2015.2.6. State Assembly Legislative Districts Social Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2015.2.7. State Senate Legislative Districts Social Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2015.2.8. Elementary School Districts Social Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2015.2.9. Secondary School Districts Social Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2015.2.10. Unified School Districts Social Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2015.2.11. Urban Areas Social Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2015.2.12. Public Use Microdata Areas Social Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2015.2.13. Block Groups Social Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2015.2.14. Census Tracts Social Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

---
### 2015.3. Economic Characteristics
---
> #### 2015.3.1. County Level Economic Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2015.3.2. County Subdivision Economic Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2015.3.3. Cities/Places Economic Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2015.3.4. ZIP Code Tabulation Areas Economic Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2015.3.5. Congressional Districts Economic Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2015.3.6. State Assembly Legislative Districts Economic Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2015.3.7. State Senate Legislative Districts Economic Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2015.3.8. Elementary School Districts Economic Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2015.3.9. Secondary School Districts Economic Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2015.3.10. Unified School Districts Economic Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2015.3.11. Urban Areas Economic Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2015.3.12. Public Use Microdata Areas Economic Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2015.3.13. Block Groups Economic Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2015.3.14. Census Tracts Economic Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

---
### 2015.4. Housing Characteristics
---
> #### 2015.4.1. County Level Housing Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2015.4.2. County Subdivision Housing Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2015.4.3. Cities/Places Housing Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2015.4.4. ZIP Code Tabulation Areas Housing Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2015.4.5. Congressional Districts Housing Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2015.4.6. State Assembly Legislative Districts Housing Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2015.4.7. State Senate Legislative Districts Housing Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2015.4.8. Elementary School Districts Housing Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2015.4.9. Secondary School Districts Housing Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2015.4.10. Unified School Districts Housing Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2015.4.11. Urban Areas Housing Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2015.4.12. Public Use Microdata Areas Housing Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2015.4.13. Block Groups Housing Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2015.4.14. Census Tracts Housing Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)


---
## Year: 2016
---
### 2016.1. Demographic Characteristics
---
> #### 2016.1.1. County Level Demographic Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2016.1.2. County Subdivision Demographic Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2016.1.3. Cities/Places Demographic Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2016.1.4. ZIP Code Tabulation Areas Demographic Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2016.1.5. Congressional Districts Demographic Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2016.1.6. State Assembly Legislative Districts Demographic Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2016.1.7. State Senate Legislative Districts Demographic Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2016.1.8. Elementary School Districts Demographic Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2016.1.9. Secondary School Districts Demographic Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2016.1.10. Unified School Districts Demographic Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2016.1.11. Urban Areas Demographic Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2016.1.12. Public Use Microdata Areas Demographic Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2016.1.13. Block Groups Demographic Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2016.1.14. Census Tracts Demographic Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

---
### 2016.2. Social Characteristics
---
> #### 2016.2.1. County Level Social Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2016.2.2. County Subdivision Social Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2016.2.3. Cities/Places Social Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2016.2.4. ZIP Code Tabulation Areas Social Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2016.2.5. Congressional Districts Social Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2016.2.6. State Assembly Legislative Districts Social Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2016.2.7. State Senate Legislative Districts Social Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2016.2.8. Elementary School Districts Social Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2016.2.9. Secondary School Districts Social Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2016.2.10. Unified School Districts Social Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2016.2.11. Urban Areas Social Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2016.2.12. Public Use Microdata Areas Social Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2016.2.13. Block Groups Social Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2016.2.14. Census Tracts Social Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

---
### 2016.3. Economic Characteristics
---
> #### 2016.3.1. County Level Economic Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2016.3.2. County Subdivision Economic Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2016.3.3. Cities/Places Economic Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2016.3.4. ZIP Code Tabulation Areas Economic Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2016.3.5. Congressional Districts Economic Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2016.3.6. State Assembly Legislative Districts Economic Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2016.3.7. State Senate Legislative Districts Economic Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2016.3.8. Elementary School Districts Economic Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2016.3.9. Secondary School Districts Economic Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2016.3.10. Unified School Districts Economic Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2016.3.11. Urban Areas Economic Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2016.3.12. Public Use Microdata Areas Economic Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2016.3.13. Block Groups Economic Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2016.3.14. Census Tracts Economic Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

---
### 2016.4. Housing Characteristics
---
> #### 2016.4.1. County Level Housing Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2016.4.2. County Subdivision Housing Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2016.4.3. Cities/Places Housing Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2016.4.4. ZIP Code Tabulation Areas Housing Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2016.4.5. Congressional Districts Housing Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2016.4.6. State Assembly Legislative Districts Housing Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2016.4.7. State Senate Legislative Districts Housing Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2016.4.8. Elementary School Districts Housing Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2016.4.9. Secondary School Districts Housing Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2016.4.10. Unified School Districts Housing Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2016.4.11. Urban Areas Housing Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2016.4.12. Public Use Microdata Areas Housing Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2016.4.13. Block Groups Housing Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2016.4.14. Census Tracts Housing Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)


---
## Year: 2017
---
### 2017.1. Demographic Characteristics
---
> #### 2017.1.1. County Level Demographic Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2017.1.2. County Subdivision Demographic Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2017.1.3. Cities/Places Demographic Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2017.1.4. ZIP Code Tabulation Areas Demographic Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2017.1.5. Congressional Districts Demographic Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2017.1.6. State Assembly Legislative Districts Demographic Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2017.1.7. State Senate Legislative Districts Demographic Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2017.1.8. Elementary School Districts Demographic Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2017.1.9. Secondary School Districts Demographic Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2017.1.10. Unified School Districts Demographic Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2017.1.11. Urban Areas Demographic Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2017.1.12. Public Use Microdata Areas Demographic Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2017.1.13. Block Groups Demographic Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2017.1.14. Census Tracts Demographic Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

---
### 2017.2. Social Characteristics
---
> #### 2017.2.1. County Level Social Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2017.2.2. County Subdivision Social Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2017.2.3. Cities/Places Social Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2017.2.4. ZIP Code Tabulation Areas Social Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2017.2.5. Congressional Districts Social Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2017.2.6. State Assembly Legislative Districts Social Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2017.2.7. State Senate Legislative Districts Social Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2017.2.8. Elementary School Districts Social Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2017.2.9. Secondary School Districts Social Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2017.2.10. Unified School Districts Social Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2017.2.11. Urban Areas Social Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2017.2.12. Public Use Microdata Areas Social Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2017.2.13. Block Groups Social Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2017.2.14. Census Tracts Social Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

---
### 2017.3. Economic Characteristics
---
> #### 2017.3.1. County Level Economic Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2017.3.2. County Subdivision Economic Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2017.3.3. Cities/Places Economic Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2017.3.4. ZIP Code Tabulation Areas Economic Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2017.3.5. Congressional Districts Economic Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2017.3.6. State Assembly Legislative Districts Economic Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2017.3.7. State Senate Legislative Districts Economic Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2017.3.8. Elementary School Districts Economic Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2017.3.9. Secondary School Districts Economic Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2017.3.10. Unified School Districts Economic Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2017.3.11. Urban Areas Economic Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2017.3.12. Public Use Microdata Areas Economic Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2017.3.13. Block Groups Economic Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2017.3.14. Census Tracts Economic Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

---
### 2017.4. Housing Characteristics
---
> #### 2017.4.1. County Level Housing Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2017.4.2. County Subdivision Housing Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2017.4.3. Cities/Places Housing Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2017.4.4. ZIP Code Tabulation Areas Housing Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2017.4.5. Congressional Districts Housing Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2017.4.6. State Assembly Legislative Districts Housing Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2017.4.7. State Senate Legislative Districts Housing Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2017.4.8. Elementary School Districts Housing Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2017.4.9. Secondary School Districts Housing Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2017.4.10. Unified School Districts Housing Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2017.4.11. Urban Areas Housing Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2017.4.12. Public Use Microdata Areas Housing Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2017.4.13. Block Groups Housing Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2017.4.14. Census Tracts Housing Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)



---
## Year: 2018
---
### 2018.1. Demographic Characteristics
---
> #### 2018.1.1. County Level Demographic Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2018.1.2. County Subdivision Demographic Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2018.1.3. Cities/Places Demographic Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2018.1.4. ZIP Code Tabulation Areas Demographic Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2018.1.5. Congressional Districts Demographic Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2018.1.6. State Assembly Legislative Districts Demographic Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2018.1.7. State Senate Legislative Districts Demographic Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2018.1.8. Elementary School Districts Demographic Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2018.1.9. Secondary School Districts Demographic Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2018.1.10. Unified School Districts Demographic Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2018.1.11. Urban Areas Demographic Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2018.1.12. Public Use Microdata Areas Demographic Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2018.1.13. Block Groups Demographic Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2018.1.14. Census Tracts Demographic Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

---
### 2018.2. Social Characteristics
---
> #### 2018.2.1. County Level Social Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2018.2.2. County Subdivision Social Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2018.2.3. Cities/Places Social Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2018.2.4. ZIP Code Tabulation Areas Social Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2018.2.5. Congressional Districts Social Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2018.2.6. State Assembly Legislative Districts Social Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2018.2.7. State Senate Legislative Districts Social Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2018.2.8. Elementary School Districts Social Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2018.2.9. Secondary School Districts Social Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2018.2.10. Unified School Districts Social Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2018.2.11. Urban Areas Social Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2018.2.12. Public Use Microdata Areas Social Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2018.2.13. Block Groups Social Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2018.2.14. Census Tracts Social Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

---
### 2018.3. Economic Characteristics
---
> #### 2018.3.1. County Level Economic Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2018.3.2. County Subdivision Economic Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2018.3.3. Cities/Places Economic Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2018.3.4. ZIP Code Tabulation Areas Economic Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2018.3.5. Congressional Districts Economic Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2018.3.6. State Assembly Legislative Districts Economic Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2018.3.7. State Senate Legislative Districts Economic Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2018.3.8. Elementary School Districts Economic Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2018.3.9. Secondary School Districts Economic Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2018.3.10. Unified School Districts Economic Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2018.3.11. Urban Areas Economic Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2018.3.12. Public Use Microdata Areas Economic Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2018.3.13. Block Groups Economic Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2018.3.14. Census Tracts Economic Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

---
### 2018.4. Housing Characteristics
---
> #### 2018.4.1. County Level Housing Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2018.4.2. County Subdivision Housing Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2018.4.3. Cities/Places Housing Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2018.4.4. ZIP Code Tabulation Areas Housing Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2018.4.5. Congressional Districts Housing Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2018.4.6. State Assembly Legislative Districts Housing Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2018.4.7. State Senate Legislative Districts Housing Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2018.4.8. Elementary School Districts Housing Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2018.4.9. Secondary School Districts Housing Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2018.4.10. Unified School Districts Housing Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2018.4.11. Urban Areas Housing Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2018.4.12. Public Use Microdata Areas Housing Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2018.4.13. Block Groups Housing Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2018.4.14. Census Tracts Housing Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)


---
## Year: 2019
---
### 2019.1. Demographic Characteristics
---
> #### 2019.1.1. County Level Demographic Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2019.1.2. County Subdivision Demographic Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2019.1.3. Cities/Places Demographic Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2019.1.4. ZIP Code Tabulation Areas Demographic Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2019.1.5. Congressional Districts Demographic Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2019.1.6. State Assembly Legislative Districts Demographic Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2019.1.7. State Senate Legislative Districts Demographic Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2019.1.8. Elementary School Districts Demographic Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2019.1.9. Secondary School Districts Demographic Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2019.1.10. Unified School Districts Demographic Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2019.1.11. Urban Areas Demographic Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2019.1.12. Public Use Microdata Areas Demographic Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2019.1.13. Block Groups Demographic Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2019.1.14. Census Tracts Demographic Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

---
### 2019.2. Social Characteristics
---
> #### 2019.2.1. County Level Social Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2019.2.2. County Subdivision Social Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2019.2.3. Cities/Places Social Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2019.2.4. ZIP Code Tabulation Areas Social Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2019.2.5. Congressional Districts Social Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2019.2.6. State Assembly Legislative Districts Social Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2019.2.7. State Senate Legislative Districts Social Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2019.2.8. Elementary School Districts Social Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2019.2.9. Secondary School Districts Social Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2019.2.10. Unified School Districts Social Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2019.2.11. Urban Areas Social Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2019.2.12. Public Use Microdata Areas Social Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2019.2.13. Block Groups Social Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2019.2.14. Census Tracts Social Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

---
### 2019.3. Economic Characteristics
---
> #### 2019.3.1. County Level Economic Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2019.3.2. County Subdivision Economic Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2019.3.3. Cities/Places Economic Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2019.3.4. ZIP Code Tabulation Areas Economic Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2019.3.5. Congressional Districts Economic Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2019.3.6. State Assembly Legislative Districts Economic Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2019.3.7. State Senate Legislative Districts Economic Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2019.3.8. Elementary School Districts Economic Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2019.3.9. Secondary School Districts Economic Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2019.3.10. Unified School Districts Economic Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2019.3.11. Urban Areas Economic Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2019.3.12. Public Use Microdata Areas Economic Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2019.3.13. Block Groups Economic Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2019.3.14. Census Tracts Economic Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

---
### 2019.4. Housing Characteristics
---
> #### 2019.4.1. County Level Housing Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2019.4.2. County Subdivision Housing Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2019.4.3. Cities/Places Housing Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2019.4.4. ZIP Code Tabulation Areas Housing Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2019.4.5. Congressional Districts Housing Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2019.4.6. State Assembly Legislative Districts Housing Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2019.4.7. State Senate Legislative Districts Housing Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2019.4.8. Elementary School Districts Housing Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2019.4.9. Secondary School Districts Housing Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2019.4.10. Unified School Districts Housing Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2019.4.11. Urban Areas Housing Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2019.4.12. Public Use Microdata Areas Housing Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2019.4.13. Block Groups Housing Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

> #### 2019.4.14. Census Tracts Housing Characteristics

- **Name**: 
- **Title**: 
- **Tags**: 
- **Summary**: 
- **Description**: 
- **Terms of Use**: 
- **Map**: 
- **Web**: 
- **REST**: 
- **Metadata**: 
- **GeoService API**: 
- **GeoJSON API**: 

[<div align="right"><< Back to Contents</div>](#contents)

