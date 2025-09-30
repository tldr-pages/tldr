# xmake

> A cross-platform C & C++ build utility based on Lua.
> More information: <https://xmake.io/#/getting_started>.

- Create an Xmake C project, consisting of a hello world and `xmake.lua`:

`xmake create {{[-l|--language]}} {{[c|clean]}} {{[-P|--project]}} {{project_name}}`

- Build and run an Xmake project:

`xmake {{[b|build]}} {{[r|run]}}`

- Run a compiled Xmake target directly:

`xmake {{[r|run]}} {{target_name}}`

- Configure a project's build targets:

`xmake {{[f|config]}} {{[-p |--plat=]}}{{macosx|linux|iphoneos|...}} {{[-a |--arch=]}}{{x86_64|i386|arm64|...}} {{[-m |--mode=]}}{{debug|release}}`

- Install the compiled target to a directory:

`xmake {{[i|install]}} {{[-o |--installdir=]}}{{path/to/directory}}`
