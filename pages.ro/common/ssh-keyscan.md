# ssh-keyscan

> Obțineți tastele ssh publice ale gazdelor la distanță.

- Recuperați toate tastele ssh publice ale unei gazde la distanță:

`ssh-keyscan {{host}}`

- Recuperați toate tastele ssh publice ale unei gazde la distanță care ascultă pe un anumit port:

`ssh-keyscan -p {{port}} {{host}}`

- Recuperați anumite tipuri de chei ssh publice ale unei gazde la distanță:

`ssh-keyscan -t {{rsa,dsa,ecdsa,ed25519}} {{host}}`

- Actualizați manual fișierul ssh cunoscut_hosts cu amprenta unei gazde date:

`ssh-keyscan -H {{host}} >> ~/.ssh/known_hosts`
