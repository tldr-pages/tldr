# դոկեր կոնտեյների գործարկում

> Գործարկեք հրաման նոր Docker կոնտեյներով:.
> Լրացուցիչ տեղեկություններ. <https://docs.docker.com/reference/cli/docker/container/run/>:.

- Գործարկել հրամանը նոր կոնտեյներով պիտակավորված պատկերից.:

`docker {{[run|container run]}} {{image:tag}} {{command}}`

- Գործարկեք հրամանը ֆոնային նոր կոնտեյներով և ցուցադրեք դրա ID-ն.:

`docker {{[run|container run]}} {{[-d|--detach]}} {{image}} {{command}}`

- Գործարկել հրամանը մեկանգամյա կոնտեյներով ինտերակտիվ ռեժիմով և կեղծ TTY.:

`docker {{[run|container run]}} --rm {{[-it|--interactive --tty]}} {{image}} {{command}}`

- Գործարկել հրամանը նոր կոնտեյներով՝ անցած միջավայրի փոփոխականներով.:

`docker {{[run|container run]}} {{[-e|--env]}} '{{variable}}={{value}}' {{[-e|--env]}} {{variable}} {{image}} {{command}}`

- Գործարկել հրամանը նոր կոնտեյներով, որը տեղադրված է կապող ծավալներով.:

`docker {{[run|container run]}} {{[-v|--volume]}} /{{path/to/host_path}}:/{{path/to/container_path}} {{image}} {{command}}`

- Գործարկել հրամանը հրապարակված նավահանգիստներով նոր կոնտեյներով.:

`docker {{[run|container run]}} {{[-p|--publish]}} {{host_port}}:{{container_port}} {{image}} {{command}}`

- Գործարկել հրամանը նոր կոնտեյներով՝ վերագրելով պատկերի մուտքի կետը.:

`docker {{[run|container run]}} --entrypoint {{command}} {{image}}`

- Գործարկել հրամանը ցանցին միացնող նոր կոնտեյներով.:

`docker {{[run|container run]}} --network {{network}} {{image}}`
