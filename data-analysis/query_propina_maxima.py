import pandas as pd
from sqlalchemy import create_engine

def resolver_pregunta_6():
    try:
        engine = create_engine('postgresql://postgres:postgres@localhost:5433/ny_taxi')
        
        # Consulta SQL para encontrar la zona de destino con mayor propina
        # Filtramos por zona de recogida "East Harlem North" en noviembre 2025
        query = """
        SELECT 
            z_do."Zone" AS zona_destino, 
            MAX(t.tip_amount) AS propina_maxima
        FROM green_taxi_data t
        JOIN zones z_pu ON t."PULocationID" = z_pu."LocationID"
        JOIN zones z_do ON t."DOLocationID" = z_do."LocationID"
        WHERE z_pu."Zone" = 'East Harlem North'
          AND t.lpep_pickup_datetime >= '2025-11-01'
          AND t.lpep_pickup_datetime < '2025-12-01'
        GROUP BY z_do."Zone"
        ORDER BY propina_maxima DESC
        LIMIT 1;
        """

        print("Buscando la zona de destino con la propina más alta para East Harlem North...")
        df_resultado = pd.read_sql(query, engine)
        
        if not df_resultado.empty:
            zona_dest = df_resultado.iloc[0, 0]
            propina = df_resultado.iloc[0, 1]
            print("-" * 45)
            print(f"RESULTADO PREGUNTA 6")
            print(f"Zona de destino: {zona_dest}")
            print(f"Propina más alta: ${propina:.2f}")
            print("-" * 45)
        else:
            print("No se encontraron registros que coincidan.")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    resolver_pregunta_6()
