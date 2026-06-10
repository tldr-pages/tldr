# podman ps

> Ցուցակեք Podman բեռնարկղերը:.
> Լրացուցիչ տեղեկություններ. <https://docs.podman.io/en/latest/markdown/podman-ps.1.html>:.

- Ներկայիս գործող Podman կոնտեյներների ցուցակ.:

`podman ps`

- Թվարկեք Podman-ի բոլոր բեռնարկղերը (աշխատող և դադարեցված).:

`podman ps {{[-a|--all]}}`

- Ցույց տալ վերջին ստեղծված կոնտեյները (ներառում է բոլոր վիճակները).:

`podman ps {{[-l|--latest]}}`

- Զտել բեռնարկղերը, որոնք իրենց անունով ենթատող են պարունակում.:

`podman ps {{[-f|--filter]}} "name={{name}}"`

- Զտել տարաներ, որոնք կիսում են տվյալ պատկերը որպես նախնի.:

`podman ps {{[-f|--filter]}} "ancestor={{image}}:{{tag}}"`

- Զտեք բեռնարկղերը ելքի կարգավիճակի կոդով.:

`podman ps {{[-a|--all]}} {{[-f|--filter]}} "exited={{code}}"`

- Զտել բեռնարկղերը ըստ կարգավիճակի.:

`podman ps {{[-f|--filter]}} "status={{created|running|removing|paused|exited|dead}}"`

- Զտել տարաներ, որոնք տեղադրում են որոշակի ծավալ կամ ունեն որոշակի ուղու վրա տեղադրված ծավալ.:

`podman ps {{[-f|--filter]}} "volume={{path/to/directory}}" --format "table {{.ID}}\t{{.Image}}\t{{.Names}}\t{{.Mounts}}"`
