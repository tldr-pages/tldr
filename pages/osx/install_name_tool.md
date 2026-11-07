# install_name_tool

> Change dynamic shared library install names and rpaths in Mach-O binaries.
> More information: <https://keith.github.io/xcode-man-pages/install_name_tool.1.html>.

- Change the install name of a linked library in a binary:

`install_name_tool -change {{old/path/to/library.dylib}} {{new/path/to/library.dylib}} {{path/to/binary}}`

- Change the identification name of a dynamic library:

`install_name_tool -id {{@rpath/library.dylib}} {{path/to/library.dylib}}`

- Add an rpath to a binary:

`install_name_tool -add_rpath {{@executable_path/../Frameworks}} {{path/to/binary}}`

- Change an existing rpath in a binary:

`install_name_tool -rpath {{old/rpath}} {{new/rpath}} {{path/to/binary}}`

- Delete an rpath from a binary:

`install_name_tool -delete_rpath {{rpath}} {{path/to/binary}}`
