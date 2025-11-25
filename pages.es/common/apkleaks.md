# apkleaks

> Expone URIs, endpoints y secretos de archivos APK.
> Nota: APKLeaks utiliza el desensamblador `jadx` para decompilar archivos APK.
> Más información: <https://github.com/dwisiswant0/apkleaks>.

- Escanea un archivo APK en busca de URIs, endpoints y secretos:

`apkleaks {{[-f|--file]}} {{ruta/al/archivo.apk}}`

- Escanea y guarda el resultad[o] en un archivo específico:

`apkleaks {{[-f|--file]}} {{ruta/al/archivo.apk}} {{[-o|--output]}} {{ruta/al/archivo.txt}}`

- Pasar [a]rgumentos del desensamblador `jadx`:

`apkleaks {{[-f|--file]}} {{ruta/al/archivo.apk}} {{[-a|--args]}} "{{--threads-count 5 --deobf}}"`
