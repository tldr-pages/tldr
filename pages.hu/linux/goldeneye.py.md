# goldeneye.py

> Egy HTTP DoS teszteszköz. További információ: <https://github.com/jseidl/GoldenEye>.

- Egy adott weboldal tesztelése:

`./goldeneye.py {{url}}`

- Egy adott weboldal tesztelése 100 felhasználói ügynökkel és 200 egyidejű socket-tel:

`./goldeneye.py {{url}} --useragents 100 --sockets 200`

- Egy adott weboldal tesztelése az SSL-tanúsítvány ellenőrzése nélkül:

`./goldeneye.py {{url}} --nosslcheck`

- Egy adott weboldal tesztelése hibakeresési módban:

`./goldeneye.py {{url}} --debug`

- Súgó megjelenítése:

`./goldeneye.py --help`
