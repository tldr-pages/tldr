# vswhere

> Localiza instalaciones de Visual Studio 2017 y posteriores.
> Más información: <https://github.com/microsoft/vswhere>.

- Encontrar la ruta de vcvarsall.bat para configurar variables de entorno:

`vswhere -products * -latest -prerelease -find **\VC\Auxiliary\Build\vcvarsall.bat`

- Encontrar el directorio del compilador x64 MSVC (cl.exe, etc.):

`vswhere -products * -latest -prerelease -find **\Hostx64\x64\*`

- Encontrar el directorio de Clang incluido con Visual Studio (clang-cl, clang-tidy, etc.):

`vswhere -products * -latest -prerelease -find **\Llvm\bin\*`

- Encontrar la ruta de `MSBuild.exe`:

`vswhere -products * -latest -prerelease -find MSBuild\**\Bin\MSBuild.exe`
