# rdesktop

> client Protocol Desktop la distanță.
> Poate fi utilizat pentru a conecta computerul la distanță utilizând protocolul RDP.

- Conectați-vă la un computer la distanță (portul implicit este 3389):

`rdesktop -u {{username}} -p {{password}} {{host:port}}`

- Exemple simple:

`rdesktop -u Administrator -p passwd123 192.168.1.111:3389`

- Conectați-vă la un computer la distanță cu ecran complet (apăsați „Ctrl + Alt + Enter” pentru a exista):

`rdesktop -u {{username}} -p {{password}} -f {{host:port}}`

- Utilizați rezoluția personalizată (utilizați litera „x” între număr):

`rdesktop -u {{username}} -p {{password}} -g 1366x768 {{host:port}}`

- Conectarea la un computer la distanță utilizând utilizator de domeniu:

`rdesktop -u {{username}} -p {{password}} -d {{domainname}} {{host:port}}`

- Utilizați culoarea 16 biți (accelerați):

`rdesktop -u {{username}} -p {{password}} -a 16 {{host:port}}`
