# vswhere

> Keresse meg a Visual Studio 2017 és újabb telepítéseket. További információ: <https://github.com/microsoft/vswhere>.

- Keresse meg a vcvarsall.bat elérési útját a környezeti változók beállításához:

`vswhere -products * -latest -prerelease -find **/VC/Auxiliary/Build/vcvarsall.bat`

- Keresse meg az x64 MSVC fordító könyvtárát (cl.exe stb.):

`vswhere -products * -latest -prerelease -find **/Hostx64/x64/*`

- Keresse meg a Visual Studio csomagban csomagolt Clang könyvtárát (clang-cl, clang-tidy stb.):

`vswhere -products * -latest -prerelease -find **/Llvm/bin/*`

- Keresse meg a `MSBuild.exe` elérési útvonalát:

`vswhere -products * -latest -prerelease -find MSBuild/**/Bin/MSBuild.exe`
