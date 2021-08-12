# cmake

> Sistem de automatizare a construi cross-platform, care generează rețete pentru sisteme native de compilare.
> Mai multe informaţii: <https://cmake.org/cmake/help/latest/manual/cmake.1.html>

- Generați o rețetă de compilare în directorul curent cu `cmakelists.txt` dintr-un director de proiect:

`cmake {{path/to/project_directory}}`

- Generați o rețetă build, cu tipul de build setat la `Lansare` cu variabila CMake:

`cmake {{path/to/project_directory}} -D {{CMAKE_BUILD_TYPE=Release}}`

- Utilizați o rețetă generată într-un director dat pentru a construi artefacte:

`cmake --build {{path/to/build_directory}}`

- Instalați artefactele de construcție în `/usr/local/` și benzi de depanare simboluri:

`cmake --install {{path/to/build_directory}} --strip`

- Instalați artefactele de construcție utilizând prefixul personalizat pentru trasee:

`cmake --install {{path/to/build_directory}} --strip --prefix {{path/to/directory}}`

- Rulați o țintă de construire particularizată:

`cmake --build {{path/to/build_directory}} --target {{target_name}}`
