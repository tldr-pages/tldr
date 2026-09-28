# vcpkg integrate

> Integrate vcpkg with build systems and shells.
> More information: <https://learn.microsoft.com/en-us/vcpkg/commands/integrate>.

- Set up user-wide integration for the current vcpkg installation (on Windows this also integrates with Visual Studio, and prints the path of the CMake toolchain file):

`vcpkg integrate install`

- Remove the user-wide vcpkg integration:

`vcpkg integrate remove`

- Create a NuGet package that enables per-project MSBuild integration:

`vcpkg integrate project`

- Add vcpkg tab completion to the current user's PowerShell profile (Windows only):

`vcpkg integrate powershell`

- Add vcpkg tab completion to the current user's shell initialization file (non-Windows only; also supports `zsh` and `x-fish`):

`vcpkg integrate bash`
