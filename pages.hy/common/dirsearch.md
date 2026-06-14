#փնտրում

> Վեբ ուղու սկաներ:.
> Լրացուցիչ տեղեկություններ. <https://github.com/maurosoria/dirsearch#options>:.

- Սկանավորեք վեբ սերվերը ընդհանուր ընդլայնումներով ընդհանուր ուղիների համար.:

`dirsearch {{[-u|--url]}} {{url}} --extensions-list`

- Սկանավորեք վեբ սերվերների ցուցակը տվյալ ֆայլի ընդարձակմամբ ընդհանուր ուղիների համար.:

`dirsearch {{[-l|--url-list]}} {{path/to/url-list.txt}} {{[-e|--extensions]}} {{php,jsp,aspx,...}}`

- Սկանավորեք վեբ սերվերը օգտագործողի կողմից սահմանված ուղիների համար՝ ընդհանուր ընդլայնումներով.:

`dirsearch {{[-u|--url]}} {{url}} --extensions-list {{[-w|--wordlists]}} {{path/to/url-paths1.txt,path/to/url-paths2.txt,...}}`

- Սկանավորեք վեբ սերվերը՝ օգտագործելով թխուկ.:

`dirsearch {{[-u|--url]}} {{url}} {{[-e|--extensions]}} {{php}} --cookie {{cookie}}`

- Սկանավորեք վեբ սերվերը՝ օգտագործելով `HEAD` HTTP մեթոդը.:

`dirsearch {{[-u|--url]}} {{url}} {{[-e|--extensions]}} {{php}} {{[-m|--http-method]}} {{HEAD}}`

- Սկանավորեք վեբ սերվերը՝ արդյունքները պահելով `.json` ֆայլում՝:

`dirsearch {{[-u|--url]}} {{url}} {{[-e|--extensions]}} {{php}} --json-report {{path/to/report.json}}`
