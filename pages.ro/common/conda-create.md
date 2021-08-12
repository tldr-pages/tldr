# conda create

> Creați medii conda noi.
> Mai multe informaţii: <https://docs.conda.io/projects/conda/en/latest/commands/create.html>

- Creați un mediu nou numit `py39` și instalați Python 3.9 și numpy v1.11 sau mai sus în el:

`conda create --yes --name {{py39}} python={{3.9}} "{{numpy>=1.11}}"`

- Faceți o copie exactă a unui mediu:

`conda create --clone {{py39}} --name {{py39-copy}}`

- Creați un mediu nou cu un nume specificat și instalați un pachet dat:

`conda create --name {{env_name}} {{package_name}}`
