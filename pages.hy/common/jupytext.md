# jupytext

> Փոխակերպեք Jupyter-ի նոթատետրերը պարզ տեքստային փաստաթղթերի և նորից հետ:.
> Լրացուցիչ տեղեկություններ. <https://jupytext.readthedocs.io/en/latest/using-cli.html>:.

- Նոթատետրը վերածեք զուգակցված `.ipynb`/`.py` նոթատետրի.:

`jupytext --set-formats ipynb,py {{path/to/notebook}}.ipynb`

- Նոութբուքը փոխարկեք `.py` ֆայլի.:

`jupytext --to py {{path/to/notebook}}.ipynb`

- Փոխարկեք `.py` ֆայլը նոթատետրի առանց ելքերի.:

`jupytext --to notebook {{path/to/notebook}}.py`

- Փոխակերպեք `.md` ֆայլը նոթատետր և գործարկեք այն.:

`jupytext --to notebook --execute {{path/to/notebook}}.md`

- Թարմացրեք մուտքային բջիջները նոթատետրում և պահպանեք ելքերը և մետատվյալները.:

`jupytext --update --to notebook {{path/to/notebook}}.py`

- Թարմացրեք նոթատետրի բոլոր զուգակցված ներկայացումները.:

`jupytext {{[-s|--sync]}} {{path/to/notebook}}.ipynb`
