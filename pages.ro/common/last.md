# last

> Vizualizați ultimii utilizatori autentificați.

- Vizualizați ultimele autentificări, durata acestora și alte informații citite din `/var/log/wtmp`:

`last`

- Specificați cât de multe dintre ultimele autentificări pentru a afișa:

`last -n {{login_count}}`

- Imprimați data și ora completă pentru intrări și apoi afișați ultima coloană nume gazdă pentru a preveni trunchierea:

`last -F -a`

- Vizualizați toate datele de conectare de către un anumit utilizator și afișați adresa IP în loc de numele gazdei:

`last {{username}} -i`

- Vezi toate reporniri înregistrate (adică, ultimele login-uri ale pseudo utilizator „reboot”):

`last reboot`

- Vizualizați toate închiderile înregistrate (adică, ultimele autentificări ale pseudo user „shutdown”):

`last shutdown`
