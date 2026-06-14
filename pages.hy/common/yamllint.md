# yamllint

> Լինտեր YAML ֆայլերի համար:.
> Լրացուցիչ տեղեկություններ. <https://yamllint.readthedocs.io>:.

- Տեղադրեք ֆայլ.:

`yamllint {{path/to/file.yaml}}`

- Բոլոր YAML ֆայլերը գրացուցակում ռեկուրսիվ կերպով տեղադրեք.:

`yamllint {{path/to/directory}}`

- Տեղադրեք ֆայլը հատուկ կազմաձևման ֆայլով.:

`yamllint {{[-c|--config-file]}} {{path/to/config.yaml}} {{path/to/file.yaml}}`

- Տեղադրեք ֆայլը՝ օգտագործելով նախադրված կազմաձևը (`default` կամ `relaxed`):

`yamllint {{[-d|--config-data]}} "{{extends: relaxed}}" {{path/to/file.yaml}}`

- Արդյունք վերլուծելի ձևաչափով (CI ինտեգրման համար).:

`yamllint {{[-f|--format]}} parsable {{path/to/file.yaml}}`

- Փակեք ֆայլը խիստ ռեժիմով (վերադարձեք 2 նախազգուշացումների համար).:

`yamllint {{[-s|--strict]}} {{path/to/file.yaml}}`

- Կարդացեք `stdin`-ից՝:

`cat {{path/to/file.yaml}} | yamllint -`

- Ցուցադրել օգնությունը.:

`yamllint {{[-h|--help]}}`
