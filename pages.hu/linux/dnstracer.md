# dnstracer

> A dnstracer parancs meghatározza, hogy a DNS honnan kapja az információkat. További információ: <https://manned.org/dnstracer>.

- Tudja meg, hogy a helyi DNS honnan kapta az információkat a www.example.com oldalon:

`dnstracer {{www.example.com}}`

- Kezdje egy olyan \[s\]pecific DNS-sel, amelyet már ismer:

`dnstracer -s {{dns.example.org}} {{www.example.com}}`

- Csak IPv4-kiszolgálókat kérdezzen le:

`dnstracer -4 {{www.example.com}}`

- Sikertelenség esetén minden kérést 5-ször próbáljon meg újra:

`dnstracer -r {{5}} {{www.example.com}}`

- Minden lépés megjelenítése a végrehajtás során:

`dnstracer -v {{www.example.com}}`

- Az összes kapott válasz \[o\]verview megjelenítése a végrehajtás után:

`dnstracer -o {{www.example.com}}`
