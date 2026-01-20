import pandas as pd
from sqlalchemy import create_engine

def resolver_pregunta_4():
    # 1. Conexión a la base de datos
    try:
        engine = create_engine('postgresql://postgres:postgres@localhost:5433/ny_taxi')
        
        # 2. Consulta SQL
        # Convertimos el timestamp a fecha (DATE) para agrupar
        # Filtramos por trip_distance < 160 para limpiar errores de datos
        query = """
        SELECT 
            lpep_pickup_datetime::date AS fecha_recogida, 
            MAX(trip_distance) AS distancia_maxima
        FROM green_taxi_data
        WHERE trip_distance < 160
        GROUP BY 1
        ORDER BY distancia_maxima DESC
        LIMIT 1;
        """

        print("Calculando el día con el viaje más largo...")
        df_resultado = pd.read_sql(query, engine)
        
        # 3. Mostrar resultados
        if not df_resultado.empty:
            fecha = df_resultado.iloc[0, 0]
            distancia = df_resultado.iloc[0, 1]
            print("-" * 40)
            print(f"La mayor distancia fue de: {distancia:.2f} km/millas")
            print(f"El día registrado fue: {fecha}")
            print("-" * 40)
            
            # Verificación con las opciones de la tarea
            opciones = ['2025-11-14', '2025-11-20', '2025-11-23', '2025-11-25']
            if str(fecha) in opciones:
                print(f"Este resultado coincide con una de tus opciones: {fecha}")
        else:
            print("No se encontraron datos que coincidan con los filtros.")

    except Exception as e:
        print(f"Error en la consulta: {e}")

if __name__ == "__main__":
        resolver_pregunta_4()