# պարան

> Կոմունալ Python փաթեթներ PyPI-ում հրապարակելու համար:.
> Լրացուցիչ տեղեկություններ. <https://twine.readthedocs.io/en/stable/#commands>:.

- Վերբեռնեք PyPI:

`twine upload dist/*`

- Վերբեռնեք Test PyPI պահոց՝ ստուգելու, թե ինչն է ճիշտ.:

`twine upload {{[-r|--repository]}} testpypi dist/*`

- Վերբեռնեք PyPI-ում նշված օգտվողի անունով և գաղտնաբառով.:

`twine upload {{[-u|--username]}} {{username}} {{[-p|--password]}} {{password}} dist/*`

- Վերբեռնեք այլընտրանքային պահեստի URL.:

`twine upload --repository-url {{repository_url}} dist/*`

- Ստուգեք, որ ձեր բաշխման երկար նկարագրությունը պետք է ճիշտ ներկայացվի PyPI-ում.:

`twine check dist/*`

- Վերբեռնեք հատուկ pypirc կազմաձևման ֆայլի միջոցով.:

`twine upload --config-file {{configuration_file}} dist/*`

- Շարունակեք ֆայլերի վերբեռնումը, եթե դրանք արդեն գոյություն ունեն (վավեր է միայն PyPI-ում վերբեռնելիս).:

`twine upload --skip-existing dist/*`

- Վերբեռնեք PyPI-ին, ցույց տալով մանրամասն տեղեկատվություն.:

`twine upload --verbose dist/*`
