# pyflakes

> Ստուգեք Python-ի սկզբնական կոդերի ֆայլերը սխալների համար:.
> Լրացուցիչ տեղեկություններ. <https://pypi.org/project/pyflakes>:.

- Ստուգեք մեկ Python ֆայլ.:

`pyflakes check {{path/to/file.py}}`

- Ստուգեք Python ֆայլերը որոշակի գրացուցակում.:

`pyflakes checkPath {{path/to/directory}}`

- Ստուգեք Python ֆայլերը գրացուցակում ռեկուրսիվ կերպով.:

`pyflakes checkRecursive {{path/to/directory}}`

- Ստուգեք բոլոր Python ֆայլերը, որոնք գտնվել են բազմաթիվ գրացուցակներում.:

`pyflakes iterSourceCode {{path/to/directory_1 path/to/directory_2 ...}}`
