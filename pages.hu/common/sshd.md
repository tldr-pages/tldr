# sshd

> Secure Shell Daemon - lehetővé teszi a távoli gépek számára, hogy biztonságosan bejelentkezzenek az aktuális gépre. A távoli gépek parancsokat hajthatnak végre, ahogyan azt az adott gépen is végrehajtják. További információ: <https://man.openbsd.org/sshd>.

- A démon elindítása a háttérben:

`sshd`

- Az sshd futtatása az előtérben:

`sshd -D`

- Futtatás verbose kimenettel (hibakereséshez):

`sshd -D -d`

- Futtatás egy adott porton:

`sshd -p {{port}}`
