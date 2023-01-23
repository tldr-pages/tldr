# sqlmap

> SQL-injekciós hibák felderítése és kihasználása. További információ: <https://sqlmap.org>.

- Az sqlmap futtatása egyetlen cél URL-cím ellen:

`python sqlmap.py -u "{{http://www.target.com/vuln.php?id=1}}"`

- Adatok küldése POST-kérelemben (`--data` implies POST request):

`python sqlmap.py -u "{{http://www.target.com/vuln.php}}" --data="{{id=1}}"`

- Változtassa meg a paraméterek elválasztójelét (az & az alapértelmezett):

`python sqlmap.py -u "{{http://www.target.com/vuln.php}}" --data="{{query=foobar;id=1}}" --param-del="{{;}}"`

- Véletlenszerű `User-Agent` kiválasztása a `./txt/user-agents.txt` oldalról és használata:

`python sqlmap.py -u "{{http://www.target.com/vuln.php}}" --random-agent`

- Adja meg a HTTP protokoll hitelesítéséhez szükséges felhasználói hitelesítő adatokat:

`python sqlmap.py -u "{{http://www.target.com/vuln.php}}" --auth-type {{Basic}} --auth-cred "{{testuser:testpass}}"`
