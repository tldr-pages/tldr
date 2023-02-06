# beanstalkd

> Egy egyszerű és általános work-queue szerver. További információ: <https://beanstalkd.github.io/>.

- Indítsuk el a beanstalkd-ot, amely a 11300-as porton figyel:

`beanstalkd`

- A beanstalkd elindítása egy egyéni porton és címen történő figyeléssel:

`beanstalkd -l {{ip_address}} -p {{port_number}}`

- A munkaköri várólisták megőrzése a lemezre mentéssel:

`beanstalkd -b {{path/to/persistence_directory}}`

- Szinkronizálás a perzisztencia könyvtárba 500 milliszekundumonként:

`beanstalkd -b {{path/to/persistence_directory}} -f {{500}}`
