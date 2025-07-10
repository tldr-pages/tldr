# mkdir

> Maak mappen aan en stel hun permissies in.
> Meer informatie: <https://www.gnu.org/software/coreutils/manual/html_node/mkdir-invocation.html>.

- Maak specifieke mappen aan:

`mkdir {{pad/naar/map1 pad/naar/map2 ...}}`

- Maak specifieke mappen en hun ouders aan indien nodig:

`mkdir {{[-p|--parents]}} {{pad/naar/map1 pad/naar/map2 ...}}`

- Maak mappen aan met specifieke permissies:

`mkdir {{[-m|--mode]}} {{rwxrw-r--}} {{pad/naar/map1 pad/naar/map2 ...}}`

- Maak meerdere geneste mappen recursief:

`mkdir {{[-p|--parents]}} {{path/to/{a,b}/{x,y,z}/{h,i,j}}}`
