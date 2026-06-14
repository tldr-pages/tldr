# դոկեր-մեքենա

> Ստեղծեք և կառավարեք Docker-ով աշխատող մեքենաներ:.
> Լրացուցիչ տեղեկություններ. <https://github.com/docker-archive-public/docker.machine>:.

- Ներկայիս գործող Docker մեքենաների ցուցակ.:

`docker-machine ls`

- Ստեղծեք նոր Docker մեքենա հատուկ անունով.:

`docker-machine create {{name}}`

- Ստացեք մեքենայի կարգավիճակը.:

`docker-machine status {{name}}`

- Գործարկել մեքենա.:

`docker-machine start {{name}}`

- Դադարեցրեք մեքենան.:

`docker-machine stop {{name}}`

- Ստուգեք մեքենայի մասին տեղեկատվությունը.:

`docker-machine inspect {{name}}`
