# mamba repoquery

> A conda és mamba csomagtárak és csomagfüggőségek hatékony lekérdezése. További információ: <https://mamba.readthedocs.io/en/latest/user_guide/mamba.html#repoquery>.

- Egy adott csomag összes elérhető verziójának keresése:

`mamba repoquery search {{package_name}}`

- Az összes olyan csomag keresése, amely megfelel bizonyos korlátozásoknak:

`mamba repoquery search {{sphinx<5}}`

- Az aktuálisan aktivált környezetbe telepített csomag függőségeinek listázása fa formátumban:

`mamba repoquery depends --tree {{scipy}}`

- Az aktuális környezetben lévő olyan csomagok nyomtatása, amelyek egy adott csomag telepítését igénylik (azaz a `depends` fordítottja):

`mamba repoquery whoneeds {{ipython}}`
