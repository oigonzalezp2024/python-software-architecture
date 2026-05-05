<?php
set_time_limit(0);
ini_set('memory_limit', '1024M');
gc_enable();

while (ob_get_level() > 0) { @ob_end_flush(); }
ob_implicit_flush(true);

require_once 'ImageGenerator.php';

function limpiarTexto($cadena, $mantenerGuionBajo = false) {
    $tabla = ['Á'=>'A','É'=>'E','Í'=>'I','Ó'=>'O','Ú'=>'U','Ñ'=>'N','á'=>'a','é'=>'e','í'=>'i','ó'=>'o','ú'=>'u','ñ'=>'n'];
    $cadena = strtr($cadena, $tabla);
    $cadena = strtolower(trim($cadena));
    if ($mantenerGuionBajo) {
        $cadena = preg_replace('/\s+/', '_', $cadena);
        return preg_replace('/[^a-z0-9_]/', '', $cadena);
    }
    return preg_replace('/[^a-z0-9]/', '', $cadena);
}

function generaImagen($mapData) {
    $nombreReporte = $mapData['data']['reporte'];
    $rutaFinalavif = '../static/images/expo/' . $nombreReporte . '.avif';
    $rutaFinalpng = '../static/images/expo/' . $nombreReporte . '.png';
    try {
        $generator = new ImageGenerator($mapData);
        $generator->render();
        $generator->outputPng($rutaFinalpng);
        $generator->outputAvif($rutaFinalavif);
        echo "✅ " . $nombreReporte . " procesado.<br>";
        unset($generator);
    } catch (Exception $e) {
        echo "❌ Error en $nombreReporte: " . $e->getMessage() . "<br>";
    }
}

// 1. CARGA DE DATOS
$mapData_base = json_decode(file_get_contents('data_map.json'), true);
$json_path = '../project/data/json/promediosSipsaCiudad.json';
$mapData_ciudad = json_decode(file_get_contents($json_path), true);

$ciudadObjetivoNorm = str_replace(['*', '.', '-'], '', trim(mb_strtolower("SAN JOSÉ DE CÚCUTA", 'UTF-8')));

// 2. FILTRADO: SOLO CÚCUTA Y SOLO EL REGISTRO MÁS RECIENTE POR PRODUCTO
$productosUnicos = [];

foreach ($mapData_ciudad as $item) {
    $ciudadLimpia = str_replace(['*', '.', '-'], '', trim(mb_strtolower($item['ciudad'], 'UTF-8')));
    
    if ($ciudadLimpia === $ciudadObjetivoNorm) {
        $idProducto = limpiarTexto($item['producto']); // Clave única por nombre de producto
        
        // Si no existe o si este registro tiene una fecha más reciente, lo guardamos/reemplazamos
        if (!isset($productosUnicos[$idProducto]) || 
            strtotime($item['fechaCaptura']) > strtotime($productosUnicos[$idProducto]['fechaCaptura'])) {
            $productosUnicos[$idProducto] = $item;
        }
    }
}

// Convertimos de nuevo a array indexado para procesar
$itemsAProcesar = array_values($productosUnicos);
$totalItems = count($itemsAProcesar);
$chunks = array_chunk($itemsAProcesar, 10);

echo "<h2>Detectados $totalItems productos únicos para Cúcuta</h2>";
echo "<p>Procesando en bloques de 10...</p><hr>";

$procesadosGlobal = 0;

foreach ($chunks as $indiceBloque => $bloque) {
    $numBloque = $indiceBloque + 1;
    echo "<strong>--- Bloque $numBloque ---</strong><br>";

    foreach ($bloque as $item) {
        $procesadosGlobal++;

        $ciudadArchivo   = limpiarTexto($item['ciudad']);
        $productoArchivo = limpiarTexto($item['producto'], true);
        $productoVisual  = preg_replace('/[^\w\sáéíóúÁÉÍÓÚñÑ]/u', '', $item['producto']);
        $ciudadVisual    = preg_replace('/[^\w\sáéíóúÁÉÍÓÚñÑ]/u', '', $item['ciudad']);

        $currentMapData = $mapData_base;
        $currentMapData['data'] = array_merge($currentMapData['data'], [
            'producto' => $productoVisual,
            'precio'   => '$' . number_format($item['precioPromedio'], 0, ',', '.'),
            'ciudad'   => $ciudadVisual,
            'fecha'    => date("d/m/Y", strtotime($item['fechaCaptura'])), // Fecha formateada legible
            'reporte'  => "reporte_{$ciudadArchivo}_{$productoArchivo}"
        ]);

        $currentMapData['elements'][0]['path'] = './fotos/ciudad.png';
        $currentMapData['elements'][1]['path'] = $ciudadArchivo . $productoArchivo . ".png";
        $currentMapData['elements'][2]['path'] = './fotos/' . $productoArchivo . '.png';

        generaImagen($currentMapData);
        flush();
    }

    gc_collect_cycles(); 
    usleep(100000); 
}

echo "<hr><h3>✅ PROCESO COMPLETADO</h3>";
echo "Total de imágenes generadas: <strong>$procesadosGlobal</strong>";

exit;