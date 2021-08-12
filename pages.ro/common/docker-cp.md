# docker cp

> Copiați fișiere sau directoare între sistemele de fișiere gazdă și container.
> Mai multe informaţii: <https://docs.docker.com/engine/reference/commandline/cp>

- Copiați un fișier sau un director de la gazdă într-un container:

`docker cp {{path/to/file_or_directory_on_host}} {{container_name}}:{{path/to/file_or_directory_in_container}}`

- Copiați un fișier sau un director dintr-un container la gazdă:

`docker cp {{container_name}}:{{path/to/file_or_directory_in_container}} {{path/to/file_or_directory_on_host}}`

- Copiați un fișier sau un director de la gazdă într-un container, urmând link-uri simbolice (copiază fișierele simlink direct, nu legăturile simbolice în sine):

`docker cp --follow-link {{path/to/symlink_on_host}} {{container_name}}:{{path/to/file_or_directory_in_container}}`
