# unzip

> Քաղեք ֆայլեր/տեղեկատուներ Zip արխիվներից:.
> Տես նաև՝ `zip`:.
> Լրացուցիչ տեղեկություններ. <https://manned.org/unzip>:.

- Բոլոր ֆայլերը / գրացուցակները հանեք հատուկ արխիվներից ընթացիկ գրացուցակում.:

`unzip {{path/to/archive1.zip path/to/archive2.zip ...}}`

- Արխիվներից հանեք ֆայլերը/տեղեկատուները կոնկրետ ուղու վրա.:

`unzip {{path/to/archive1.zip path/to/archive2.zip ...}} -d {{path/to/output}}`

- Արտահանեք ֆայլերը/տեղեկատուները արխիվներից `stdout`՝ արդյունահանված ֆայլերի անունների հետ մեկտեղ.:

`unzip -c {{path/to/archive1.zip path/to/archive2.zip ...}}`

- Քաղեք Windows-ում ստեղծված արխիվը, որը պարունակում է ոչ ASCII (օրինակ՝ չինական կամ ճապոնական նիշ) ֆայլերի անուններով ֆայլեր.:

`unzip -O {{gbk}} {{path/to/archive1.zip path/to/archive2.zip ...}}`

- Թվարկեք կոնկրետ արխիվի բովանդակությունը՝ առանց դրանք հանելու.:

`unzip -l {{path/to/archive}}.zip`

- Արտահանեք հատուկ ֆայլեր արխիվից.:

`unzip -j {{path/to/archive}}.zip {{path/to/file1_in_archive path/to/file2_in_archive ...}}`
