# asciidoctor

> Un processeur qui convertit des fichiers AsciiDoc vers un format publiable.
> Plus d'informations : <https://docs.asciidoctor.org>.

- Convertis un fichier `.adoc` vers un fichier HTML (le format de sortie par défaut) :

`asciidoctor {{chemin/vers/fichier.adoc}}`

- Convertis un fichier `.adoc` vers un fichier HTML et lie une feuille de style CSS :

`asciidoctor -a stylesheet {{chemin/vers/feuille_de_style.css}} {{chemin/vers/fichier.adoc}}`

- Convertis un fichier `.adoc` vers un fichier HTML embarqué, en enlevant tout sauf le body :

`asciidoctor --embedded {{chemin/vers/fichier.adoc}}`

- Convertis un fichier `.adoc` vers un PDF en utilisant la librairie `asciidoctor-pdf` :

`asciidoctor --backend {{pdf}} --require {{asciidoctor-pdf}} {{chemin/vers/fichier.adoc}}`
