# docker cp

> Fájlok vagy könyvtárak másolása az állomás és a konténer fájlrendszere között. További információ: <https://docs.docker.com/engine/reference/commandline/cp>.

- Fájl vagy könyvtár másolása az állomásról egy konténerbe:

`docker cp {{path/to/file_or_directory_on_host}} {{container_name}}:{{path/to/file_or_directory_in_container}}`

- Fájl vagy könyvtár másolása egy konténerből a gazdára:

`docker cp {{container_name}}:{{path/to/file_or_directory_in_container}} {{path/to/file_or_directory_on_host}}`

- Fájl vagy könyvtár másolása az állomásról egy konténerbe, szimlinkek után (a szimlinkelt fájlokat közvetlenül másolja, magukat a szimlinkeket nem):

`docker cp --follow-link {{path/to/symlink_on_host}} {{container_name}}:{{path/to/file_or_directory_in_container}}`
