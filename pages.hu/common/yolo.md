# yolo

> A YOLO parancssori felület segítségével egyszerűen képezhet, validálhat vagy következtethet modelleket különböző feladatokra és verziókra. További információ: <https://docs.ultralytics.com/cli/>.

- Hozzon létre egy másolatot az alapértelmezett konfigurációról az aktuális munkakönyvtárában:

`yolo task=init`

- Képezze az objektumfelismerő, példányszegmentáló vagy osztályozó modellt a megadott konfigurációs fájllal:

`yolo task={{detect|segment|classify}} mode=train cfg={{path/to/config.yaml}}`
