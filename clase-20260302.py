from pandas import DataFrame
import pandas as pd

def main() -> None:
    """air_quality_data: DataFrame = pd.read_csv(filepath_or_buffer="00-raw-data/calidad-aire/contaminantes_2024_sample.csv", skiprows=9)
    

#Para poder modificar datos dentro de un csv, necesitamos saber como acceder a culumnas y como cambiarlos
#Cambia la columna a categorica, pero crea una nueva variable, buscamos sustituir esta nueva columna 
    air_quality_data['id_station']=air_quality_data['id_station'].astype('category')  

    air_quality_data['date'] = pd.to_datetime(air_quality_data['date'], format='ISO8601')"""

    dtypes= {
        "id_station": "category",
        "id_parameter": "category",
        "value": "float32", 
        "unit": "uint8"
    } 


    air_quality_data: DataFrame= pd.read_csv(
        filepath_or_buffer="00-raw-data/calidad-aire/contaminantes_2024_sample.csv",
        dtype=dtypes,
        parse_dates=['date'],
        skiprows=9
    
        )



    print(air_quality_data.info())   #Que tipo de valores tengo, valores nulos, cuantos son, memoria
    print(air_quality_data.head())   #Nos muestran los priemros 5 lineas del csv


if __name__ == "__main__":
    main()
