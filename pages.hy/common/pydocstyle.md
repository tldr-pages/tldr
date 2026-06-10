# pydocstyle

> Ստատիկորեն ստուգեք Python-ի սկրիպտները՝ Python-ի վավերագրման կոնվենցիաներին համապատասխանելու համար:.
> Լրացուցիչ տեղեկություններ. <https://www.pydocstyle.org/en/latest/>:.

- Վերլուծեք Python-ի սցենարը կամ Python-ի բոլոր սկրիպտները կոնկրետ գրացուցակում.:

`pydocstyle {{file.py|path/to/directory}}`

- Ցույց տվեք յուրաքանչյուր սխալի բացատրությունը.:

`pydocstyle {{[-e|--explain]}} {{file.py|path/to/directory}}`

- Ցուցադրել վրիպազերծման տեղեկատվությունը.:

`pydocstyle {{[-d|--debug]}} {{file.py|path/to/directory}}`

- Ցուցադրել սխալների ընդհանուր թիվը.:

`pydocstyle --count {{file.py|path/to/directory}}`

- Օգտագործեք հատուկ կազմաձևման ֆայլ.:

`pydocstyle --config {{path/to/config_file}} {{file.py|path/to/directory}}`

- Անտեսել մեկ կամ մի քանի սխալ.:

`pydocstyle --ignore {{D101,D2,D107,...}} {{file.py|path/to/directory}}`

- Ստուգեք որոշակի կոնվենցիայի սխալների համար.:

`pydocstyle --convention {{pep257|numpy|google}} {{file.py|path/to/directory}}`
