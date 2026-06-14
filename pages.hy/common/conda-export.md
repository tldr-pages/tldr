# conda արտահանում

> Արտահանել շրջակա միջավայրի մանրամասները:.
> Լրացուցիչ տեղեկություններ. <https://docs.conda.io/projects/conda/en/latest/commands/export.html>:.

- Արտահանել ընթացիկ միջավայրի մանրամասները `stdout`:

`conda export`

- Արտահանել ընթացիկ միջավայրի մանրամասները `YAML` ֆայլ.:

`conda export {{[-f|--file]}} {{path/to/environment.yaml}}`

- Արտահանել մանրամասները հատուկ ձևաչափով.:

`conda export --format {{environment-json|environment-yaml|explicit|json|reqs|requirements|txt|yaml|yml}}`

- Թիրախավորեք միջավայրը անունով.:

`conda export {{[-n|--name]}} {{environment_name}}`

- Թիրախավորեք միջավայրն իր ճանապարհով.:

`conda export {{[-p|--prefix]}} {{path/to/environment}}`

- Ներառեք հատուկ ալիք.:

`conda export {{[-c|--channel]}} {{channel_name}}`
