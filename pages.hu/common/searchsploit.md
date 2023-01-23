# searchsploit

> A Searchsploit az exploit adatbázis adatbázisában keres exploitokat, shellkódokat és/vagy papírokat. Ha ismert verziószámokat használunk keresési feltételként, akkor a pontos verzióra vonatkozó exploitok és olyanok is megjelennek, amelyek verzióköre a megadott verzióra terjed ki. További információ: <https://www.exploit-db.com/searchsploit>.

- Exploit, shellcode vagy dokumentum keresése:

`searchsploit {{search_terms}}`

- Egy ismert konkrét verzió keresése, pl. sudo 1.8.27-es verzió:

`searchsploit sudo 1.8.27`

- Megjeleníti a megtalált erőforrások exploit-db linkjét:

`searchsploit --www {{search_terms}}`

- Készítsen másolatot az erőforrásról az aktuális könyvtárba (az exploit száma szükséges):

`searchsploit --mirror {{exploit_number}}`

- Nyissa meg az erőforrást az olvasáshoz a `$PAGER` környezeti változóban meghatározott pagerrel:

`searchsploit --explore {{exploit_number}}`

- A helyi exploit adatbázis frissítése:

`searchsploit --update`
