# դոկեր

> Կառավարեք Docker բեռնարկղերը և պատկերները:.
> Որոշ ենթահրամաններ, ինչպիսիք են `container`-ը և `image`-ն, ունեն իրենց օգտագործման փաստաթղթերը:.
> Լրացուցիչ տեղեկություններ. <https://docs.docker.com/reference/cli/docker/>:.

- Թվարկեք բոլոր Docker կոնտեյներները (աշխատող և դադարեցված).:

`docker {{[ps|container ls]}} {{[-a|--all]}}`

- Սկսեք կոնտեյներ պատկերից, հատուկ անունով.:

`docker {{[run|container run]}} --name {{container_name}} {{image}}`

- Սկսել կամ դադարեցնել գոյություն ունեցող կոնտեյները.:

`docker container {{start|stop}} {{container_name}}`

- Քաշեք պատկեր Docker ռեեստրից.:

`docker {{[pull|image pull]}} {{image}}`

- Ցուցադրել արդեն ներբեռնված պատկերների ցանկը.:

`docker {{[images|image ls]}}`

- Բացեք ինտերակտիվ tty Bourne shell-ով (`sh`) հոսող կոնտեյների ներսում.:

`docker {{[exec|container exec]}} {{[-it|--interactive --tty]}} {{container_name}} {{sh}}`

- Հեռացրեք կանգնեցված տարաները.:

`docker {{[rm|container rm]}} {{container1 container2 ...}}`

- Վերցրեք և հետևեք կոնտեյների տեղեկամատյաններին.:

`docker {{[logs|container logs]}} {{[-f|--follow]}} {{container_name}}`
