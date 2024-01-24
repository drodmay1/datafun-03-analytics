Temperature, ozone, and PM2.5 data for "Associations Between Simulated 
Future Changes in Climate, Air Quality, and Human Health" by Fann et 
al., 2021.

These data are output from the Community Multiscale Air Quality (CMAQ) model,
version 5.3.  See www.epa.gov/cmaq for information about CMAQ and how to 
download it.

The meteorological input data for CMAQ were derived from outputs of the
Community Earth System Model (CESM) and the Coupled Model version 3
(CM3) following Representative Concentration Pathway (RCP) 8.5, which
represents a relatively high warming scenario.  The CESM and CM3 fields
were downscaled to 36-km grid cells over North America using the Weather
Research and Forecasting model version 3.4.1. The downscaling and air
quality modeling procedure are described in Spero et al. (2016) and
Nolte et al. (2018).

CMAQ simulations were conducted using the meteorology downscaled from
the two climate models and using two different sets of anthropogenic
emissions: the 2011 National Emission Inventory and a 2040 projection
developed for analysis of the Heavy Duty Greenhouse Gas Rule. This 2040
projection represents significant reductions relative to present-day of
pollutant emissions, including nitrogen oxides (NOx), sulfur dioxide,
and volatile organic compounds (VOCs). See U.S. EPA (2016) for further
information on the anthropogenic emissions. Climate-sensitive VOCs
emitted from vegetation, e.g., isoprene, were modeled within CMAQ using
the downscaled meteorological projections from WRF. 

Nolte CG, Spero TL, Bowden JH, Mallard MS, Dolwick PD (2018), The
potential effects of climate change on air quality across the
conterminous US at 2030 under three Representative Concentration
Pathways, Atmos. Chem. Phys., 18, 15471-15489, doi:10.5194/acp-18-15471-
2018.

Spero TL, Nolte CG, Bowden JH, Mallard MS, Herwehe JA (2016), The impact of
incongruous lake temperatures on regional climate extremes downscaled from
the CMIP5 archive using the WRF model, J. Clim., 29, 839-853, 
doi:10.1175/JCLI-D-15-0233.1.

U.S. EPA (2016), Emissions Inventory for Air Quality Modeling Technical
Support Document: Heavy-Duty Vehicle Greenhouse Gase Phase 2 Final Rule,
U.S. Environmental Protection Agency, EPA 420-R-16-008.

Dataset manifest
README.txt (this file)
  grid.csv - contains latitude (degrees_N) and longitude (degrees_E) for the
             center of the indicated grid cell, as indexed by the cell column 
             and row.  The modeling domain is a 148x110 Lambert conformal 
             grid, with each grid cell 36x36 km in size. 

  cesm_t2max_o3.csv - Contains surface-layer maximum daily temperature 
             (Kelvin) downscaled from CESM and maximum daily 8-h average 
             ozone mixing ratios (parts per billion by volume, ppb) modeled 
             using the CESM meteorology for each indicated grid cell for 
             the indicated modeling periods.
             Each modeling period is 11 years, with the indicated year 
             representing the midpoint, i.e., "2000" represents 1995-2005
             and "2095" represents 2090-2100. 
             Data are averaged over the May-September ozone season.

   cm3_t2max_o3.csv - As above, except for meteorology downscaled from CM3.
   
   cesm_t2mean_pm.csv - As above, except contains annual average 
             temperature (Kelvin) from the CESM model and annual average 
             PM2.5 concentrations (micrograms per cubic meter) modeled
             by CMAQ using the CESM meteorology.
             
   cm3_t2mean_pm.csv - As above, except for meteorology downscaled from CM3.


These data provided to Neal Fann (EPA, Office of Air and Radiation, Office of 
Air Quality Planning and Standards) for health impacts analysis using the
Benefits Mapping and Analysis Program-Community Edition (BenMAP-CE) tool.


This file prepared by:
Christopher G. Nolte
Office of Research and Development
U.S. Environmental Protection Agency
nolte.chris@epa.gov
20 March 2020
