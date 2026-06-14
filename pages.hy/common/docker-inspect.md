# docker ստուգում

> Վերադարձեք ցածր մակարդակի տեղեկատվություն Docker-ի օբյեկտների վերաբերյալ:.
> Լրացուցիչ տեղեկություններ. <https://docs.docker.com/reference/cli/docker/inspect/>:.

- Ցուցադրել կոնտեյների, պատկերի կամ ծավալի մասին տեղեկությունները՝ օգտագործելով անուն կամ ID.:

`docker inspect {{container|image|id}}`

- Ցուցադրել կոնտեյների IP հասցեն.:

`docker inspect {{[-f|--format]}} '\{\{range.NetworkSettings.Networks\}\}\{\{.IPAddress\}\}\{\{end\}\}' {{container}}`

- Ցուցադրել բեռնարկղի գրանցամատյանի ուղին.:

`docker inspect {{[-f|--format]}} '\{\{.LogPath\}\}' {{container}}`

- Ցուցադրել կոնտեյների պատկերի անունը.:

`docker inspect {{[-f|--format]}} '\{\{.Config.Image\}\}' {{container}}`

- Ցուցադրել կազմաձևման տեղեկատվությունը որպես JSON:

`docker inspect {{[-f|--format]}} '\{\{json .Config\}\}' {{container}}`

- Ցուցադրել բոլոր նավահանգիստների կապերը.:

`docker inspect {{[-f|--format]}} '\{\{range $p, $conf := .NetworkSettings.Ports\}\} \{\{$p\}\} -> \{\{(index $conf 0).HostPort\}\} \{\{end\}\}' {{container}}`

- Ցուցադրել օգնությունը.:

`docker inspect`
