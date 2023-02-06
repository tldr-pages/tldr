# cmake

> Cross-platform build automation rendszer, amely recepteket generál natív build rendszerekhez. További információ: <https://cmake.org/cmake/help/latest/manual/cmake.1.html>.

- Építési recept generálása az aktuális könyvtárban a `CMakeLists.txt` címmel egy projektkönyvtárból:

`cmake {{path/to/project_directory}}`

- Generáljon egy build receptet, melynek build típusa a `Release` -ra van állítva a CMake változóval:

`cmake {{path/to/project_directory}} -D {{CMAKE_BUILD_TYPE=Release}}`

- Egy adott könyvtárban generált recept használata a leletek építéséhez:

`cmake --build {{path/to/build_directory}}`

- Telepítse a build artefaktumokat a `/usr/local/` címre, és távolítsa el a hibakeresési szimbólumokat:

`cmake --install {{path/to/build_directory}} --strip`

- Telepítse a build artefaktumokat az egyéni előtag használatával az elérési utakhoz:

`cmake --install {{path/to/build_directory}} --strip --prefix {{path/to/directory}}`

- Egyéni build-célpont futtatása:

`cmake --build {{path/to/build_directory}} --target {{target_name}}`
