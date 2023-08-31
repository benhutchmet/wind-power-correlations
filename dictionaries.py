# import modules
import os

# Shipping zones for the UK offshore wind power
# Which we will use to aggregate the data for offshore wind power capacity factors
shipping_zones_uk_e_coast = []


# base directory for the CLEARHEADS data
ch_base_dir = "/home/users/benhutch/CLEARHEADS_EU_Power_Data"


# Path to the uk offshore wind power data
# Shipping_zones_United_Kingdom_wp_ofs_historical.nc
ch_uk_offshore_wind_power = os.path.join(ch_base_dir, "Shipping_zones_United_Kingdom_wp_ofs_historical.nc")