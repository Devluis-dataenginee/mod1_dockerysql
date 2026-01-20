import pandas as pd
from sqlalchemy import create_engine

def resolver_pregunta_3():
    # 1. Conexión a la base de datos en Docker
    # Usamos el puerto 5433 que definiste en tu docker-compose.yaml
    try:
        engine = create_engine('postgresql://postgres:postgres@localhost:5433/ny_taxi')
        
        # 2. Definir la consulta SQL para la Pregunta 3
        query = """
        SELECT COUNT(*) 
        FROM green_taxi_data
        WHERE lpep_pickup_datetime >= '2025-11-01' 
          AND lpep_pickup_datetime < '2025-12-01'
          AND trip_distance <= 1.0;
        """

        # 3. Ejecutar la consulta y obtener el resultado
        print("Ejecutando consulta para la Pregunta 3...")
        df_resultado = pd.read_sql(query, engine)
        
        # 4. Mostrar el resultado final
        resultado = df_resultado.iloc[0, 0]
        print("-" * 30)
        print(f"RESULTADO: {resultado}")
        print("-" * 30)
        
        if resultado == 8007:
            print("La respuesta coincide con la opción: 8007")

    except Exception as e:
        print(f"Error al conectar o consultar la base de datos: {e}")

if __name__ == "__main__":
    resolver_pregunta_3()