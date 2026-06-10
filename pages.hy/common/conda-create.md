# conda ստեղծել

> Ստեղծեք նոր կոնդա միջավայրեր:.
> Լրացուցիչ տեղեկություններ. <https://docs.conda.io/projects/conda/en/latest/commands/create.html>:.

- Ստեղծեք նոր միջավայր՝ `py39` անունով, դրա մեջ տեղադրեք Python 3.9, NumPy v1.11 կամ ավելի բարձր և SciPy-ի վերջին կայուն տարբերակը: Ասեք այո բոլոր հաստատումներին.:

`conda create {{[-ny|--name --yes]}} py39 python=3.9 "numpy>=1.11 scipy"`

- Ստեղծեք նոր միջավայր `myenv` անունով և տեղադրեք ֆայլերում թվարկված փաթեթներ.:

`conda create {{[-n|--name]}} myenv --file {{file1.yml}} --file {{file2.yml}}`

- Ստեղծեք նոր միջավայր հատուկ ճանապարհով (այսինքն՝ նախածանց).:

`conda create {{[-p|--prefix]}} {{path/to/myenv}}`

- Ստեղծեք `py39` անունով միջավայրի ճշգրիտ պատճենը՝:

`conda create --clone py39 {{[-n|--name]}} {{py39-copy}}`

- Ցուցադրել օգնությունը.:

`conda create {{[-h|--help]}}`
