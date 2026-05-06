import os
from moviepy import ImageClip, concatenate_videoclips, vfx, AudioFileClip

class VideoGenerator:
    def __init__(self, ruta_carpeta, transicion=0.5, fps=24):
        """
        Inicializa el generador de video compatible con MoviePy v2.0+
        """
        self.ruta_carpeta = ruta_carpeta
        self.transicion = transicion
        self.fps = fps
        # Separamos las imágenes generales de la portada
        self.imagenes, self.ruta_portada = self._cargar_imagenes()

    def _cargar_imagenes(self):
        """Escanea la carpeta y retorna las imágenes normales y la ruta de la portada por separado."""
        if not os.path.exists(self.ruta_carpeta):
            print(f"Error: La ruta '{self.ruta_carpeta}' no existe.")
            return [], None
        
        archivos_totales = sorted([
            os.path.join(self.ruta_carpeta, f) 
            for f in os.listdir(self.ruta_carpeta) 
            if f.lower().endswith('.png')
        ])

        # Filtrar la portada para que no afecte el timing del audio
        imagenes_normales = [f for f in archivos_totales if "zz_portada.png" not in f]
        ruta_portada = next((f for f in archivos_totales if "zz_portada.png" in f), None)

        return imagenes_normales, ruta_portada

    def _procesar_clips(self, lista_rutas, duracion_por_imagen):
        """Aplica duración calculada y efectos de Fade."""
        clips = []
        for ruta in lista_rutas:
            # En v2.0+, usamos with_duration y with_effects
            clip = ImageClip(ruta).with_duration(duracion_por_imagen + self.transicion)
            
            clip = clip.with_effects([
                vfx.FadeIn(self.transicion),
                vfx.FadeOut(self.transicion)
            ])
            
            clips.append(clip)
        return clips

    def generar_video_con_audio(self, ruta_audio, nombre_salida="video_con_audio.mp4"):
        """
        Genera un video ajustado al audio y añade zz_portada.png al final por 6 segundos.
        """
        if not self.imagenes:
            print("No se encontraron imágenes .png.")
            return

        if not os.path.exists(ruta_audio):
            print(f"Error: El archivo de audio '{ruta_audio}' no existe.")
            return

        # 1. Cargar Audio
        audio = AudioFileClip(ruta_audio)
        duracion_audio = audio.duration
        num_imagenes = len(self.imagenes)

        # 2. Calcular duración por imagen (solo para la parte con audio)
        duracion_por_imagen = (duracion_audio / num_imagenes)
        
        print(f"Audio detectado: {duracion_audio:.2f}s")
        print(f"Duración por imagen (cuerpo): {duracion_por_imagen:.2f}s")

        # 3. Procesar clips principales
        clips = self._procesar_clips(self.imagenes, duracion_por_imagen)

        # 4. Procesar Clip de Portada Final (6 segundos)
        if self.ruta_portada:
            print(f"Añadiendo portada final: {self.ruta_portada}")
            clip_portada = (ImageClip(self.ruta_portada)
                            .with_duration(6.0 + self.transicion)
                            .with_effects([vfx.FadeIn(self.transicion), vfx.FadeOut(self.transicion)]))
            clips.append(clip_portada)
        else:
            print("Advertencia: No se encontró 'zz_portada.png' en la carpeta.")

        # 5. Concatenar
        video_final = concatenate_videoclips(clips, method="compose", padding=-self.transicion)
        
        # 6. Asignar audio (el audio terminará y luego quedará la portada en silencio o imagen fija)
        # Si prefieres que el audio se extienda, tendrías que editar el archivo de audio.
        video_final = video_final.with_audio(audio)

        # 7. Renderizar
        video_final.write_videofile(nombre_salida, fps=self.fps, codec="libx264", audio_codec="aac")

# --- Bloque de ejecución ---
if __name__ == "__main__":
    RUTA_FOTOS = "./expo" 
    RUTA_AUDIO = "audio.mp3" 

    generador = VideoGenerator(
        ruta_carpeta=RUTA_FOTOS, 
        transicion=0.5
    )

    generador.generar_video_con_audio(RUTA_AUDIO, "resultado_final_con_portada.mp4")
