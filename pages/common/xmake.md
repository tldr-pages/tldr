# xmake

> A cross-platform C & C++ build utility based on Lua.
> More information: <https://xmake.io/#/getting_started>.

- Create an Xmake C project, consisting of a hello world and `xmake.lua`:

`xmake create --language c -P {{project_name}}`

- Build and run an Xmake project:

`xmake build run`

- Run a compiled Xmake target directly:

`xmake run {{target_name}}`

- Configure a project's build targets:

`xmake config --plat={{macosx|linux|iphoneos|...}} --arch={{x86_64|i386|arm64|...}} --mode={{debug|release}}`

- Install the compiled target to a directory:

`xmake install -o {{path/to/directory}}`
