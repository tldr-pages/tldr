# autopep8

> Ձևաչափեք Python կոդը ըստ PEP 8 ոճի ուղեցույցի:.
> Լրացուցիչ տեղեկություններ. <https://github.com/hhatto/autopep8>:.

- Ձևաչափեք ֆայլը `stdout`-ի, հատուկ տողի առավելագույն երկարությամբ.:

`autopep8 {{path/to/file.py}} --max-line-length {{length}}`

- Ֆայլի ֆորմատավորում՝ ցուցադրելով փոփոխությունների տարբերությունը.:

`autopep8 --diff {{path/to/file}}`

- Ձևաչափեք ֆայլը տեղում և պահպանեք փոփոխությունները.:

`autopep8 --in-place {{path/to/file.py}}`

- Ռեկուրսիվ ձևաչափեք բոլոր ֆայլերը գրացուցակում և պահպանեք փոփոխությունները.:

`autopep8 --in-place --recursive {{path/to/directory}}`
