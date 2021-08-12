# docker save

> Exportați una sau mai multe imagini docker în arhivă.
> Mai multe informaţii: <https://docs.docker.com/engine/reference/commandline/save/>

- Salvați o imagine prin redirecționarea stdout către o arhivă de gudron:

`docker save {{image}}:{{tag}} > {{path/to/file.tar}}`

- Salvați o imagine într-o arhivă de gudron:

`docker save --output {{path/to/file.tar}} {{image}}:{{tag}}`

- Salvați toate etichetele imaginii:

`docker save --output {{path/to/file.tar}} {{image_name}}`

- Cherry-alege anumite etichete ale unei imagini pentru a salva:

`docker save --output {{path/to/file.tar}} {{image_name:tag1 image_name:tag2 ...}}`
