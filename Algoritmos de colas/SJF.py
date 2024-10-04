def sjf(tareas):
    """
    Este algoritmo organiza las tareas según su tiempo de ejecución, 
    priorizando las más cortas para minimizar el tiempo de espera promedio.
    """
    tareas.sort(key=lambda x: x['tiempo'])
    
    tiempo_total = 0
    tiempo_espera_total = 0
    tiempo_respuesta_total = 0
    tiempo_procesador = 0
    
    print("Ejecución de tareas en orden SJF:")
    
    for tarea in tareas:
        """
        Calcula el tiempo de espera para cada tarea en función de cuánto tiempo ha pasado
        desde que llegó hasta que comenzó a ejecutarse.
        """
        tiempo_espera = tiempo_total - tarea['llegada']
        if tiempo_espera < 0:
            tiempo_espera = 0
        
        tiempo_respuesta = tiempo_espera
        
        tiempo_espera_total += tiempo_espera
        tiempo_respuesta_total += tiempo_respuesta
        tiempo_procesador += tarea['tiempo']
        
        tiempo_total += tarea['tiempo']
        
        print(f"Tarea {tarea['nombre']} - Tiempo de ejecución: {tarea['tiempo']} - Tiempo de espera: {tiempo_espera}")

    tiempo_espera_promedio = tiempo_espera_total / len(tareas)
    tiempo_respuesta_promedio = tiempo_respuesta_total / len(tareas)
    utilizacion_procesador = (tiempo_procesador / tiempo_total) * 100
    
    print("--- Métricas ---")
    print(f"Tiempo de espera promedio: {tiempo_espera_promedio}")
    print(f"Tiempo de respuesta promedio: {tiempo_respuesta_promedio}")
    print(f"Utilización del procesador: {utilizacion_procesador}%")

tareas_sjf = [
    {'nombre': 'Tarea 1', 'tiempo': 6, 'llegada': 0},
    {'nombre': 'Tarea 2', 'tiempo': 2, 'llegada': 2},
    {'nombre': 'Tarea 3', 'tiempo': 8, 'llegada': 4},
    {'nombre': 'Tarea 4', 'tiempo': 3, 'llegada': 6}
]

sjf(tareas_sjf)




