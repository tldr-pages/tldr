# docker images

> Docker-képek kezelése. További információ: <https://docs.docker.com/engine/reference/commandline/images/>.

- Az összes Docker-kép listázása:

`docker images`

- Az összes Docker-kép listázása, beleértve a közteseket is:

`docker images --all`

- Listázza a kimenetet csendes üzemmódban (csak numerikus azonosítók):

`docker images --quiet`

- Az összes olyan Docker-kép listázása, amelyet egyetlen konténer sem használ:

`docker images --filter dangling=true`

- Azoknak a képeknek a listázása, amelyek nevében szerepel egy részlánc:

`docker images "{{*name*}}"`
