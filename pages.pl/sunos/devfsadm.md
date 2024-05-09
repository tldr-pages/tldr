# devfsadm

> Komenda administracyjna dla `/dev`. Zarządza przestrzenią nazw `/dev`.
> Więcej informacji: <https://www.unix.com/man-page/sunos/1m/devfsadm>.

- Skanuj w poszukiwaniu nowych dysków:

`devfsadm -c disk`

- Wyczyść wszystkie wiszące linki /dev i skanuj w poszukiwaniu nowego urządzenia:

`devfsadm -C -v`

- Próbne uruchomienie - wypisz to, co zostanie zmienione, ale bez wprowadzania modyfikacji:

`devfsadm -C -v -n`
