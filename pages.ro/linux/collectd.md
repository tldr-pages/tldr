# collectd

> Statisticile sistemului de colectare daemon.
> Mai multe informaţii: <https://collectd.org/>

- Afișați ajutorul de utilizare, inclusiv versiunea programului:

`collectd -h`

- Testați fișierul de configurare și apoi ieșiți:

`collectd -t`

- Testați funcționalitatea de colectare a datelor plugin-ului și apoi ieșiți:

`collectd -T`

- Începe colecția:

`collectd`

- Specificați o locație de fișier de configurare particularizată:

`collectd -C {{path/to/file}}`

- Specificați o locație de fișier PID particularizată:

`collectd -P {{path/to/file}}`

- Nu te băga în fundal:

`collectd -f`
