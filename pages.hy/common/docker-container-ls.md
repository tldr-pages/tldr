# դոկեր կոնտեյներ ls

> Ցուցակ Docker կոնտեյներներ:.
> Լրացուցիչ տեղեկություններ. <https://docs.docker.com/reference/cli/docker/container/ls/>:.

- Ներկայիս գործող Docker կոնտեյներների ցուցակ.:

`docker {{[ps|container ls]}}`

- Թվարկեք բոլոր Docker կոնտեյներները (աշխատող և դադարեցված).:

`docker {{[ps|container ls]}} {{[-a|--all]}}`

- Ցույց տալ վերջին ստեղծված կոնտեյները (ներառում է բոլոր վիճակները).:

`docker {{[ps|container ls]}} {{[-l|--latest]}}`

- Զտել բեռնարկղերը, որոնք իրենց անունով ենթատող են պարունակում.:

`docker {{[ps|container ls]}} {{[-f|--filter]}} "name={{name}}"`

- Զտել տարաներ, որոնք կիսում են տվյալ պատկերը որպես նախնի.:

`docker {{[ps|container ls]}} {{[-f|--filter]}} "ancestor={{image}}:{{tag}}"`

- Զտեք բեռնարկղերը ելքի կարգավիճակի կոդով.:

`docker {{[ps|container ls]}} {{[-f|--filter]}} "exited={{code}}" {{[-a|--all]}}`

- Զտել բեռնարկղերը ըստ կարգավիճակի (ստեղծված, գործարկված, հեռացված, դադարեցված, ելք և մեռած).:

`docker {{[ps|container ls]}} {{[-f|--filter]}} "status={{status}}"`

- Զտել տարաներ, որոնք տեղադրում են որոշակի ծավալ կամ ունեն որոշակի ուղու վրա տեղադրված ծավալ.:

`docker {{[ps|container ls]}} {{[-f|--filter]}} "volume={{path/to/directory}}" --format "table {{.ID}}\t{{.Image}}\t{{.Names}}\t{{.Mounts}}"`
