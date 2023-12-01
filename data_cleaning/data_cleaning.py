import geopandas as gpd


def clean_restaurant_data():
    # I had to delete this file after filtering it because it was too big for GitHub
    file_path = './assets/Restaurant_Inspections___restaurant_inspections_point.geojson'
    df = gpd.read_file(file_path)
    df = df[(df['CITY'] == 'Seattle') &
            (df['DATE_INSPECTION'].astype(str).str[:4] == '2023')]
    df = df.drop(columns=['RECORD_ID', 'FACILITY_NAME', 'CHAIN_NAME',
                 'CHAIN_ESTABLISHMENT', 'SITE_ADDRESS'])
    df.to_file('./assets/Cleaned_Restaurant_Inspections.geojson',
               driver='GeoJSON')


def main():
    clean_restaurant_data()


if __name__ == '__main__':
    main()