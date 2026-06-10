# php- ծածկոց

> PHP-հաճախորդ համազգեստի համար:.
> Լրացուցիչ տեղեկություններ. <https://php-coveralls.github.io/php-coveralls/#cli-options>:.

- Ուղարկեք ծածկույթի մասին տեղեկատվություն ծածկոցներին.:

`php-coveralls`

- Ուղարկեք ծածկույթի մասին տեղեկատվություն Կոմբինատներին հատուկ գրացուցակի համար.:

`php-coveralls {{[-r|--root_dir]}} {{path/to/directory}}`

- Ուղարկեք ծածկույթի մասին տեղեկատվություն Կոմբինատներին հատուկ կազմաձևով.:

`php-coveralls {{[-c|--config]}} {{path/to/.coveralls.yml}}`

- Ուղարկեք ծածկույթի մասին տեղեկատվություն կոմբինեզոններին՝ մանրամասն ելքով.:

`php-coveralls {{[-v|--verbose]}}`

- Ուղարկեք ծածկույթի մասին տեղեկատվություն Coveralls-ին՝ բացառելով սկզբնական ֆայլերը՝ առանց գործարկվող հայտարարությունների.:

`php-coveralls --exclude-no-stmt`

- Ուղարկեք ծածկույթի մասին տեղեկատվություն Կոմբինատներին հատուկ միջավայրի անունով.:

`php-coveralls {{[-e|--env]}} {{test|dev|prod}}`

- Նշեք մի քանի Coverage Clover XML ֆայլեր վերբեռնելու համար.:

`php-coveralls {{[-x|--coverage_clover]}} {{path/to/first_clover.xml}} --coverage_clover {{path/to/second_clover.xml}}`

- Արտադրեք JSON-ը, որը կուղարկվի Coveralls-ին որոշակի ֆայլ.:

`php-coveralls {{[-o|--json_path]}} {{path/to/coveralls-upload.json}}`
