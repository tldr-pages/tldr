# docker հանգույց

> Կառավարեք Docker Swarm հանգույցները:.
> Լրացուցիչ տեղեկություններ. <https://docs.docker.com/reference/cli/docker/node/>:.

- Թվարկե՛ք երամի հանգույցները.:

`docker node ls`

- Ցուցակել առաջադրանքները, որոնք գործում են մեկ կամ մի քանի հանգույցների վրա, լռելյայն ընթացիկ հանգույցի համար.:

`docker node ps {{node1 node2 node3 ...}}`

- Ցուցադրել մանրամասն տեղեկատվություն մեկ կամ մի քանի հանգույցների վերաբերյալ.:

`docker node inspect {{node1 node2 node3 ...}}`

- Խրախուսեք մեկ կամ մի քանի հանգույցներ մենեջերի համար.:

`docker node promote {{node1 node2 node3 ...}}`

- Մեկ կամ մի քանի հանգույց իջեցնել կառավարիչից երամում.:

`docker node demote {{node1 node2 node3 ...}}`

- Հեռացրեք մեկ կամ մի քանի հանգույցներ պարսից.:

`docker node rm {{node1 node2 node3 ...}}`

- Թարմացրեք հանգույցի մասին մետատվյալները, ինչպիսիք են դրա հասանելիությունը, պիտակները կամ դերերը.:

`docker node update --{{availability|role|label-add|...}} {{active|worker|...}} {{node1}}`
