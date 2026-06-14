# sqlmap

> Հայտնաբերել և օգտագործել SQL ներարկման թերությունները:.
> Լրացուցիչ տեղեկություններ. <https://github.com/sqlmapproject/sqlmap/wiki/Usage>:.

- Գործարկեք sqlmap-ը մեկ թիրախային URL-ի դեմ.:

`python sqlmap.py {{[-u|--url]}} "{{http://www.example.com/vuln.php?id=1}}"`

- Ուղարկեք տվյալներ POST հարցումով (`--data` ենթադրում է POST հարցում).:

`python sqlmap.py {{[-u|--url]}} "{{http://www.example.com/vuln.php}}" --data="{{id=1}}"`

- Փոխեք պարամետրի սահմանազատիչը (&-ը լռելյայն է).:

`python sqlmap.py {{[-u|--url]}} "{{http://www.example.com/vuln.php}}" --data="{{query=foobar;id=1}}" --param-del="{{;}}"`

- Ընտրեք պատահական `User-Agent` `./txt/user-agents.txt`-ից և օգտագործեք այն՝:

`python sqlmap.py {{[-u|--url]}} "{{http://www.example.com/vuln.php}}" --random-agent`

- Տրամադրել օգտվողի հավատարմագրերը HTTP արձանագրության նույնականացման համար.:

`python sqlmap.py {{[-u|--url]}} "{{http://www.example.com/vuln.php}}" --auth-type {{Basic}} --auth-cred "{{testuser:testpass}}"`
