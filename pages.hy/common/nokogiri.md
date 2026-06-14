# nokogiri

> HTML, XML, SAX և Reader վերլուծիչ:.
> Լրացուցիչ տեղեկություններ. <https://manned.org/nokogiri>:.

- Վերլուծեք URL-ի կամ ֆայլի բովանդակությունը.:

`nokogiri {{url|path/to/file}}`

- Վերլուծել որպես հատուկ տեսակ.:

`nokogiri {{url|path/to/file}} --type {{xml|html}}`

- Բեռնել որոշակի սկզբնավորման ֆայլ նախքան վերլուծելը.:

`nokogiri {{url|path/to/file}} -C {{path/to/config_file}}`

- Վերլուծել՝ օգտագործելով հատուկ կոդավորում.:

`nokogiri {{url|path/to/file}} {{[-E|--encoding]}} {{encoding}}`

- Վավերացրեք RELAX NG ֆայլի միջոցով.:

`nokogiri {{url|path/to/file}} --rng {{url|path/to/file}}`
