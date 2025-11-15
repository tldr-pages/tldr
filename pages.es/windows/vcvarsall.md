# vcvarsall

> Configura las variables de entorno necesarias para usar las herramientas de Microsoft Visual Studio.
> La ruta de `vcvarsall` para una instalación específica de Visual Studio puede encontrarse usando `vswhere`.
> Más información: <https://learn.microsoft.com/cpp/build/building-on-the-command-line>.

- Configurar el entorno para native x64:

`vcvarsall x64`

- Configurar el entorno para compilación cruzada nativa x86 desde un host x64:

`vcvarsall x64_x86`

- Configurar el entorno para compilación cruzada nativa Arm x64 desde un host x64:

`vcvarsall x64_arm64`

- Configurar el entorno para native UWP x64:

`vcvarsall x64 uwp`
