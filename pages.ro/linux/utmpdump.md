# utmpdump

> Dump și încărcați btmp, utmp și wtmp fișiere contabile.

- Dați fișierul `/var/log/wtmp` la ieșirea standard ca text simplu:

`utmpdump {{/var/log/wtmp}}`

- Încărcați un fișier care a făcut obiectul unui dumping anterior în `/var/log/wtmp`:

`utmpdump -r {{dumpfile}} > {{/var/log/wtmp}}`
