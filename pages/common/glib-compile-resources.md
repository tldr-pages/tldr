# glib-compile-resources

> Compiles resource files (e.g. images) into a binary resource bundle.
> These may be linked into GTK applications using the GResource API.
> More information: <https://manned.org/glib-compile-resources>.

- Compile resources referenced in `file.gresource.xml` to a .gresource binary:

`glib-compile-resources {{path/to/file.gresource.xml}}`

- Compile resources referenced in `file.gresource.xml` to a C source file:

`glib-compile-resources --generate-source {{path/to/file.gresource.xml}}`

- Compile resources in `file.gresource.xml` to a chosen target file, with `.c`, `.h` or `.gresource` extension:

`glib-compile-resources --generate --target={{path/to/file.ext}} {{path/to/file.gresource.xml}}`

- Print a list of resource files referenced in `file.gresource.xml`:

`glib-compile-resources --generate-dependencies {{path/to/file.gresource.xml}}`
