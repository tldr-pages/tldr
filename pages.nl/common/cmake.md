# cmake

> Cross-platform bouwautomatiseringssysteem dat recepten genereert voor native bouwsystemen.
> Meer informatie: <https://cmake.org/cmake/help/latest/manual/cmake.1.html>.

- Genereer een bouwrecept in de huidige map met `CMakeLists.txt` van een projectmap:

`cmake {{pad/naar/projectmap}}`

- Gebruik een gegenereerd recept in een bepaalde map om artefacten te bouwen:

`cmake --build {{pad/naar/bouwmap}}`

- Installeer de bouwartefacten in `/usr/local/` en verwijder debug-symbolen:

`cmake --install {{pad/naar/bouwmap}} --strip`

- Genereer een bouwrecept met bouwtype ingesteld naar `Release` met CMake-variabele:

`cmake {{pad/naar/projectmap}} -D CMAKE_BUILD_TYPE=Release`

- Genereer een bouwrecept met `generator_naam` als onderliggend bouwsysteem:

`cmake -G {{generator_naam}} {{pad/naar/projectmap}}`

- Installeer de bouwartefacten met een aangepaste voorvoegsel voor paden:

`cmake --install {{pad/naar/bouwmap}} --strip --prefix {{pad/naar/map}}`

- Voer een aangepaste bouwdoel uit:

`cmake --build {{pad/naar/bouwmap}} {{[-t|--target]}} {{doelnaam}}`

- Toon de help:

`cmake {{[-h|--help]}}`
