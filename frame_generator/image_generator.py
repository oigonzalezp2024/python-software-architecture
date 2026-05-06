import os
from PIL import Image, ImageDraw, ImageFont

class ImageGenerator:
    def __init__(self, config):
        self.config = config
        base_path = os.path.dirname(os.path.abspath(__file__))
        # Ruta a las imágenes estáticas
        self.img_dir = os.path.abspath(os.path.join(base_path, '../static/images/'))
        # Ruta a la fuente (asegúrate de que el archivo existe en esta carpeta)
        self.font_path = os.path.join(base_path, 'fonts', 'Roboto_Condensed-Bold.ttf')
        
        canvas_cfg = config['canvas']
        self.image = Image.new('RGBA', (canvas_cfg['width'], canvas_cfg['height']), (0, 0, 0, 0))
        self.draw = ImageDraw.Draw(self.image)

    def render(self):
        # 1. Renderizar Imágenes (Capas fondo)
        for el in self.config['elements']:
            if el['type'] == 'image': self._draw_image(el)
        
        # 2. Renderizar Textos (Capas superiores)
        for el in self.config['elements']:
            if el['type'] == 'text': self._draw_text(el)

    def _draw_image(self, el):
        full_path = os.path.join(self.img_dir, el['path'])
        if not os.path.exists(full_path): return

        with Image.open(full_path) as img:
            img_resized = img.convert("RGBA").resize((el['w'], el['h']), Image.Resampling.LANCZOS)
            self.image.paste(img_resized, (el['x'], el['y']), img_resized)

    def _draw_text(self, el):
        if not os.path.exists(self.font_path):
            print(f"⚠️ Fuente no encontrada en: {self.font_path}")
            return

        data = self.config.get('data', {})
        
        # Lógica idéntica a PHP: prefix + contenido de la llave
        texto_base = data.get(el['content_key'], '')
        text = f"{el.get('prefix', '')}{texto_base}"
        
        # Soporte para suffix_key (como lo tenías en PHP)
        if 'suffix_key' in el and el['suffix_key'] in data:
            text += f" - {data[el['suffix_key']]}"

        font = ImageFont.truetype(self.font_path, el['size'])
        color = self._hex_to_rgb(el['color'])

        # Dibujar Outline si existe
        if 'outline_color' in el and 'outline_thickness' in el:
            out_color = self._hex_to_rgb(el['outline_color'])
            self.draw.text(
                (el['x'], el['y']), text, font=font, fill=color,
                stroke_width=el['outline_thickness'], stroke_fill=out_color
            )
        else:
            self.draw.text((el['x'], el['y']), text, font=font, fill=color)

    def _hex_to_rgb(self, hex_str):
        hex_str = hex_str.lstrip('#')
        return tuple(int(hex_str[i:i+2], 16) for i in (0, 2, 4))

    def output_png(self, filename):
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        self.image.save(filename, "PNG")

    def output_avif(self, filename):
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        try:
            self.image.convert("RGB").save(filename, "AVIF", quality=75)
        except:
            self.image.save(filename.replace('.avif', '.webp'), "WEBP", quality=75)
