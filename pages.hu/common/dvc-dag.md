# dvc dag

> A `dvc.yaml` oldalon meghatározott csővezeték(ek) megjelenítése. További információ: <https://dvc.org/doc/command-reference/dag>.

- A teljes csővezeték vizualizálása:

`dvc dag`

- A csővezeték szakaszainak vizualizálása egy megadott célszakaszig:

`dvc dag {{target}}`

- A csővezeték exportálása pont formátumban:

`dvc dag --dot > {{path/to/pipeline.dot}}`
