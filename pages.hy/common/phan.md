# ֆան

> PHP-ի ստատիկ վերլուծության գործիք:.
> Լրացուցիչ տեղեկություններ. <https://github.com/phan/phan>:.

- Ստեղծեք `.phan/config.php` ընթացիկ գրացուցակում.:

`phan --init`

- Ստեղծեք Phan-ի կազմաձևման ֆայլ՝ օգտագործելով որոշակի մակարդակ (1-ը ամենախիստից մինչև 5-ը՝ ամենաքիչը).:

`phan --init --init-level {{level}}`

- Վերլուծեք ընթացիկ գրացուցակը.:

`phan`

- Վերլուծեք մեկ կամ մի քանի գրացուցակներ.:

`phan {{--directory path/to/directory1 --directory path/to/directory2 ...}}`

- Նշեք կազմաձևման ֆայլը (կանխադրված է `.phan/config.php`):

`phan --config-file {{path/to/config.php}}`

- Նշեք ելքային ռեժիմը.:

`phan --output-mode {{text|verbose|json|csv|codeclimate|checkstyle|pylint|html}}`

- Նշեք զուգահեռ գործընթացների քանակը.:

`phan --processes {{number_of_processes}}`
