<!DOCTYPE html>
<html lang="es">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Galería de Pimentón</title>
    <style>
        body {
            font-family: sans-serif;
            margin: 0;
            padding: 10px;
            background-color: #f4f4f4;
        }

        /* Contenedor flexible - TU DISEÑO ORIGINAL */
        .gallery-container {
            display: flex;
            flex-wrap: wrap; /* Permite que las imágenes bajen al siguiente renglón */
            gap: 10px;       /* Espacio entre imágenes */
            justify-content: center; /* Centra las imágenes */
        }

        /* Estilo de las imágenes - TU DISEÑO ORIGINAL */
        .gallery-item {
            width: calc(50% - 10px); /* 2 imágenes por fila en móvil */
            max-width: 300px;         /* No crecerán más de 300px en PC */
            height: auto;
            border-radius: 8px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            object-fit: cover;
        }

        /* Ajuste para pantallas muy pequeñas - TU DISEÑO ORIGINAL */
        @media (max-width: 400px) {
            .gallery-item {
                width: 100%; /* 1 sola imagen por fila en pantallas mini */
            }
        }
    </style>
</head>

<body>

    <div class="gallery-container">
        <?php
        // 1. Definimos la ruta de la carpeta
        $directory = '../static/images/expo/';

        // 2. Buscamos todos los archivos que terminen en .avif, .jpg, .png o .webp
        // Usamos GLOB_BRACE para que tome diferentes extensiones si las hay
        $images = glob($directory . "*.{avif,jpg,jpeg,png,webp}", GLOB_BRACE);

        // 3. Si existen imágenes, las recorremos todas
        if ($images) {
            foreach ($images as $image) {
                // Se aplica exactamente tu clase 'gallery-item'
                echo "<img class='gallery-item' src='$image' alt='Pimentón Cúcuta'>";
            }
        } else {
            echo "<p>No se encontraron imágenes en la carpeta.</p>";
        }
        ?>
    </div>

</body>

</html>