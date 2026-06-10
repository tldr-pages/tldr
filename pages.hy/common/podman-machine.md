# podman մեքենա

> Ստեղծեք և կառավարեք Podman-ով աշխատող վիրտուալ մեքենաներ:.
> Ներառված է Podman 4 կամ ավելի տարբերակի հետ:.
> Լրացուցիչ տեղեկություններ. <https://docs.podman.io/en/latest/markdown/podman-machine.1.html>:.

- Թվարկեք առկա մեքենաները.:

`podman machine {{[ls|list]}}`

- Ստեղծեք նոր լռելյայն մեքենա.:

`podman machine init`

- Ստեղծեք նոր մեքենա հատուկ անունով.:

`podman machine init {{name}}`

- Ստեղծեք նոր մեքենա տարբեր ռեսուրսներով.:

`podman machine init --cpus {{4}} --memory {{4096}} --disk-size {{50}}`

- Գործարկել կամ դադարեցնել մեքենան.:

`podman machine {{start|stop}} {{name}}`

- Միացեք աշխատող մեքենային SSH-ի միջոցով.:

`podman machine ssh {{name}}`

- Ստուգեք մեքենայի մասին տեղեկատվությունը.:

`podman machine inspect {{name}}`
