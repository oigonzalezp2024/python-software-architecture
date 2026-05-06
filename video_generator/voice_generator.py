import asyncio
import edge_tts

# 1. El "Jefe Senior" (Voz grave, pausada, mucha autoridad)
PERFIL_A = {"voice": "es-CO-SalomeNeural", "rate": "-15%", "pitch": "-10Hz"}

# 2. El "Colega Joven" (Voz más rápida, enérgica, tono natural)
PERFIL_B = {"voice": "es-CO-SalomeNeural", "rate": "+5%", "pitch": "+2Hz"}

# 3. El "Asistente Formal" (Voz plana, velocidad media, tono institucional)
PERFIL_C = {"voice": "es-CO-SalomeNeural", "rate": "+0%", "pitch": "-5Hz"}

async def generar_variantes(texto, perfil, nombre_archivo):
    communicate = edge_tts.Communicate(
        texto, 
        perfil["voice"], 
        rate=perfil["rate"], 
        pitch=perfil["pitch"]
    )
    await communicate.save(nombre_archivo)

if __name__ == "__main__":
    texto_ejemplo = """Análisis del mercado de aguacate en San José de Cúcuta según el reporte de SIPSA DANE.

El comportamiento de los precios durante el mes de abril y los primeros días de mayo muestra una clara tendencia bajista. A pesar de registrarse una volatilidad considerable en las primeras semanas, el valor del producto terminó por debajo de su precio inicial.

Dentro de los valores más relevantes, destaca el precio máximo alcanzado el diez de abril, cuando llegó a los nueve mil seiscientos sesenta y siete pesos. Por el contrario, el punto más bajo se observó el veintiocho de abril, situándose en los siete mil quinientos ochenta y tres pesos.

Como conclusión, tras las fluctuaciones presentadas, el mercado ha encontrado un punto de equilibrio. Desde el treinta de abril hasta el cinco de mayo, el precio se ha mantenido estable en los ocho mil pesos, consolidando un soporte importante para el inicio de este mes."""
    asyncio.run(generar_variantes(texto_ejemplo, PERFIL_B, "audio.mp3"))