# wind-power-correlations

Looking at how wind power correlates with the NAO index and North Sea/Central Europe wind speeds both onshore and offshore over Europe.

For the wind power data we are using the datasets from Bloomfield and Brayshaw (2021): ERA5 derived time series of European aggregated surface weather variables ... (doi: https://doi.org/10.17864/1947.000321).

For observations/reanalysis we are using the ERA5 dataset (at monthly average resolution).

For the model data, we are using the dcppA-hindcast experiments in a multi-model ensemble set-up, where an equally weighted average of the ensemble members is taken.

The research question(s) for this are as follows:

* Can a decadal forecast for wind power capacity over a specific region (e.g. UK East Coast shipping zones) show skill?
* Does this skill come from gridpoint methods (i.e. using sfcWinds) or by using pattern based forecasting measures (such as the NAO index)?

1. First, we will look at the correlations between the year 2-9 average DJFM (and other seasons) sfcWind speeds in the North Sea box (from ERA5) and the 8 year running mean DJFM (and other seasons) offshore wind power capacity factors for a selection of the Met Office shipping zones off the East Coast of the UK.

2. Second, we will look at the correlations between the year 2-9 NAO index for DJFM (and other seasons) over the North Atlantic (from ERA5) and the the 8 year running mean DJFM (and other seasons) offshore wind power capacity factors for a selection of the Met Office shipping zones off the East Coast of the UK.

3. Third, we will do the same as the first experiment, but using the dcppA-hindcast data for the sfcWind speeds.

4. Fourth, we will do the same as the second experiment, but using the dcppA-hindcast data for the NAO anomalies.

5. Fifth, we will quantify a regression relationship between the observed offshore wind power capacity for the selected shipping zones and the dcppA-hindcast sfcWind speeds. We can then use this relationship to construct a retrospective decadal forecast of offhore wind power capacity for the region by using this relationship combined with the dcppA-hindcast sfcWind data.

6. Sixth, we will quantify a regression relationship between the observed offshore wind power capacity for the selected shipping zones and the dcppA-hindcast NAO index. We can then use this relationship to construct a retrospective decadal forecast of offhore wind power capacity for the region by using this relationship combined with the dcppA-hindcast NAO anomaly data.

