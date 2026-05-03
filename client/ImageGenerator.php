<?php

class ImageGenerator {
    private $config;
    private $image;
    private $imgDir = __DIR__ . '/../static/images/';
    private $fontPath = __DIR__ . '/fonts/Roboto_Condensed-Bold.ttf';

    public function __construct($config) {
        $this->config = $config;
        $this->image = imagecreatetruecolor($config['canvas']['width'], $config['canvas']['height']);
        
        // Soporte para transparencia y mezcla de colores
        imagealphablending($this->image, true);
        imagesavealpha($this->image, true);
    }

    public function render() {
        // Primero renderizamos todas las imágenes (Capas inferiores)
        foreach ($this->config['elements'] as $el) {
            if ($el['type'] === 'image') $this->drawImage($el);
        }
        
        // Luego superponemos los textos (Capas superiores)
        foreach ($this->config['elements'] as $el) {
            if ($el['type'] === 'text') $this->drawText($el);
        }
    }

    private function drawImage($el) {
        $fullPath = $this->imgDir . $el['path'];
        if (!file_exists($fullPath)) return;

        $info = getimagesize($fullPath);
        $src = null;
        switch ($info[2]) {
            case IMAGETYPE_JPEG: $src = imagecreatefromjpeg($fullPath); break;
            case IMAGETYPE_PNG:  $src = imagecreatefrompng($fullPath);  break;
            case IMAGETYPE_WEBP: $src = imagecreatefromwebp($fullPath); break;
        }

        if ($src) {
            imagecopyresampled(
                $this->image, $src, 
                $el['x'], $el['y'], 0, 0, 
                $el['w'], $el['h'], $info[0], $info[1]
            );
            imagedestroy($src);
        }
    }

    private function drawText($el) {
        if (!file_exists($this->fontPath)) return;

        $data = $this->config['data'];
        $text = ($el['prefix'] ?? '') . ($data[$el['content_key']] ?? '');
        if (isset($el['suffix_key'])) $text .= " - " . $data[$el['suffix_key']];

        $colorArr = $this->hexToRgb($el['color']);
        $textColor = imagecolorallocate($this->image, $colorArr[0], $colorArr[1], $colorArr[2]);

        // Dibujar el borde (Outline) si está definido
        if (isset($el['outline_color']) && isset($el['outline_thickness'])) {
            $outArr = $this->hexToRgb($el['outline_color']);
            $outColor = imagecolorallocate($this->image, $outArr[0], $outArr[1], $outArr[2]);
            $this->drawOutline($el['size'], $el['x'], $el['y'], $outColor, $text, $el['outline_thickness']);
        }

        // Texto principal
        imagettftext($this->image, $el['size'], 0, $el['x'], $el['y'], $textColor, $this->fontPath, $text);
    }

    private function drawOutline($size, $x, $y, $color, $text, $thickness) {
        for ($dx = -$thickness; $dx <= $thickness; $dx++) {
            for ($dy = -$thickness; $dy <= $thickness; $dy++) {
                if ($dx == 0 && $dy == 0) continue;
                imagettftext($this->image, $size, 0, $x + $dx, $y + $dy, $color, $this->fontPath, $text);
            }
        }
    }

    private function hexToRgb($hex) {
        return sscanf($hex, "#%02x%02x%02x");
    }

    public function outputAvif($filename) {
        // Formato AVIF para máximo rendimiento técnico
        imageavif($this->image, $filename, 75);
        imagedestroy($this->image);
    }
}
