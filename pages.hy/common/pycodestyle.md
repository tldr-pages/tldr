# pycodestyle

> Ստուգեք Python կոդը PEP 8 ոճի կոնվենցիաների դեմ:.
> Լրացուցիչ տեղեկություններ. <https://pycodestyle.pycqa.org/en/latest/intro.html#example-usage-and-output>:.

- Ստուգեք մեկ ֆայլի ոճը.:

`pycodestyle {{file.py}}`

- Ստուգեք բազմաթիվ ֆայլերի ոճը.:

`pycodestyle {{file1.py file2.py ...}}`

- Ցույց տալ միայն սխալի առաջին դեպքը.:

`pycodestyle --first {{file.py}}`

- Ցույց տալ աղբյուրի կոդը յուրաքանչյուր սխալի համար.:

`pycodestyle --show-source {{file.py}}`

- Ցույց տվեք PEP 8-ի հատուկ տեքստը յուրաքանչյուր սխալի համար.:

`pycodestyle --show-pep8 {{file.py}}`
