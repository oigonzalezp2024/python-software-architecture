import asyncio
import voice_generator
import VideoGenerator

if __name__ == "__main__":
    RUTA_FOTOS = "./expo" 
    RUTA_AUDIO = "audio.mp3" # Asegúrate de que este archivo exista

    texto_ejemplo = """Análisis del mercado de aguacate en San José de Cúcuta según el reporte de SIPSA DANE.

El comportamiento de los precios durante el mes de abril y los primeros días de mayo muestra una clara tendencia bajista. A pesar de registrarse una volatilidad considerable en las primeras semanas, el valor del producto terminó por debajo de su precio inicial.

Dentro de los valores más relevantes, destaca el precio máximo alcanzado el diez de abril, cuando llegó a los nueve mil seiscientos sesenta y siete pesos. Por el contrario, el punto más bajo se observó el veintiocho de abril, situándose en los siete mil quinientos ochenta y tres pesos.

Como conclusión, tras las fluctuaciones presentadas, el mercado ha encontrado un punto de equilibrio. Desde el treinta de abril hasta el cinco de mayo, el precio se ha mantenido estable en los ocho mil pesos, consolidando un soporte importante para el inicio de este mes.

Considerando que el mercado ha mostrado una tendencia bajista durante el mes de abril, es fundamental actuar con cautela. El precio alcanzó un máximo de nueve mil seiscientos sesenta y siete pesos el diez de abril, pero luego descendió hasta tocar un mínimo de siete mil quinientos ochenta y tres pesos el día veintiocho.

Actualmente, el panorama es de estabilidad, ya que el valor se ha mantenido firme en los ocho mil pesos desde el treinta de abril hasta el cinco de mayo. Para los comerciantes, este soporte de ocho mil pesos representa una oportunidad para estabilizar los márgenes de ganancia y planificar compras con menor riesgo de fluctuación inmediata.

Se sugiere monitorear de cerca este nivel de precio. Si el valor se mantiene constante, es un buen momento para fortalecer la rotación de inventarios; sin embargo, si el precio rompe el suelo de los siete mil quinientos ochenta y tres pesos, se recomienda reducir el volumen de existencias para proteger el capital de trabajo. Mantener una documentación clara de estas variaciones les permitirá tomar decisiones más rigurosas y basadas en datos reales del mercado local.

"""
    asyncio.run(voice_generator.generar_variantes(texto_ejemplo, voice_generator.PERFIL_B, "audio.mp3"))

    generador = VideoGenerator.VideoGenerator(
        ruta_carpeta=RUTA_FOTOS, 
        transicion=0.5
    )

    # Genera el video ajustado al audio
    generador.generar_video_con_audio(RUTA_AUDIO, "resultado_final_con_audio.mp4")
