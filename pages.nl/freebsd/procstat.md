# procstat

> Geef gedetailleerde informatie weer over processen in FreeBSD.
> Meer informatie: <https://man.freebsd.org/cgi/man.cgi?query=procstat>.

- Geef bestandsdescriptors van een specifiek proces weer:

`procstat fds {{pid}}`

- Toon virtuele geheugentoewijzingen van een proces:

`procstat vm {{pid}}`

- Geef procesargumenten weer:

`procstat arguments {{pid}}`

- Toon bron limieten van een proces:

`procstat rlimit {{pid}}`
