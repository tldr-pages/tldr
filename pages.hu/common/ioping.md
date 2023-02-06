# ioping

> Az I/O késleltetés valós idejű figyelése. További információ: <https://github.com/koct9i/ioping>.

- A lemezek I/O késleltetésének megjelenítése az alapértelmezett értékek és az aktuális könyvtár használatával:

`ioping .`

- A /tmp lemezen 10 darab, egyenként 1 megabájtos kérés felhasználásával mérje a késleltetést:

`ioping -c 10 -s 1M /tmp`

- Lemezkeresési sebesség mérése a `/dev/sdX` oldalon:

`ioping -R {{/dev/sdX}}`

- A lemez szekvenciális sebességének mérése a `/dev/sdX` oldalon:

`ioping -RL {{/dev/sdX}}`
