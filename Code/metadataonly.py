import os, arcpy
from arcpy import metadata as md

def ocacs_metadata(prjPath):
    """_summary_
    OCACS Python Class for Metadata Only

    Args:
        prjPath (_type_): _description_
    """
    
    # Obtain the Data folders in the project directory
    dataIn = os.path.join(prjPath, "Original")
    dataOut = os.path.join(prjPath, "Processed")
    
    # Set and obtain the workspaces (geodatabases) in the folder
    arcpy.env.workspace = dataOut
    workspaces = arcpy.ListWorkspaces("*", "FileGDB")
    
    # Get the year
    year = int(os.path.split(prjPath)[1].split("OCACS")[1])
    
    # Obtain the geodatabase list (no path)
    gdbListIn = [os.path.split(w)[1] for w in workspaces]
    
    # Geodatabase Metadata Template
    metadataTemplate = {
        "D": {
            "Characteristic": "Demographic Characteristics",
            "Title": "OCACS {year} Geodatabase Selected Demographic Characteristics",
            "Tags": "geodemographics, Orange County, California, US Census, ACS, American Community Survey, Demographic Characteristics, Orange County, County Subdivisions, Cities, ZIP Code Tabulation Areas, Congressional Districts, State Assembly Legislative Districts, State Senate Legislative Districts, Elementary Education Districts, Secondary Education Districts, Unified Education Districts, Urban Areas, PUMA, Census Tracts, Block Groups, age, sex, race, Hispanic or Latino, citizen, voting",
            "Summary": "Key demographic characteristics of the {year} American Community Survey (ACS), 5-year estimates for multiple geography levels in Orange County, California.",
            "Description": "US Census American Community Survey (ACS) {year}, 5-year estimates of the key demographic characteristics of multiple geographic levels (county; county subdivisions; cities; ZIP codes; congressional, state assembly and state senate districts; elementary, secondary and unified educational districts; urban areas, PUMA, census tracts and block groups) for Orange County, California. The data contains 105 fields for the variable groups D01: Sex and age (universe: total population, table X1, 49 fields); D02: Median age by sex and race (universe: total population, table X1, 12 fields); D03: Race (universe: total population, table X2, 8 fields); D04: Race alone or in combination with one or more other races (universe: total population, table X2, 7 fields); D05: Hispanic or Latino and race (universe: total population, table X3, 21 fields), and; D06: Citizen voting age population (universe: citizen, 18 and over, table X5, 8 fields). The US Census geodemographic data are based on the {year} TigerLines across multiple geographies. The spatial geographies were merged with ACS data tables. See full documentation at the OCACS project github page (https://github.com/ktalexan/OCACS-Geodemographics).",
            "Credits": "Original datasets from US Census TigerLine Geography (https://www.census.gov/geo/maps-data/data/tiger-line.html), and American FactFinder (https://factfinder.census.gov/) for the selected tables of the American Community Survey (ACS, {year}). Linking and merging geographic with demographic tables along with final production of the merged spatial geodatabase and online datasets are performed by Orange County Public Works, OC Survey Geospatial Services, Dr. Kostas Alexandridis, GISP.",
            "Thumbnail": "https://github.com/ktalexan/OCACS-Geodemographics/blob/main/Images/OCDemographicCharacteristics.jpg?raw=true"
        },
        "S": {
            "Characteristic": "Social Characteristics",
            "Title": "OCACS {year} Geodatabase Selected Social Characteristics",
            "Tags": "geodemographics, Orange County, California, US Census, ACS, American Community Survey, Social Characteristics, Orange County, County Subdivisions, Cities, ZIP Code Tabulation Areas, Congressional Districts, State Assembly Legislative Districts, State Senate Legislative Districts, Elementary Education Districts, Secondary Education Districts, Unified Education Districts, Urban Areas, PUMA, Census Tracts, Block Groups, households, relationship, marital status, Fertility, grandparents, school enrollment, educational attainment, veteran status, disability, residence, place of birth, citizenship, region of birth, language spoken, ancestry, computer use, internet use",
            "Summary": "Key social characteristics of the {year} American Community Survey (ACS), 5-year estimates for multiple geography levels in Orange County, California.",
            "Description": "US Census American Community Survey (ACS) {year}, 5-year estimates of the key social characteristics of multiple geographic levels (county; county subdivisions; cities; ZIP codes; congressional, state assembly and state senate districts; elementary, secondary and unified educational districts; urban areas, PUMA, census tracts and block groups) for Orange County, California. The data contains 500 fields for the variable groups S01: Households by type (universe: total households, table X11, 17 fields); S02: Relationship (universe: population in households, table X9, 19 fields); S03: Marital status (universe: population 15 years and over, table X12, 13 fields); S04: Fertility (universe: women 15-50 years who had birth in the past 12 months, table X13, 11 fields); S05: Grandparents (universe: grandparents living or responsible for own grandchildren under 18 years, table X10, 18 fields); S06: School enrollment (universe: population 3 years old and over enrolled in school, table X14, 17 fields); S07: Educational attainment (universe: population 25 years and over, table X15, 25 fields); S08: Veteran status (universe: civilian population 18 years and over, table X21, 2 fields); S09: Disability status and type by sex and age (universe: total civilian non-institutionalized population, table X18, 77 fields); S10: Disability status by age and health insurance coverage (universe: civilian non-institutionalized population, table X18, 16 fields); S11: Residence 1 year ago (universe: population 1 year and over, table X7, 6 fields); S12: Place of birth (universe: total population, table X5, 27 fields); S13: Citizenship status by nativity in the US (universe: total population, table X5, 6 fields); S14: Year of entry (universe: population born outside the US, table X5, 21 fields); S15: World region of birth of foreign born population (universe: foreign born population, excluding population born at sea, table X5, 25 fields); S16: Language spoken in households (universe: total households, table X16, 6 fields); S17: Language spoken at home (universe: population 5 years and over, table X16, 67 fields); S18: Ancestry (universe: total population reporting ancestry, table X4, 114 fields), and; S19: Computers and internet use (universe: total population in households and total households, table X28, 13 fields). The US Census geodemographic data are based on the {year} TigerLines across multiple geographies. The spatial geographies were merged with ACS data tables. See full documentation at the OCACS project GitHub page (https://github.com/ktalexan/OCACS-Geodemographics).",
            "Credits": "Original datasets from US Census TigerLine Geography (https://www.census.gov/geo/maps-data/data/tiger-line.html), and American FactFinder (https://factfinder.census.gov/) for the selected tables of the American Community Survey (ACS, {year}). Linking and merging geographic with demographic tables along with final production of the merged spatial geodatabase and online datasets are performed by Orange County Public Works, OC Survey Geospatial Services, Dr. Kostas Alexandridis, GISP.",
            "Thumbnail": "https://github.com/ktalexan/OCACS-Geodemographics/blob/main/Images/OCSocialCharacteristics.jpg?raw=true"
        },
        "E": {
            "Characteristic": "Economic Characteristics",
            "Title": "OCACS {year} Geodatabase Selected Economic Characteristics",
            "Tags": "geodemographics, Orange County, California, US Census, ACS, American Community Survey, Economic Characteristics, Orange County, County Subdivisions, Cities, ZIP Code Tabulation Areas, Congressional Districts, State Assembly Legislative Districts, State Senate Legislative Districts, Elementary Education Districts, Secondary Education Districts, Unified Education Districts, Urban Areas, PUMA, Census Tracts, Block Groups, employment status, work status, worker, commuting, travel time, vehicles, transportation, occupation, industry, class of worker, income, earnings, health insurance, poverty",
            "Summary": "Key economic characteristics of the {year} American Community Survey (ACS), 5-year estimates for multiple geography levels in Orange County, California.",
            "Description": "US Census American Community Survey (ACS) {year}, 5-year estimates of the key economic characteristics of multiple geographic levels (county; county subdivisions; cities; ZIP codes; congressional, state assembly and state senate districts; elementary, secondary and unified educational districts; urban areas, PUMA, census tracts and block groups) for Orange County, California. The data contains 397 fields for the variable groups E01: Employment status (universe: population 16 years and over, table X23, 7 fields); E02: Work status by age of worker (universe: population 16 years and over, table X23, 36 fields); E03: Commuting to work (universe: workers 16 years and over, table X8, 8 fields); E04: Travel time to work (universe: workers 16 years and over who did not work at home, table X8, 14 fields); E05: Number of vehicles available for workers (universe: workers 16 years and over in households, table X8, 8 fields); E06: Median age by means of transportation to work (universe: median age, workers 16 years and over, table X8, 7 fields); E07: Means of transportation to work by race (universe: workers 16 years and over, table X8, 64 fields); E08: Occupation (universe: civilian employed population 16 years and over, table X24, 53 fields); E09: Industry (universe: civilian employed population 16 years and over, table X24, 43 fields); E10: Class of worker (universe: civilian employed population 16 years and over, table X24, 19 fields); E11: Household income and earnings in the past 12 months (universe: total households, table X19, 37 fields); E12: Income and earnings in dollars (universe: inflation-adjusted dollars, tables X19-X20, 31 fields); E13: Family income in dollars (universe: total families, table X19, 17 fields); E14: Health insurance coverage (universe: total families, table X19, 17 fields); E15: Ratio of income to Poverty level (universe: total population for whom Poverty level is determined, table X17,  8 fields); E16: Poverty in population in the past 12 months (universe: total population for whom Poverty level is determined, table X17, 7 fields); E17: Poverty in households in the past 12 months (universe: total households, table X17, 9 fields); E18: Percentage of families and people whose income in the past 12 months is below the poverty level (universe: families, population, table X17, 8 fields), and; X19: Poverty and income deficit (dollars) in the past 12 months for families (universe: families with income below Poverty level in the past 12 months, table X17, 4 fields). The US Census geodemographic data are based on the {year} TigerLines across multiple geographies. The spatial geographies were merged with ACS data tables. See full documentation at the OCACS project GitHub page (https://github.com/ktalexan/OCACS-Geodemographics).",
            "Credits": "Original datasets from US Census TigerLine Geography (https://www.census.gov/geo/maps-data/data/tiger-line.html), and American FactFinder (https://factfinder.census.gov/) for the selected tables of the American Community Survey (ACS, {year}). Linking and merging geographic with demographic tables along with final production of the merged spatial geodatabase and online datasets are performed by Orange County Public Works, OC Survey Geospatial Services, Dr. Kostas Alexandridis, GISP.",
            "Thumbnail": "https://github.com/ktalexan/OCACS-Geodemographics/blob/main/Images/OCEconomicCharacteristics.jpg?raw=true"
        },
        "H": {
            "Characteristic": "Housing Characteristics",
            "Title": "OCACS {year} Geodatabase Selected Housing Characteristics",
            "Tags": "geodemographics, Orange County, California, US Census, ACS, American Community Survey, Housing Characteristics, Orange County, County Subdivisions, Cities, ZIP Code Tabulation Areas, Congressional Districts, State Assembly Legislative Districts, State Senate Legislative Districts, Elementary Education Districts, Secondary Education Districts, Unified Education Districts, Urban Areas, PUMA, Census Tracts, Block Groups, housing occupancy, units, tenure, year built, rooms, bedrooms, vacancy status, vehicles, heating fuel, kitchen, plumbing, occupants, housing value, price asked, mortgage status, owner costs, rent value, gross rent",
            "Summary": "Key housing characteristics of the {year} American Community Survey (ACS), 5-year estimates for multiple geography levels in Orange County, California.",
            "Description": "US Census American Community Survey (ACS) {year}, 5-year estimates of the key housing characteristics of multiple geographic levels (county; county subdivisions; cities; ZIP codes; congressional, state assembly and state senate districts; elementary, secondary and unified educational districts; urban areas, PUMA, census tracts and block groups) for Orange County, California. The data contains 406 fields for the variable groups H01: Housing occupancy (universe: total housing units, table X25, 3 fields); H02: Units in structure (universe: total housing units, table X25, 11 fields); H03: Population in occupied housing units by tenure by units in structure (universe: total population in occupied housing units, table X25, 13 fields); H04: Year structure built (universe: total housing units, table X25, 15 fields); H05: Rooms (universe: total housing units, table X25, 18 fields); H06: Bedrooms (universe: total housing units, table X25, 21 fields); H07: Housing tenure by race of householder (universe: occupied housing units, table X25, 51 fields); H08: Total population in occupied housing units by tenure (universe: total population in occupied housing units, table X25, 3 fields); H09: Vacancy status (universe: vacant housing units, table X25, 8 fields); H10: Occupied housing units by race of householder (universe: occupied housing units, table X25, 8 fields); H11: Year householder moved into unit (universe: occupied housing units, table X25, 18 fields); H12: Vehicles available (universe: occupied housing units, table X25, 18 fields); H13: Housing heating fuel (universe: occupied housing units, table X25, 10 fields); H14: Selected housing characteristics (universe: occupied housing units, table X25, 9 fields); H15: Occupants per room (universe: occupied housing units, table X25, 13 fields); H16: Housing value (universe: owner-occupied units, table X25, 32 fields); H17: Price asked for vacant for sale only, and sold not occupied housing units (universe: vacant for sale only, and sold not occupied housing units, table X25, 28 fields); H18: Mortgage status (universe: owner-occupied units, table X25, 10 fields); H19: Selected monthly owner costs, SMOC (universe: owner-occupied housing units with or without a mortgage, table X25, 45 fields); H20: Selected monthly owner costs as a percentage of household income, SMOCAPI (universe: owner-occupied housing units with or without a mortgage, table X25, 26 fields); H21: Contract rent distribution and rent asked distribution in dollars (universe: renter-occupied housing units paying cash rent and vacant, for rent, and rented not occupied housing units, table X25, 7 fields); H22: Gross rent (universe: occupied units paying rent, table X25, 28 fields), and; X23: Gross rent as percentage of household income (universe: occupied units paying rent, table X25, 11 fields). The US Census geodemographic data are based on the {year} TigerLines across multiple geographies. The spatial geographies were merged with ACS data tables. See full documentation at the OCACS project GitHub page (https://github.com/ktalexan/OCACS-Geodemographics).",
            "Credits": "Original datasets from US Census TigerLine Geography (https://www.census.gov/geo/maps-data/data/tiger-line.html), and American FactFinder (https://factfinder.census.gov/) for the selected tables of the American Community Survey (ACS, 2021). Linking and merging geographic with demographic tables along with final production of the merged spatial geodatabase and online datasets are performed by Orange County Public Works, OC Survey Geospatial Services, Dr. Kostas Alexandridis, GISP.",
            "Thumbnail": "https://github.com/ktalexan/OCACS-Geodemographics/blob/main/Images/OCHousingCharacteristics.jpg?raw=true"
        }
    }
    
    # Format the metadata from the template
    metadataList = {}
    for w in workspaces:
        f = os.path.split[w][1]
        c = f.split(".gdb")[0].split(f"OCACS{year}")[1]
        metadataList[c] = {
            "Path": w,
            "Name": f.split(".gdb")[0],
            "Year": year,
            "Characteristic": metadataTemplate[c]["Characteristic"],
            "Title": metadataTemplate[c].format(year = year),
            "Tags": metadataTemplate[c]["Tags"],
            "Summary": metadataTemplate[c]["Summary"].format(year = year),
            "Description": metadataTemplate[c]["Description"].format(year = year),
            "Credits": metadataTemplate[c]["Credits"].format(year = year),
            "Thumbnail": metadataTemplate[c]["Thumbnail"].format(prjPath = prjPath)
            }
    
    
    # Assign metadata
    for key in metadataList.keys():
        metadataItems = md.Metadata()
        metadataItems.title = metadataList[key]["Title"]
        metadataItems.tags = metadataList[key]["Tags"]
        metadataItems.summary = metadataList[key]["Summary"]
        metadataItems.description = metadataList[key]["Description"]
        metadataItems.credits = metadataList[key]["Credits"]
        metadataItems.accessConstraints = metadataList[key]["Credits"]
        metadataItems.thumbnailUri = metadataList["Thumbnail"]
        metadataTarget = md.Metadata(metadataList[key]["Path"])
        if not metadataTarget.isReadOnly:
            metadataTarget.copy(metadata)
            metadataTarget.save()
        elif metadataTarget.isReadOnly:
            print(f"{metadataList[key]['Name']} is Read Only...")
    
    