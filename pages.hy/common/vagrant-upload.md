# թափառաշրջիկ վերբեռնում

> Վերբեռնեք ֆայլեր և գրացուցակներ հոսթից դեպի հյուրի մեքենա:.
> Լրացուցիչ տեղեկություններ. <https://developer.hashicorp.com/vagrant/docs/cli/upload>:.

- Վերբեռնեք ֆայլը կամ գրացուցակը հոսթից դեպի հյուրի մեքենա.:

`vagrant upload {{path/to/source_file_or_directory}} {{path/to/destination_file_or_directory}} {{name|id}}`

- Սեղմեք ֆայլը կամ գրացուցակը, նախքան հյուրի մեքենա վերբեռնելը.:

`vagrant upload --compress {{path/to/source_file_or_directory}} {{path/to/destination_file_or_directory}} {{name|id}}`

- Նշեք, թե որ տեսակի սեղմումն օգտագործել: Կանխադրված տեսակն է `zip`:

`vagrant upload --compression-type {{tgz|zip}} {{path/to/source_file_or_directory}} {{path/to/destination_file_or_directory}} {{name|id}}`

- Ստեղծեք ժամանակավոր տեղ հյուրի մեքենայի վրա և ֆայլեր վերբեռնեք այդ վայրում՝:

`vagrant upload --temporary {{path/to/source_file_or_directory}} {{path/to/destination_file_or_directory}} {{name|id}}`
