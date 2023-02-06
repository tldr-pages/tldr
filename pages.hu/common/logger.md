# logger

> Üzenetek hozzáadása a sysloghoz (/var/log/syslog). További információ: <https://manned.org/logger>.

- Üzenet naplózása a syslogba:

`logger {{message}}`

- A `stdin` oldalról történő bevitel és naplózás a syslogba:

`echo {{log_entry}} | logger`

- A kimenetet küldje el egy adott porton futó távoli syslog-kiszolgálónak. Az alapértelmezett port az 514-es:

`echo {{log_entry}} | logger --server {{hostname}} --port {{port}}`

- Használjon egy adott címkét minden naplózott sorhoz. Alapértelmezett a bejelentkezett felhasználó neve:

`echo {{log_entry}} | logger --tag {{tag}}`

- Naplózza az üzeneteket adott prioritással. Az alapértelmezett érték: `user.notice`. Az összes prioritási opciót lásd a `man logger` oldalon:

`echo {{log_entry}} | logger --priority {{user.warning}}`
