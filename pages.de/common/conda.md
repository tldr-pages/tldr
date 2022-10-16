# conda

> Ein Kommandozeilentool und Paketverwaltung für beliebige Programmiersprachen.
> Manche Unterbefehle wie `conda create` sind separat dokumentiert.
> Weitere Informationen: <https://github.com/conda/conda>.

- Erstelle eine neue Umgebung mit den zu installierenden Paketen:

`conda create --name {{umgebungs_name}} {{python=3.9 matplotlib}}`

- Liste alle Umgebungen auf:

`conda info --envs`

- Lade eine Umgebung:

`conda {{activate umgebungs_name}}`

- Entlade eine Umgebung:

`conda {{deactivate}}`

- Lösche eine Umgebung (entferne alle Pakete):

`conda remove --name {{umgebungs_name}} --all`

- Installiere Pakete in die derzeit geladene Umgebung:

`conda install {{python=3.4 numpy}}`

- Auflistung aller installierten Pakete in der derzeit geladenen Umgebung:

`conda list`

- Lösche alle ungenutzten Pakete und leere den Cache:

`conda clean --all`
