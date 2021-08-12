# beanstalkd

> Un server de coadă de lucru simplu și generic.
> Mai multe informaţii: <https://beanstalkd.github.io/>

- Start vrejul de fasole, ascultarea pe portul 11300:

`beanstalkd`

- Start beanstalkd ascultare pe un port personalizat și adresa:

`beanstalkd -l {{ip_address}} -p {{port_number}}`

- Persistă cozile de lucru salvându-le pe disc:

`beanstalkd -b {{path/to/persistence_directory}}`

- Sincronizați cu directorul de persistență la fiecare 500 milisecunde:

`beanstalkd -b {{path/to/persistence_directory}} -f {{500}}`
