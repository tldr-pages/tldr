# podman քաշեք

> Քաշեք պատկերները կոնտեյների ռեեստրից:.
> Լրացուցիչ տեղեկություններ. <https://docs.podman.io/en/latest/markdown/podman-pull.1.html>:.

- Քաշեք հատուկ կոնտեյների պատկեր.:

`podman pull {{image}}:{{tag}}`

- Քաշեք կոնտեյների պատկերը հանգիստ ռեժիմով.:

`podman pull {{[-q|--quiet]}} {{image}}:{{tag}}`

- Քաշեք կոնտեյների պատկերի բոլոր պիտակները.:

`podman pull {{[-a|--all-tags]}} {{image}}`

- Քաշեք կոնտեյների պատկերը կոնկրետ հարթակի համար.:

`podman pull --platform {{linux/arm64}} {{image}}:{{tag}}`

- Քաշեք կոնտեյների պատկեր առանց TLS ստուգման.:

`podman pull --tls-verify=false {{image}}:{{tag}}`

- Ցուցադրել օգնությունը.:

`podman pull {{[-h|--help]}}`
