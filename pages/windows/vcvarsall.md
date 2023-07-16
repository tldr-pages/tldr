# vcvarsall

> Setup the environment variables required for using the Microsoft Visual Studio tools.
> The path of `vcvarsall` for a certain Visual Studio installation can be found using `vswhere`.
> More information: <https://learn.microsoft.com/cpp/build/building-on-the-command-line>.

- Setup the environment for native x64:

`vcvarsall x64`

- Setup the environment for cross-compiled native x86 from the x64 host:

`vcvarsall x64_x86`

- Setup the environment for cross-compiled native Arm x64 from the x64 host:

`vcvarsall x64_arm64`

- Setup the environment for native UWP x64:

`vcvarsall x64 uwp`
