# pprof

> Parancssori eszköz a profiladatok vizualizálására és elemzésére. További információ: <https://github.com/google/pprof>.

- Szöveges jelentés készítése egy adott profilkészítő fájlból, fibbo binárison:

`pprof -top {{./fibbo}} {{./fibbo-profile.pb.gz}}`

- Grafikon generálása és megnyitása webböngészőben:

`pprof -svg {{./fibbo}} {{./fibbo-profile.pb.gz}}`

- Futtassa a pprof-ot interaktív módban, hogy manuálisan elindíthassa a `pprof` címet egy fájlon:

`pprof {{./fibbo}} {{./fibbo-profile.pb.gz}}`

- Webszerver futtatása, amely webes felületet szolgál ki a `pprof` felületen:

`pprof -http={{localhost:8080}} {{./fibbo}} {{./fibbo-profile.pb.gz}}`

- Egy profil lekérése egy HTTP-kiszolgálóról és egy jelentés létrehozása:

`pprof {{http://localhost:8080/debug/pprof}}`
