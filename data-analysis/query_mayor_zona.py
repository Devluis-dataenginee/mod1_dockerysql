import pandas as pd
from sqlalchemy import create_engine

def resolver_pregunta_5():
    try:
        # 1. Conexión a la base de datos en Docker
        engine = create_engine('postgresql://postgres:postgres@localhost:5433/ny_taxi')
        
        # 2. Cargar el CSV de zonas a Postgres
        # Ajustamos la ruta para buscar en la carpeta datasets/
        path_zonas = 'datasets/taxi_zone_lookup.csv'
        print(f"Leyendo catálogo de zonas desde: {path_zonas}")
        
        df_zones = pd.read_csv(path_zonas)
        df_zones.to_sql(name='zones', con=engine, if_exists='replace', index=False)

        # 3. Consulta SQL con JOIN para encontrar la zona con mayor importe
        query = """
        SELECT 
            z."Zone", 
            SUM(t.total_amount) AS suma_total
        FROM green_taxi_data t
        JOIN zones z ON t."PULocationID" = z."LocationID"
        WHERE t.lpep_pickup_datetime::date = '2025-11-18'
        GROUP BY z."Zone"
        ORDER BY suma_total DESC
        LIMIT 1;
        """

        print("Calculando la zona con mayor importe el 18 de noviembre...")
        df_resultado = pd.read_sql(query, engine)
        
        if not df_resultado.empty:
            zona = df_resultado.iloc[0, 0]
            monto = df_resultado.iloc[0, 1]
            print("-" * 40)
            print(f"RESULTADO PREGUNTA 5")
            print(f"ZONA: {zona}")
            print(f"IMPORTE TOTAL: {monto:.2f}")
            print("-" * 40)
        else:
            print("No se encontraron viajes para el 18 de noviembre de 2025.")

    except FileNotFoundError:
        print("Error: No se encontró el archivo CSV en la carpeta 'datasets/'.")
    except Exception as e:
        print(f"Error inesperado: {e}")

if __name__ == "__main__":
    resolver_pregunta_5()
