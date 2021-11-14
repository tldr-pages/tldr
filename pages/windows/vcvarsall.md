# vcvarsall

> Setup the environment variables required for using the Microsoft Visual Studio tools from the command line.
> The path of `vcvarsall.bat` for a certain Visual Studio installation can be found using `vswhere`.
> More information: <https://docs.microsoft.com/en-us/cpp/build/building-on-the-command-line>.

- Setup the environment for native x64:

`vcvarsall.bat x64`

- Setup the environment for cross-compiled native x86 from the x64 host:

`vcvarsall.bat x64_x86`

- Setup the environment for cross-compiled native Arm x64 from the x64 host:

`vcvarsall.bat x64_arm64`

- Setup the environment for native UWP x64:

`vcvarsall.bat x64 uwp`
