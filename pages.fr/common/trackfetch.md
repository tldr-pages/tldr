# trackfetch

> Télécharger les chansons listées dans un fichier texte sous forme de fichiers MP3, M4A ou Opus tagués, en utilisant les métadonnées de Spotify et l'audio de YouTube.
> Nécessite `yt-dlp`, `ffmpeg` et l'identifiant client ainsi que le secret Spotify (fichier de configuration ou `SPOTIFY_CLIENT_ID` et `SPOTIFY_CLIENT_SECRET`).
> Plus d'informations : <https://github.com/ByteMe6/trackfetch#usage>.

- Télécharger toutes les chansons d'un fichier contenant une ligne `Artiste - Titre` par chanson dans le répertoire courant :

`trackfetch {{path/to/songs.txt}}`

- Télécharger les chansons dans un répertoire précis :

`trackfetch {{path/to/songs.txt}} {{[-o|--output]}} {{path/to/directory}}`

- Conserver l'audio original de YouTube au lieu de le convertir en MP3 :

`trackfetch {{path/to/songs.txt}} {{[-f|--format]}} {{opus|m4a}}`

- Télécharger quelques titres sans fichier texte :

`trackfetch {{"Artist - Title"}} {{"Another Artist - Another Title"}}`

- Nommer les fichiers avec le seul titre de la chanson au lieu de `Artiste - Titre` :

`trackfetch {{path/to/songs.txt}} --title-only`

- Utiliser un fichier de configuration pour les valeurs par défaut :

`trackfetch {{path/to/songs.txt}} {{[--config]}} {{path/to/config.ini}}`

- Attendre quelques secondes entre les chansons pour éviter de dépasser les limites de requêtes :

`trackfetch {{path/to/songs.txt}} --delay {{3}}`

- Réessayer les chansons qui ont échoué lors de l'exécution précédente :

`cut {{[-d|--delimiter]}} '|' {{[-f|--fields]}} 1 {{path/to/directory}}/failed.txt > {{path/to/retry.txt}} && trackfetch {{path/to/retry.txt}} {{[-o|--output]}} {{path/to/directory}}`
