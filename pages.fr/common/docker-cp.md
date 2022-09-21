# docker cp

> Copier des fichiers ou des répertoires entre les systèmes de fichiers hôte et conteneur.
> Plus d'informations : <https://docs.docker.com/engine/reference/commandline/cp>.

- Copier un fichier ou un répertoire de l'hôte vers un conteneur :

`docker cp {{path/to/file_or_directory_on_host}} {{container_name}}:{{path/to/file_or_directory_in_container}}`

- Copier un fichier ou un répertoire d'un conteneur vers l'hôte :

`docker cp {{container_name}}:{{path/to/file_or_directory_in_container}} {{path/to/file_or_directory_on_host}}`

- Copier un fichier ou un répertoire de l'hôte vers un conteneur, en suivant les liens symboliques (copie les fichiers liés directement, pas les liens symboliques eux-mêmes) :

`docker cp --follow-link {{path/to/symlink_on_host}} {{container_name}}:{{path/to/file_or_directory_in_container}}`
