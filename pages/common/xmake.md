# xmake

> A cross-platform C & C++ build utility based on Lua.
> More information: <https://xmake.io/#/getting_started>.

- Create an xmake C project, consisting of a hello world and xmake.lua:

`xmake create --language c -P {{project-name}}`

- Build and run an xmake project:

`xmake build run`

- Run a compiled xmake target directly:

`xmake run {{target_name}}`

- Configure a project's build targets:

`xmake config --plat={{macosx|linux|iphoneos|...}} --arch={{x86_64|i386|arm64|...}} --mode={{debug|release}}`

- Install the compiled target to an output directory:

`xmake install -o {{path/to/directory}}`
