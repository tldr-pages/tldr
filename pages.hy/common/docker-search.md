# դոկերի որոնում

> Որոնեք Docker պատկերներ Docker Hub-ում:.
> Լրացուցիչ տեղեկություններ. <https://docs.docker.com/reference/cli/docker/search/>:.

- Որոնեք Docker պատկերները անունով կամ հիմնաբառով.:

`docker search {{keyword}}`

- Որոնեք պատկերներ և ցուցադրեք միայն պաշտոնականները.:

`docker search {{[-f|--filter]}} is-official=true {{keyword}}`

- Որոնեք պատկերներ և ցուցադրեք միայն ավտոմատացված շինությունները.:

`docker search {{[-f|--filter]}} is-automated=true {{keyword}}`

- Որոնեք նկարներ նվազագույն թվով աստղերով.:

`docker search {{[-f|--filter]}} stars={{number}} {{keyword}}`

- Սահմանափակեք արդյունքների քանակը.:

`docker search --limit {{number}} {{keyword}}`

- Անհատականացրեք ելքային ձևաչափը.:

`docker search {{[-f|--format]}} "{{.Name}}: {{.Description}}" {{keyword}}`
