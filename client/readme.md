Para realizar este proceso de forma estructurada, dividiremos el desarrollo en tres componentes: el esquema **JSON** de configuración, el **Controlador** que gestiona la lógica y el **Generador** que utiliza la extensión `GD` de PHP (asegurándote de tener soporte para AVIF habilitado).

### 1. Mapeo de Datos (data_map.json)
Este archivo define qué información se va a renderizar y en qué posición.

```json
{
    "canvas": {
        "width": 1080,
        "height": 1920,
        "background_color": "#FFFFFF"
    },
    "elements": [
        {
            "type": "text",
            "content": "Precio del Pimentón",
            "x": 50, "y": 200,
            "size": 60,
            "color": "#FFFFFF",
            "font": "fonts/Bold.ttf"
        },
        {
            "type": "text",
            "content": "Cúcuta - 2026/04/14",
            "x": 50, "y": 280,
            "size": 50,
            "color": "#FFFFFF",
            "font": "fonts/Regular.ttf"
        },
        {
            "type": "chart",
            "source": "api_dane_sipsa",
            "x": 0, "y": 400,
            "width": 1080,
            "height": 600
        },
        {
            "type": "price",
            "content": "$4.653",
            "x": 540, "y": 1500,
            "size": 180,
            "color": "#FFFFFF",
            "align": "center"
        }
    ]
}
```

---

### 2. Controlador (index.php)
El controlador se encarga de leer el JSON e instanciar la clase generadora.

```php
<?php
require_once 'ImageGenerator.php';

// Leer el mapeo de datos
$mapData = json_decode(file_get_contents('data_map.json'), true);

// Instanciar el generador
$generator = new ImageGenerator($mapData);

// Ejecutar proceso y salida
$generator->render();
$generator->outputAvif('output_pimenton.avif');

echo "Imagen generada con éxito en formato AVIF.";
```

---

### 3. Generador de Salida (ImageGenerator.php)
Esta clase procesa los datos y construye la imagen final.

```php
<?php

class ImageGenerator {
    private $config;
    private $image;

    public function __construct($config) {
        $this->config = $config;
        $this->image = imagecreatetruecolor(
            $this->config['canvas']['width'], 
            $this->config['canvas']['height']
        );
    }

    public function render() {
        // Lógica simplificada para renderizar elementos
        foreach ($this->config['elements'] as $element) {
            switch ($element['type']) {
                case 'text':
                case 'price':
                    $this->drawText($element);
                    break;
                case 'chart':
                    // Aquí se integraría la lógica para pegar la imagen del gráfico
                    break;
            }
        }
    }

    private function drawText($el) {
        $color = $this->hexToRgb($el['color']);
        $textColor = imagecolorallocate($this->image, $color[0], $color[1], $color[2]);
        
        // Nota: Requiere archivo .ttf en la ruta especificada
        imagettftext(
            $this->image, 
            $el['size'], 
            0, 
            $el['x'], 
            $el['y'], 
            $textColor, 
            './fonts/Roboto-Bold.ttf', 
            $el['content']
        );
    }

    public function outputAvif($filename) {
        // El tercer parámetro es la calidad (0-100), el cuarto es la velocidad (0-10)
        imageavif($this->image, $filename, 80, 6);
        imagedestroy($this->image);
    }

    private function hexToRgb($hex) {
        return sscanf($hex, "#%02x%02x%02x");
    }
}
```

### Notas técnicas:
* **Requisito de AVIF:** PHP debe estar compilado con soporte para `libavif` y la extensión GD. Puedes verificarlo con `phpinfo()`.
* **Fuentes:** Asegúrate de tener las fuentes TrueType (`.ttf`) en una carpeta local para que `imagettftext` funcione correctamente.
* **Gráficos:** Para la sección del gráfico de DANE-SIPSA, podrías usar una librería como **Chart.js** (capturando el canvas) o generar el gráfico directamente en PHP con **pChart** antes de insertarlo en el generador principal.