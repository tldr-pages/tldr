# pip տեղադրում

> Տեղադրեք Python փաթեթներ:.
> Լրացուցիչ տեղեկություններ. <https://pip.pypa.io/en/stable/cli/pip_install/>:.

- Տեղադրեք մեկ կամ մի քանի փաթեթ.:

`pip install {{package1 package2 ...}}`

- Թարմացրեք բոլոր նշված փաթեթները վերջին տարբերակին, տեղադրելով այն, որն արդեն առկա չէ.:

`pip install {{package1 package2 ...}} {{[-U|--upgrade]}}`

- Տեղադրեք փաթեթի որոշակի տարբերակ.:

`pip install {{package}}=={{version}}`

- Տեղադրեք ֆայլում թվարկված փաթեթները.:

`pip install {{[-r|--requirement]}} {{path/to/requirements.txt}}`

- Տեղադրեք փաթեթ տեղական արխիվից կամ գրացուցակից.:

`pip install {{path/to/file.whl|path/to/file.tar.gz|path/to/directory}}`

- Տեղադրեք փաթեթ Git պահոցից.:

`pip install git+https://{{example.com}}/{{user}}/{{repository}}.git`

- Տեղադրեք փաթեթ այլընտրանքային աղբյուրից (URL կամ գրացուցակ) PyPI-ի փոխարեն.:

`pip install {{[-f|--find-links]}} {{url|path/to/directory}} {{package}}`

- Տեղադրեք տեղական փաթեթը ընթացիկ գրացուցակում մշակման (խմբագրելի) ռեժիմում.:

`pip install {{[-e|--editable]}} .`
