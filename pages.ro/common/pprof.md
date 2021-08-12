# pprof

> Instrument linie de comandă pentru vizualizarea și analiza datelor de profil.
> Mai multe informaţii: <https://github.com/google/pprof>

- Generarea unui raport text dintr-un anumit fișier de profilare, pe fibbo binar:

`pprof -top {{./fibbo}} {{./fibbo-profile.pb.gz}}`

- Generați un grafic și deschideți-l pe un browser web:

`pprof -svg {{./fibbo}} {{./fibbo-profile.pb.gz}}`

- Rulați pprof în modul interactiv pentru a putea lansa manual `pprof` pe un fișier:

`pprof {{./fibbo}} {{./fibbo-profile.pb.gz}}`

- Rulați un server web care servește o interfață web pe partea de sus a `pprof`:

`pprof -http={{localhost:8080}} {{./fibbo}} {{./fibbo-profile.pb.gz}}`

- Preluați un profil de pe un server HTTP și generați un raport:

`pprof {{http://localhost:8080/debug/pprof}}`
