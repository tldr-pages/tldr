# csvsort

> Տեսակավորել CSV ֆայլերը:.
> Ներառված է csvkit-ում:.
> Լրացուցիչ տեղեկություններ. <https://csvkit.readthedocs.io/en/latest/scripts/csvsort.html>:.

- Տեսակավորեք CSV ֆայլը 9-րդ սյունակով.:

`csvsort {{[-c|--columns]}} {{9}} {{data.csv}}`

- Տեսակավորել CSV ֆայլը ըստ «անուն» սյունակի՝ նվազման կարգով.:

`csvsort {{[-r|--reverse]}} {{[-c|--columns]}} {{name}} {{data.csv}}`

- Տեսակավորեք CSV ֆայլը ըստ սյունակ 2-ի, ապա ըստ սյունակ 4-ի:

`csvsort {{[-c|--columns]}} {{2,4}} {{data.csv}}`

- Տեսակավորել CSV ֆայլը առանց տվյալների տեսակների եզրակացության.:

`csvsort {{[-I|--no-inference]}} {{[-c|--columns]}} {{columns}} {{data.csv}}`
