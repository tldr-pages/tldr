#առջուն

> Բացահայտեք HTTP պարամետրերը վեբ հավելվածների համար:.
> Լրացուցիչ տեղեկություններ. <https://github.com/s0md3v/Arjun/wiki/Usage>:.

- Սկանավորեք URL՝ GET պարամետրերի համար.:

`arjun -u {{https://example.com/page.php}}`

- Սկանավորեք POST մեթոդով.:

`arjun -u {{https://example.com/api}} -m POST`

- Պահպանեք հայտնաբերված պարամետրերը JSON ֆայլում.:

`arjun -u {{https://example.com}} -o {{path/to/output.json}}`

- Օգտագործեք հատուկ բառացանկ.:

`arjun -u {{https://example.com}} -w {{path/to/wordlist.txt}}`

- Բարձրացրեք հարցումների հետաձգումը որոշակի վայրկյաններով, որպեսզի խուսափեք տոկոսադրույքի սահմանափակումից.:

`arjun -u {{https://example.com}} -d {{2}}`
