# դոկերի պատկեր

> Կառավարեք Docker պատկերները:.
> Տես նաև՝ `docker build`, `docker image pull`, `docker image rm`:.
> Լրացուցիչ տեղեկություններ. <https://docs.docker.com/reference/cli/docker/image/>:.

- Թվարկեք տեղական Docker պատկերները.:

`docker {{[images|image ls]}}`

- Ջնջել չօգտագործված տեղական Docker պատկերները.:

`docker image prune`

- Ջնջել բոլոր չօգտագործված պատկերները (ոչ միայն առանց պիտակի).:

`docker image prune {{[-a|--all]}}`

- Ցույց տալ տեղական Docker պատկերի պատմությունը.:

`docker {{[history|image history]}} {{image}}`
