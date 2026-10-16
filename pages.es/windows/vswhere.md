# vswhere

> Localiza instalaciones de Visual Studio 2017 y posteriores.
> Más información: <https://github.com/microsoft/vswhere>.

- Encuentra la ruta de vcvarsall.bat para configurar variables de entorno:

`vswhere -products * -latest -prerelease -find **\VC\Auxiliary\Build\vcvarsall.bat`

- Encuentra el directorio del compilador x64 MSVC (`cl.exe`, etc.):

`vswhere -products * -latest -prerelease -find **\Hostx64\x64\*`

- Encuentra el directorio de Clang incluido con Visual Studio (clang-cl, clang-tidy, etc.):

`vswhere -products * -latest -prerelease -find **\Llvm\bin\*`

- Encuentra la ruta de `MSBuild.exe`:

`vswhere -products * -latest -prerelease -find MSBuild\**\Bin\MSBuild.exe`
