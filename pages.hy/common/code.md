# կոդ

> Խաչաձև հարթակ և ընդարձակվող կոդերի խմբագիր:.
> Լրացուցիչ տեղեկություններ. <https://code.visualstudio.com/docs/configure/command-line>:.

- Սկսեք Visual Studio կոդը.:

`code`

- Բացեք հատուկ ֆայլեր/տեղեկատուներ.:

`code {{path/to/file_or_directory1 path/to/file_or_directory2 ...}}`

- Համեմատեք երկու կոնկրետ ֆայլեր.:

`code {{[-d|--diff]}} {{path/to/file1}} {{path/to/file2}}`

- Բացեք հատուկ ֆայլեր/տեղեկատուներ նոր պատուհանում.:

`code {{[-n|--new-window]}} {{path/to/file_or_directory1 path/to/file_or_directory2 ...}}`

- Տեղադրեք/տեղահանեք հատուկ ընդլայնում.:

`code --{{install|uninstall}}-extension {{publisher.extension}}`

- Ցուցադրել ախտորոշիչ և գործընթացային տեղեկատվություն գործող կոդի պատուհանի մասին.:

`code {{[-s|--status]}}`

- Տպեք տեղադրված ընդլայնումները իրենց տարբերակներով.:

`code --list-extensions --show-versions`

- Սկսեք խմբագրիչը որպես գերօգտագործող (արմատ)՝ օգտատիրոջ տվյալները որոշակի գրացուցակում պահելիս.:

`sudo code --user-data-dir {{path/to/directory}}`
