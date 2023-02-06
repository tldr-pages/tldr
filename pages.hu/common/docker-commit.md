# docker commit

> Új kép létrehozása egy konténer módosításaiból. További információ: <https://docs.docker.com/engine/reference/commandline/commit/>.

- Kép létrehozása egy adott konténerből:

`docker commit {{container}} {{image}}:{{tag}}`

- Alkalmazza a `CMD` Dockerfile utasítást a létrehozott image-re:

`docker commit --change="CMD {{command}}" {{container}} {{image}}:{{tag}}`

- Alkalmazzon egy `ENV` Dockerfile utasítást a létrehozott image-re:

`docker commit --change="ENV {{name}}={{value}}" {{container}} {{image}}:{{tag}}`

- Létrehoz egy képet egy adott szerzővel a metaadatokban:

`docker commit --author="{{author}}" {{container}} {{image}}:{{tag}}`

- Kép létrehozása egy adott megjegyzéssel a metaadatokban:

`docker commit --message="{{comment}}" {{container}} {{image}}:{{tag}}`

- Kép létrehozása a konténer szüneteltetése nélkül a commit során:

`docker commit --pause={{false}} {{container}} {{image}}:{{tag}}`

- Súgó megjelenítése:

`docker commit --help`
