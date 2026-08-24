# dpkg-buildpackage

> Compila paquetes binarios y/o fuente en formato Debian a partir del código fuente.
> Normalmente se ejecuta dentro de un árbol de código fuente que contiene un directorio `debian/`.
> También puede verificar dependencias de compilación, generar archivos como `.buildinfo` y `.changes`, y firmar el resultado si es aplicable.
> Más información: <https://manned.org/dpkg-buildpackage>.

- Genera paquetes fuente y binario:

`dpkg-buildpackage`

- Genera solo paquetes binarios (sin el paquete fuente):

`dpkg-buildpackage {{[-b|--build=binary]}}`

- Genera solo el paquete fuente (sin compilar binarios):

`dpkg-buildpackage {{[-S|--build=source]}}`

- No firma los archivos `.dsc` y `.changes`:

`dpkg-buildpackage {{[-us|--unsigned-source]}} {{[-uc|--unsigned-changes]}}`

- No ejecuta `clean` antes de compilar:

`dpkg-buildpackage {{[-nc|--no-pre-clean]}}`

- Usa `fakeroot` como comando para obtener privilegios de root durante la compilación:

`dpkg-buildpackage {{[-r|--root-command=]}}fakeroot`

- Ejecuta un objetivo específico de `debian/rules`:

`dpkg-buildpackage {{[-T|--rules-target=]}}{{clean}}`
