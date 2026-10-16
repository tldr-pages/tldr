# procstat

> Geef gedetailleerde informatie weer over processen in FreeBSD.
> Meer informatie: <https://man.freebsd.org/cgi/man.cgi?query=procstat>.

- Geef bestandsdescriptors van een specifiek proces weer:

`procstat fds {{proces_id}}`

- Toon virtuele geheugentoewijzingen van een proces:

`procstat vm {{proces_id}}`

- Geef procesargumenten weer:

`procstat arguments {{proces_id}}`

- Toon bronlimieten van een proces:

`procstat rlimit {{proces_id}}`
