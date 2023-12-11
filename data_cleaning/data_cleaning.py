import geopandas as gpd


# Does the initial cleaning
def clean_restaurant_data():
    # I had to delete this file after filtering it because it was too big for GitHub
    # The file can be found here: https://gis-kingcounty.opendata.arcgis.com/datasets/kingcounty::restaurant-inspections-restaurant-inspections-point/explore?location=47.449024%2C-121.952400%2C10.87
    file_path = './assets/Restaurant_Inspections___restaurant_inspections_point.geojson'
    df = gpd.read_file(file_path)
    df = df[(df['CITY'] == 'Seattle') &
            (df['DATE_INSPECTION'].astype(str).str[:4] == '2023')]
    df = df.drop(columns=['RECORD_ID', 'FACILITY_NAME', 'CHAIN_NAME',
                 'CHAIN_ESTABLISHMENT', 'SITE_ADDRESS'])
    df.to_file('./assets/Cleaned_Restaurant_Inspections.geojson',
               driver='GeoJSON')


# Gets rid of duplicated restaurants
def get_rid_duplicates():
    file_path = './assets/Cleaned_Restaurant_Inspections.geojson'
    df = gpd.read_file(file_path)
    duplicate_mask = df['NAME'].duplicated(keep='first')
    df = df[~duplicate_mask]
    df.to_file('./assets/Cleaned_Restaurant_Inspections_No_Dupes.geojson',
               driver='GeoJSON')



def main():
    # clean_restaurant_data()
    get_rid_duplicates()


if __name__ == '__main__':
    main()