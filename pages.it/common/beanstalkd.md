# beanstalkd

> Un semplice e generico gestore di code di lavoro.
> Maggiori informazioni: <https://beanstalkd.github.io/>.

- Avvia beanstalkd, ascoltando sulla porta 11300:

`beanstalkd`

- Avvia beanstalkd ascoltando su porta ed un indirizzo dati:

`beanstalkd -l {{indirizzo_ip}} -p {{numero_porta}}`

- Rendi le code di lavoro persistenti salvandole su disco:

`beanstalkd -b {{percorso/a/directory_persistente}}`

- Sincronizza con una cartella persistente ogni 500 millisecondi:

`beanstalkd -b {{percorso/a/directory_persistente}} -f {{500}}`
