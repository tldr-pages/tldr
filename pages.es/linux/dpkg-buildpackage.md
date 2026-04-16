# dpkg-buildpackage

> Compila paquetes binarios y/o fuente en formato Debian a partir del código fuente.
> Normalmente se ejecuta dentro de un árbol de código fuente que contiene un directorio `debian/`.
> También puede verificar dependencias de compilación, generar archivos como `.buildinfo` y `.changes`, y firmar el resultado si es aplicable.
> Más información: <https://man7.org/linux/man-pages/man1/dpkg-buildpackage.1.html>.

- Genera paquetes fuente y binario:

`dpkg-buildpackage`

- Genera solo paquetes binarios (sin el paquete fuente):

`dpkg-buildpackage -b`

- Genera solo el paquete fuente (sin compilar binarios):

`dpkg-buildpackage -S`

- No firma los archivos `.dsc` y `.changes`:

`dpkg-buildpackage -us -uc`

- Tampoco firma el archivo `.buildinfo`:

`dpkg-buildpackage -us -uc -ui`

- No ejecuta `clean` antes de compilar:

`dpkg-buildpackage -nc`

- También ejecuta `clean` después de la compilación:

`dpkg-buildpackage -tc`

- No verifica las dependencias de compilación:

`dpkg-buildpackage -d`

- Usa `fakeroot` como comando para obtener privilegios de root durante la compilación:

`dpkg-buildpackage -rfakeroot`

- Ejecuta un objetivo específico de `debian/rules`:

`dpkg-buildpackage -T clean`

- Compila en paralelo:

`DEB_BUILD_OPTIONS=parallel={{N}} dpkg-buildpackage`
