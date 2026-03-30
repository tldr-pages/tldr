# jq

> Procesador de JSON que utiliza un lenguaje de dominio específico (DSL).
> Más información: <https://jqlang.org/manual/>.

- Ejecuta una expresión específica usando solo el binario `jq` (imprime la salida JSON con colores y formato):

`jq '.' {{ruta/al/archivo.json}}`

- Ejecuta un script específico:

`{{cat ruta/al/archivo.json}} | jq {{[-f|--from-file]}} {{ruta/al/script.jq}}`

- Pasa argumentos específicos:

`{{cat ruta/al/archivo.json}} | jq {{--arg "nombre1" "valor1" --arg "nombre2" "valor2" ...}} '{{. + $ARGS.named}}'`

- Crea un nuevo objeto JSON a partir de objetos JSON de múltiples archivos:

`{{cat ruta/a/multiples_archivos_json_*.json}} | jq '{{{nuevaClave1: .clave1, nuevaClave2: .clave2.claveAnidada, ...}}}'`

- Imprime elementos específicos de un array:

`{{cat ruta/al/archivo.json}} | jq '{{.[indice1], .[indice2], ...}}'`

- Imprime todos los valores de un array u objeto:

`{{cat ruta/al/archivo.json}} | jq '.[]'`

- Imprime objetos con filtro de 2 condiciones en un array:

`{{cat ruta/al/archivo.json}} | jq '.[] | select((.clave1=="valor1") and .clave2=="valor2")'`

- Añade o elimina claves específicas:

`{{cat ruta/al/archivo.json}} | jq '. {{+|-}} {{{"clave1": "valor1", "clave2": "valor2", ...}}}'`
