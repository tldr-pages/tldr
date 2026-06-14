#ընթերցող

> Կարդացեք տողերը `stdin`-ից զանգվածի մեջ:.
> Լրացուցիչ տեղեկություններ. <https://www.gnu.org/software/bash/manual/bash.html#index-readarray>:.

- Ինտերակտիվ կերպով մուտքագրեք տողերը զանգվածի մեջ.:

`readarray {{array_name}}`

- Կարդացեք տողերը ֆայլից և տեղադրեք դրանք զանգվածի մեջ.:

`readarray < {{path/to/file.txt}} {{array_name}}`

- Հեռացրեք [t] railing deliminators (նոր գիծը լռելյայն).:

`readarray < {{path/to/file.txt}} -t {{array_name}}`

- Պատճենել առավելագույնը `n` տող.:

`readarray < {{path/to/file.txt}} -n {{n}} {{array_name}}`

- [s]բաց թողեք առաջին `n` տողերը՝:

`readarray < {{path/to/file.txt}} -s {{n}} {{array_name}}`

- Սահմանեք սովորական [d]սահմանափակիչ.:

`readarray < {{path/to/file.txt}} -d {{delimiter}} {{array_name}}`

- Ցուցադրել օգնությունը.:

`help mapfile`
