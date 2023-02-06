# killall

> A folyamat minden példányának küld kill jelet a név alapján (a pontos névnek kell lennie). A SIGKILL és SIGSTOP jelek kivételével minden jelet elfoghat a folyamat, lehetővé téve a tiszta kilépést. További információ: <https://manned.org/killall>.

- Egy folyamat befejezése az alapértelmezett SIGTERM (terminate) jel használatával:

`killall {{process_name}}`

- A rendelkezésre álló jelnevek listája (a 'SIG' előtag nélkül használandó):

`killall --list`

- Interaktívan kérjen megerősítést a befejezés előtt:

`killall -i {{process_name}}`

- Egy folyamat befejezése a SIGINT (megszakítás) jel használatával, amely ugyanaz a jel, amelyet a `Ctrl + C` megnyomásával küldünk:

`killall -INT {{process_name}}`

- Egy folyamat kényszerített leállítása:

`killall -KILL {{process_name}}`
