# nmon

> Rendszergazda, tuner és benchmark eszköz. További információ: <https://manned.org/nmon>.

- Indítsa el az nmon-t:

`nmon`

- Rekordok mentése fájlba ("-s 300 -c 288" alapértelmezés szerint):

`nmon -f`

- Összesen 240 mérésből álló rekordok mentése fájlba, 30 másodpercet szánva az egyes mérések között:

`nmon -f -s {{30}} -c {{240}}`
