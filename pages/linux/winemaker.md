# winemaker

> Generate build files to port Windows source code to a Winelib application.
> More information: <https://manned.org/winemaker>.

- Generate build files for a source tree (assumes a graphical application):

`winemaker {{path/to/source_directory}}`

- Treat the target as a console application:

`winemaker --console {{path/to/source_directory}}`

- Treat the target as a DLL:

`winemaker --dll {{path/to/source_directory}}`

- Generate build files without modifying or renaming the original sources:

`winemaker --nosource-fix {{path/to/source_directory}}`

- Process a project that uses MFC:

`winemaker --mfc {{path/to/source_directory}}`

- Display help:

`winemaker --help`
