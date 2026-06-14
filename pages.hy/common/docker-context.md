# դոկերի համատեքստ

> Անցեք համատեքստերի միջև՝ Docker-ի բազմաթիվ միջավայրերը կառավարելու համար:.
> Լրացուցիչ տեղեկություններ. <https://docs.docker.com/reference/cli/docker/context/>:.

- Ստեղծեք համատեքստ՝ օգտագործելով Docker-ի կոնկրետ վերջնակետը.:

`docker context create {{context_name}} --docker "host={{tcp://remote-host:2375}}"`

- Ստեղծեք համատեքստ՝ հիմնված `$DOCKER_HOST` միջավայրի փոփոխականի վրա.:

`docker context create {{context_name}}`

- Անցում համատեքստի.:

`docker context use {{context_name}}`

- Թվարկեք բոլոր համատեքստերը.:

`docker context ls`
