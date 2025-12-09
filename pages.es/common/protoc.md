# protoc

> Analiza los archivos `.proto` de Google Protobuf y genera la salida en el idioma especificado.
> Más información: <https://developers.google.com/protocol-buffers>.

- Genera código Python a partir de un archivo `.proto`:

`protoc --python_out={{ruta/a/directorio_salida}} {{archivo_entrada.proto}}`

- Genera código Java a partir de un archivo `.proto` que importa otros archivos `.proto`:

`protoc --java_out={{ruta/a/directorio_salida}} --proto_path={{ruta/a/importación_ruta_de_busqueda}} {{archivo_entrada.proto}}`

- Genera código para múltiples lenguajes:

`protoc --csharp_out={{ruta/a/c#_directorio_salida}} --js_out={{ruta/a/js_directorio_salida}} {{archivo_entrada.proto}}`

- Codifica un mensaje en formato texto en un mensaje de protocolo a partir de un archivo `.proto`:

`protoc --encode={{TypeName}} {{archivo_de_entrada.proto}} < {{mensaje.txt}}`

- Decodifica un mensaje de protocolo en formato de texto a partir de un archivo `.proto`:

`protoc --decode={{TypeName}} {{archivo_entrada.proto}} < {{mensaje.bin}}`

- Decodifica un mensaje de protocolo en pares de etiquetas/valores sin procesar:

`protoc --decode_raw < {{mensaje.bin}}`
