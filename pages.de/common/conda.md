# conda

> Eine Paket-, Abhängigkeits- und Umgebungsverwaltung für beliebige Programmiersprachen.
> Manche Unterbefehle wie `conda create` sind separat dokumentiert.
> Weitere Informationen: <https://github.com/conda/conda>.

- Erstelle eine neue Umgebung mit den zu installierenden Paketen:

`conda create --name {{umgebungsname}} {{python=3.9 matplotlib}}`

- Liste alle Umgebungen auf:

`conda info --envs`

- Lade eine Umgebung:

`conda {{activate umgebungs_name}}`

- Entlade eine Umgebung:

`conda {{deactivate}}`

- Lösche eine Umgebung (entferne alle Pakete):

`conda remove --name {{umgebungsname}} --all`

- Installiere Pakete in die derzeit geladene Umgebung:

`conda install {{python=3.4 numpy}}`

- Liste alle installierten Pakete in der derzeit geladenen Umgebung auf:

`conda list`

- Lösche alle ungenutzten Pakete und leere den Cache:

`conda clean --all`
