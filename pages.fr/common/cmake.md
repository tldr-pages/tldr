# cmake

> Système de construction logicielle multiplateforme, qui permet de générer des recettes de construction pour les systèmes de construction natifs.
> Plus d'informations : <https://cmake.org/cmake/help/latest/manual/cmake.1.html>.

- Génère une recette de construction `CMakeLists.txt` depuis le répertoire d'un projet :

`cmake {{chemin/vers/le/répertoire_du_projet}}`

- Génère une recette de construction, en définissant le type de construction à `Release` à l'aide d'une variable CMake :

`cmake {{chemin/vers/le/répertoire_du_projet}} -D {{CMAKE_BUILD_TYPE=Release}}`

- Utilise une recette déjà générée dans un répertoire donné pour construire les artefacts :

`cmake --build {{chemin/vers/le/répertoire_de_construction}}`

- Installe les artefacts de construction dans `/usr/local/` et retirer les symboles de débogage :

`cmake --install {{chemin/vers/le/répertoire_de_construction}} --strip`

- Installe les artefacts de construction en utilisant un préfixe personnalisé pour les chemins :

`cmake --install {{chemin/vers/le/répertoire_de_construction}} --strip --prefix {{chemin/vers/le/répertoire}}`

- Lance une cible de construction personnalisée :

`cmake --build {{chemin/vers/le/répertoire_de_construction}} --target {{nom_de_la_cible}}`
