# iotop

> Afișați un tabel de utilizare I/O curentă prin procese sau fire.
> Mai multe informaţii: <https://manned.org/iotop>

- Porniți top-ca I/O monitor:

`sudo iotop`

- Arată numai procese sau fire de fapt face I/O:

`sudo iotop --only`

- Afișează utilizarea I/O în modul non-interactiv:

`sudo iotop --batch`

- Arată numai I/O utilizarea proceselor (implicit este de a afișa toate firele):

`sudo iotop --processes`

- Afișează utilizarea I/O a PID (e) dat (e):

`sudo iotop --pid={{PID}}`

- Arată I/O de utilizare a unui anumit utilizator:

`sudo iotop --user={{user}}`

- Afișează acumulat I/O în loc de lățime de bandă:

`sudo iotop --accumulated`
