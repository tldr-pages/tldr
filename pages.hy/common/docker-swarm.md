# docker երամ

> Կոնտեյներային նվագախմբի գործիք:.
> Լրացուցիչ տեղեկություններ. <https://docs.docker.com/engine/swarm/>:.

- Նախաձեռնել երամի կլաստերը.:

`docker swarm init`

- Ցուցադրեք մենեջերին կամ աշխատողին միանալու նշանը.:

`docker swarm join-token {{worker|manager}}`

- Միացրեք նոր հանգույց կլաստերին.:

`docker swarm join --token {{token}} {{manager_node_url:2377}}`

- Հեռացրեք աշխատողին երամակից (վազում է աշխատողի հանգույցի ներսում).:

`docker swarm leave`

- Ցուցադրել ընթացիկ CA վկայագիրը PEM ձևաչափով.:

`docker swarm ca`

- Պտտեցնել ընթացիկ CA վկայագիրը և ցուցադրել նոր վկայականը.:

`docker swarm ca --rotate`

- Փոխեք հանգույցի վկայագրերի վավեր ժամկետը.:

`docker swarm update --cert-expiry {{hours}}h{{minutes}}m{{seconds}}s`
