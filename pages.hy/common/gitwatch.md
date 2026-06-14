# gitwatch

> Ավտոմատ կերպով կատարել ֆայլի կամ գրացուցակի փոփոխությունները Git պահոցում:.
> Լրացուցիչ տեղեկություններ. <https://github.com/gitwatch/gitwatch>:.

- Ավտոմատ կերպով կատարել ցանկացած փոփոխություն, որը կատարվել է ֆայլում կամ գրացուցակում.:

`gitwatch {{path/to/file_or_directory}}`

- Ավտոմատ կերպով կատարեք փոփոխությունները և դրանք մղեք հեռավոր պահեստ.:

`gitwatch -r {{remote_name}} {{path/to/file_or_directory}}`

- Ավտոմատ կերպով կատարեք փոփոխությունները և դրանք մղեք հեռավոր պահեստի որոշակի մասնաճյուղ.:

`gitwatch -r {{remote_name}} -b {{branch_name}} {{path/to/file_or_directory}}`
