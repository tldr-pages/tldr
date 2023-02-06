# drupal-check

> Ellenőrizze a Drupal PHP kódját az értékvesztések tekintetében. További információ: <https://github.com/mglaman/drupal-check>.

- Ellenőrizze a kódot egy adott könyvtárban a deprecations szempontjából:

`drupal-check {{path/to/directory}}`

- Ellenőrizze a kódot, kivéve egy vesszővel elválasztott könyvtárak listáját:

`drupal-check --exclude-dir {{path/to/excluded_directory}},{{path/to/excluded_files/*.php}} {{path/to/directory}}`

- Ne jelenítsen meg előrehaladási sávot:

`drupal-check --no-progress {{path/to/directory}}`

- Végezzen statikus elemzést a rossz kódolási gyakorlatok felderítésére:

`drupal-check --analysis {{path/to/directory}}`
