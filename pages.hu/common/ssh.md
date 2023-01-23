# ssh

> A Secure Shell egy olyan protokoll, amelyet távoli rendszerekbe való biztonságos bejelentkezésre használnak. Naplózásra vagy parancsok végrehajtására használható egy távoli szerveren. További információ: <https://man.openbsd.org/ssh>.

- Csatlakozás egy távoli kiszolgálóhoz:

`ssh {{username}}@{{remote_host}}`

- Csatlakozás egy távoli kiszolgálóhoz egy adott azonosítóval (privát kulcs):

`ssh -i {{path/to/key_file}} {{username}}@{{remote_host}}`

- Csatlakozás egy távoli kiszolgálóhoz egy adott porton keresztül:

`ssh {{username}}@{{remote_host}} -p {{2222}}`

- Egy parancs futtatása egy távoli kiszolgálón egy \[t\]ty kiosztással, amely lehetővé teszi a távoli paranccsal való interakciót:

`ssh {{username}}@{{remote_host}} -t {{command}} {{command_arguments}}`

- SSH alagútépítés: Dinamikus porttovábbítás (SOCKS proxy a `localhost:1080` oldalon):

`ssh -D {{1080}} {{username}}@{{remote_host}}`

- Egy adott port továbbítása (`localhost:9999` a `example.org:80`-ra ) a távoli parancsok ál-\[T\]ty kiosztásának és futtatásának letiltásával együtt:

`ssh -L {{9999}}:{{example.org}}:{{80}} -N -T {{username}}@{{remote_host}}`

- SSH ugrás: Csatlakozás egy ugróállomáson keresztül egy távoli kiszolgálóhoz (több ugróugrást lehet megadni vesszővel elválasztva):

`ssh -J {{username}}@{{jump_host}} {{username}}@{{remote_host}}`

- Ügynökök továbbítása: A hitelesítési információk továbbítása a távoli géphez (a rendelkezésre álló opciókat lásd a `man ssh_config` oldalon):

`ssh -A {{username}}@{{remote_host}}`
