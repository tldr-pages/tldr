#գոբաստեր

> Վեբ սերվերների վրա թաքնված ուղիները կոպիտ ուժի մեջ է և ավելին:.
> Լրացուցիչ տեղեկություններ. <https://github.com/OJ/gobuster#modes>:.

- Բացահայտեք դիրեկտորիաներ և ֆայլեր, որոնք համընկնում են բառացանկում.:

`gobuster dir {{[-u|--url]}} {{https://example.com/}} {{[-w|--wordlist]}} {{path/to/file}}`

- Բացահայտեք ենթադոմեյնները.:

`gobuster dns {{[-d|--domain]}} {{example.com}} {{[-w|--wordlist]}} {{path/to/file}}`

- Բացահայտեք Amazon S3 դույլերը.:

`gobuster s3 {{[-w|--wordlist]}} {{path/to/file}}`

- Բացահայտեք այլ վիրտուալ հոսթեր սերվերի վրա.:

`gobuster vhost {{[-u|--url]}} {{https://example.com/}} {{[-w|--wordlist]}} {{path/to/file}}`

- Անջատեք պարամետրի արժեքը.:

`gobuster fuzz {{[-u|--url]}} {{https://example.com/?parameter=FUZZ}} {{[-w|--wordlist]}} {{path/to/file}}`

- Շփոթեք պարամետրի անունը.:

`gobuster fuzz {{[-u|--url]}} {{https://example.com/?FUZZ=value}} {{[-w|--wordlist]}} {{path/to/file}}`
