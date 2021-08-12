# guacd

> Apache Guacamole daemon proxy.
> Încărcător de suport pentru pluginurile client pentru interfața între protocolul Guacamole și orice protocol arbitrar desktop la distanță (de exemplu, RDP, VNC, Altele).
> Mai multe informaţii: <https://guacamole.apache.org/>

- Legați la un anumit port pe localhost:

`guacd -b {{127.0.0.1}} -l {{4823}}`

- Porniți în modul de depanare, păstrând procesul în prim-plan:

`guacd -f -L {{debug}}`

- Începeți cu suport TLS:

`guacd -C {{my-cert.crt}} -K {{my-key.pem}}`

- Scrieți PID-ul într-un fișier:

`guacd -p {{path/to/file.pid}}`
