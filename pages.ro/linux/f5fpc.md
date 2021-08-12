# f5fpc

> Un client propriu SSL VPN comercial de BIG-IP Edge.
> Mai multe informaţii: <https://techdocs.f5.com/kb/en-us/products/big-ip_apm/manuals/product/apm-client-configuration-11-4-0/4.html>

- Deschideți o nouă conexiune VPN:

`sudo f5fpc --start`

- Deschideți o nouă conexiune VPN la o anumită gazdă:

`sudo f5fpc --start --host {{host.example.com}}`

- Specificați un nume de utilizator (utilizatorul va fi solicitat pentru o parolă):

`sudo f5fpc --start --host {{host.example.com}} --username {{user}}`

- Afișează starea curentă VPN:

`sudo f5fpc --info`

- Opriți conexiunea VPN:

`sudo f5fpc --stop`
