# podman պատկեր

> Կառավարեք OCI/Docker կոնտեյների պատկերները:.
> Տես նաև՝ `podman build`, `podman import`, `podman pull`:.
> Լրացուցիչ տեղեկություններ. <https://docs.podman.io/en/latest/markdown/podman-image.1.html>:.

- Թվարկեք տեղական կոնտեյների պատկերները.:

`podman image {{[ls|list]}}`

- Ջնջել չօգտագործված տեղական կոնտեյների պատկերները.:

`podman image prune`

- Ջնջել բոլոր չօգտագործված պատկերները (ոչ միայն առանց պիտակի).:

`podman image prune {{[-a|--all]}}`

- Ցույց տալ տեղական կոնտեյների պատկերի պատմությունը.:

`podman image history {{image}}`
