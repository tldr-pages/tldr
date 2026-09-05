# winedump

> Dump the contents of Windows binaries (PE, NE, etc.), demangle C++ symbols, and generate Wine `.spec` files.
> More information: <https://manned.org/winedump>.

- Dump the contents of a PE file, DLL, or executable:

`winedump dump {{path/to/file.dll}}`

- Dump only the [f]ile header information:

`winedump dump -f {{path/to/file.dll}}`

- Dump a specific section in [j]SON, such as the import or export table:

`winedump dump -j {{import|export}} {{path/to/file.dll}}`

- Demangle a C++ (MSVC-mangled) symbol:

`winedump sym {{mangled_symbol}}`

- Generate a `.spec` file and stub implementation code from a DLL:

`winedump spec {{path/to/file.dll}}`

- Display help:

`winedump -h`
