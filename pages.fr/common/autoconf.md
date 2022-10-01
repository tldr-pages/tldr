# autoconf

> Génère des scripts de configuration pour configurer automatiquement les paquets du code source.
> Plus d'informations : <https://www.gnu.org/software/autoconf>.

- Génère un script de configuration depuis `configure.ac` (si présent) ou `configure.in` et le sauvegarde dans `configure` :

`autoconf`

- Génère un script de configuration depuis un modèle spécifié; et l'affiche la sortie standard :

`autoconf {{fichier_de_template}}`

- Génère un script de configuration depuis un modèle spécifié (même si the fichier d'entrée n'a pas changé) et l'écrit dans un fichier :

`autoconf --force --output={{fichier_de_sortie}} {{fichier_de_template}}`
