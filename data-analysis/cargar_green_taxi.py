import pandas as pd
from sqlalchemy import create_engine
import time

def cargar_datos():
    # 1. Configuración de la conexión
    # IMPORTANTE: Usamos localhost:5433 porque el script corre en el host de IDX
    # apuntando al puerto que mapeaste en el docker-compose.yaml
    conn_string = 'postgresql://postgres:postgres@localhost:5433/ny_taxi'
    engine = create_engine(conn_string)

    file_name = 'green_tripdata_2025-11.parquet'
    table_name = 'green_taxi_data'

    print(f"Leyendo archivo {file_name}...")
    
    try:
        # 2. Cargar el DataFrame
        df = pd.read_parquet(file_name)
        
        # 3. Mostrar información básica
        print(f"Columnas detectadas: {df.columns.tolist()}")
        print(f"Total de filas a cargar: {len(df)}")

        # 4. Inserción en la base de datos
        start_time = time.time()
        print("Iniciando la carga en Postgres (esto puede tardar unos segundos)...")
        
        # Usamos chunksize si el archivo es muy grande para no saturar la memoria
        df.to_sql(name=table_name, con=engine, if_exists='replace', index=False)
        
        end_time = time.time()
        print(f"¡Éxito! Datos cargados en {end_time - start_time:.2f} segundos.")

    except Exception as e:
        print(f"Error durante la carga: {e}")

if __name__ == "__main__":
    cargar_datos()