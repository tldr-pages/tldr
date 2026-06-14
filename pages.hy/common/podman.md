# podman

> Պարզ կառավարման գործիք պատիճների, բեռնարկղերի և պատկերների համար:.
> Podman-ը տրամադրում է Docker-CLI համադրելի հրամանի տող: Պարզ ասած՝ `alias docker=podman`:.
> Լրացուցիչ տեղեկություններ. <https://github.com/containers/podman/blob/main/commands-demo.md>:.

- Թվարկեք բոլոր բեռնարկղերը (ինչպես աշխատող, այնպես էլ դադարեցված).:

`podman ps {{[-a|--all]}}`

- Ստեղծեք կոնտեյներ պատկերից, հատուկ անունով.:

`podman run --name {{container_name}} {{image}}`

- Սկսել կամ դադարեցնել գոյություն ունեցող կոնտեյները.:

`podman {{start|stop}} {{container_name}}`

- Քաշեք պատկեր ռեեստրից (կանխադրված է Docker Hub-ին).:

`podman pull {{image}}`

- Ցուցադրել արդեն ներբեռնված պատկերների ցանկը.:

`podman images`

- Բացեք պատյան արդեն հոսող տարայի մեջ.:

`podman exec {{[-it|--interactive --tty]}} {{container_name}} {{sh}}`

- Հեռացրեք կանգնեցված տարան.:

`podman rm {{container_name}}`

- Ցուցադրել մեկ կամ մի քանի բեռնարկղերի տեղեկամատյանները և հետևել գրանցամատյանի ելքին.:

`podman logs {{[-f|--follow]}} {{container_name_or_id1 container_name_or_id2 ...}}`
