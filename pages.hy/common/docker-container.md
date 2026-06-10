# դոկեր կոնտեյներ

> Կառավարեք Docker կոնտեյներները:.
> Լրացուցիչ տեղեկություններ. <https://docs.docker.com/reference/cli/docker/container/>:.

- Ներկայիս գործող Docker կոնտեյներների ցուցակ.:

`docker {{[ps|container ls]}}`

- Սկսեք մեկ կամ մի քանի դադարեցված կոնտեյներ.:

`docker {{[start|container start]}} {{container1_name container2_name ...}}`

- Սպանեք մեկ կամ մի քանի հոսող կոնտեյներ.:

`docker {{[kill|container kill]}} {{container1_name container2_name ...}}`

- Դադարեցրեք մեկ կամ մի քանի բեռնարկղեր.:

`docker {{[stop|container stop]}} {{container1_name container2_name ...}}`

- Դադարեցնել բոլոր գործընթացները մեկ կամ մի քանի կոնտեյներով.:

`docker {{[pause|container pause]}} {{container1_name container2_name ...}}`

- Ցուցադրել մանրամասն տեղեկատվություն մեկ կամ մի քանի բեռնարկղերի վերաբերյալ.:

`docker container inspect {{container1_name container2_name ...}}`

- Արտահանել կոնտեյների ֆայլային համակարգը որպես `.tar` արխիվ.:

`docker {{[export|container export]}} {{container_name}}`

- Ստեղծեք նոր պատկեր կոնտեյների փոփոխություններից.:

`docker {{[commit|container commit]}} {{container_name}}`
