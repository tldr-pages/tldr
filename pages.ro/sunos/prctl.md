# prctl

> Obține sau setează controalele de resurse ale proceselor, sarcinilor și proiectelor care rulează.
> Mai multe informații: <https://www.unix.com/man-page/sunos/1/prctl>.

- Examinează limitele și permisiunile procesului:

`prctl {{pid}}`

- Examinează limitele și permisiunile procesului într-un format prelucrabil automat:

`prctl -P {{pid}}`

- Obține o limită specifică pentru un proces care rulează:

`prctl -n process.max-file-descriptor {{pid}}`