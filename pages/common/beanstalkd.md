# beanstalkd

> A simple and generic work-queue server.
> More information: <https://beanstalkd.github.io/>.

- Start beanstalkd, listening on port 11300:

`beanstalkd`

- Start beanstalkd listening on a custom port and address:

`beanstalkd -l {{ip_address}} -p {{port_number}}`

- Persist work queues by saving them to disk:

`beanstalkd -b {{path/to/persistence_directory}}`

- Sync to the persistence directory every 500 milliseconds:

`beanstalkd -b {{path/to/persistence_directory}} -f {{500}}`
