# guacd

> Apache Guacamole proxy démon. Támogatja a kliens pluginok betöltését a Guacamole protokoll és bármely tetszőleges távoli asztali protokoll (pl. RDP, VNC, egyéb) közötti interfészhez. További információ: https: [//guacamole.apache.org/](https://guacamole.apache.org/).

- A localhost egy adott portjához való kötés:

`guacd -b {{127.0.0.1}} -l {{4823}}`

- Indítás hibakeresési módban, a folyamatot előtérben tartva:

`guacd -f -L {{debug}}`

- TLS-támogatással indítson:

`guacd -C {{my-cert.crt}} -K {{my-key.pem}}`

- Írja a PID azonosítót egy fájlba:

`guacd -p {{path/to/file.pid}}`
