# uuencode

> A bináris fájlok ASCII-be kódolása olyan adathordozókon történő szállításhoz, amelyek csak az egyszerű ASCII kódolást támogatják. További információ: <https://manned.org/uuencode>.

- Egy fájl kódolása és az eredmény kinyomtatása a `stdout` címre:

`uuencode {{path/to/input_file}} {{output_file_name_after_decoding}}`

- Egy fájl kódolása és az eredmény kiírása egy fájlba:

`uuencode -o {{path/to/output_file}} {{path/to/input_file}} {{output_file_name_after_decoding}}`

- Egy fájl kódolása az alapértelmezett uuencode kódolás helyett a Base64 használatával, és az eredmény kiírása egy fájlba:

`uuencode -m -o {{path/to/output_file}} {{path/to/input_file}} {{output_file_name_after_decoding}}`
