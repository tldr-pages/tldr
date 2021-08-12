# sqlmap

> Detectați și exploatați defectele de injectare SQL.
> Mai multe informaţii: <https://sqlmap.org>

- Rulați sqlmap împotriva unui singur URL țintă:

`python sqlmap.py -u "{{http://www.target.com/vuln.php?id=1}}"`

- Trimiterea datelor într-o cerere POST (`—data` presupune solicitarea POST):

`python sqlmap.py -u "{{http://www.target.com/vuln.php}}" --data="{{id=1}}"`

- Modificați parametrul delimitator (& este implicit):

`python sqlmap.py -u "{{http://www.target.com/vuln.php}}" --data="{{query=foobar;id=1}}" --param-del="{{;}}"`

- Selectaţi aleatoriu `User-agent` de la `. /txt/user-agents.txt `și utilizați-l:

`python sqlmap.py -u "{{http://www.target.com/vuln.php}}" --random-agent`

- Furnizarea acreditărilor de utilizator pentru autentificarea protocolului HTTP:

`python sqlmap.py -u "{{http://www.target.com/vuln.php}}" --auth-type {{Basic}} --auth-cred "{{testuser:testpass}}"`
