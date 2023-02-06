# stress

> Eszköz a CPU, a memória és az IO stressztesztelésére egy Linux rendszerben. További információ: <https://manned.org/stress>.

- 4 munkás létrehozása a CPU stresszteszteléséhez:

`stress -c {{4}}`

- 2 munkást indít az IO stresszteszteléséhez, és 5 másodperc után időkorlátot ad:

`stress -i {{2}} -t {{5}}`

- 2 munkás létrehozása a memória stresszteszteléséhez (minden munkás 256 MB bájtot oszt ki):

`stress -m {{2}} --vm-bytes {{256M}}`

- 2 munkás létrehozása, akik a write()/unlink() funkciót pörgetik (minden munkás 1 G bájtot ír):

`stress -d {{2}} --hdd-bytes {{1GB}}`
