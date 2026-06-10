# podman run

> Գործարկել հրաման նոր Podman կոնտեյներով:.
> Լրացուցիչ տեղեկություններ. <https://docs.podman.io/en/latest/markdown/podman-run.1.html>:.

- Գործարկել հրամանը նոր կոնտեյներով պիտակավորված պատկերից.:

`podman run {{image:tag}} {{command}}`

- Գործարկեք հրամանը ֆոնային նոր կոնտեյներով և ցուցադրեք դրա ID-ն.:

`podman run {{[-d|--detach]}} {{image:tag}} {{command}}`

- Գործարկել հրամանը մեկանգամյա կոնտեյներով ինտերակտիվ ռեժիմով և կեղծ TTY.:

`podman run --rm {{[-it|--interactive --tty]}} {{image:tag}} {{command}}`

- Գործարկել հրամանը նոր կոնտեյներով՝ անցած միջավայրի փոփոխականներով.:

`podman run {{[-e|--env]}} '{{variable}}={{value}}' {{[-e|--env]}} {{variable}} {{image:tag}} {{command}}`

- Գործարկել հրամանը նոր կոնտեյներով, որը տեղադրված է կապող ծավալներով.:

`podman run {{[-v|--volume]}} /{{path/to/host_path}}:/{{path/to/container_path}} {{image:tag}} {{command}}`

- Գործարկել հրամանը հրապարակված նավահանգիստներով նոր կոնտեյներով.:

`podman run {{[-p|--publish]}} {{host_port}}:{{container_port}} {{image:tag}} {{command}}`

- Գործարկել հրամանը նոր կոնտեյներով՝ վերագրելով պատկերի մուտքի կետը.:

`podman run --entrypoint {{command}} {{image:tag}}`

- Գործարկել հրամանը ցանցին միացնող նոր կոնտեյներով.:

`podman run --network {{network}} {{image:tag}}`
