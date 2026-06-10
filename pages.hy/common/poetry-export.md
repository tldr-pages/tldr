# պոեզիայի արտահանում

> Արտահանել Poetry-ի կողպեքի ֆայլը այլ ձևաչափերով:.
> Տրամադրվում է Export Poetry Plugin-ի կողմից:.
> Լրացուցիչ տեղեկություններ. <https://github.com/python-poetry/poetry-plugin-export#usage>:.

- Արտահանել կախվածությունները `requirements.txt` ֆայլ՝:

`poetry export {{[-o|--output]}} {{requirements.txt}}`

- Արտահանման կախվածությունը, ներառյալ զարգացման կախվածությունը.:

`poetry export {{[-o|--output]}} {{requirements-dev.txt}} --dev`

- Արտահանեք կախվածություններ առանց հեշերի.:

`poetry export {{[-o|--output]}} {{requirements.txt}} --without-hashes`

- Արտահանել կախվածությունը որոշակի ձևաչափի համար.:

`poetry export {{[-o|--output]}} {{requirements.txt}} {{[-f|--format]}} {{requirements.txt}}`

- Արտահանել միայն հատուկ կախվածության խմբեր.:

`poetry export {{[-o|--output]}} {{requirements.txt}} --only {{main}}`

- Ցուցադրել օգնությունը.:

`poetry export {{[-h|--help]}}`
