# docker exec

> Executați o comandă pe un container Docker care rulează deja.
> Mai multe informaţii: <https://docs.docker.com/engine/reference/commandline/exec/>

- Introduceți o sesiune de shell interactivă pe un container care rulează deja:

`docker exec --interactive --tty {{container_name}} {{/bin/bash}}`

- Rulați o comandă în fundal (detașată) pe un container de alergare:

`docker exec --detach {{container_name}} {{command}}`

- Selectați directorul de lucru pentru o comandă dată pentru a executa în:

`docker exec --interactive -tty --workdir {{path/to/directory}} {{container_name}} {{command}}`

- Rulați o comandă în fundal pe containerul existent, dar păstrați stdin deschis:

`docker exec --interactive --detach {{container_name}} {{command}}`

- Setați o variabilă de mediu într-o sesiune de bash de funcționare:

`docker exec --interactive --tty --env {{variable_name}}={{value}} {{container_name}} {{/bin/bash}}`

- Rulați o comandă ca un anumit utilizator:

`docker exec --user {{user}} {{container_name}} {{command}}`
