# flock

> Beheer sloten van shell scripts.
> Het kan worden gebruikt om ervoor te zorgen dat slechts één proces van een commando wordt uitgevoerd.
> Meer informatie: <https://manned.org/flock>.

- Voer een commando uit met een bestandslot zodra het slot niet vereist is door anderen:

`flock {{pad/naar/lock.lock}} --command "{{commando}}"`

- Voer een commando uit met een bestandslot en stop als het slot niet bestaat:

`flock {{pad/naar/lock.lock}} --nonblock --command "{{commando}}"`

- Voer een commando uit met een bestandslot en stop met een specifieke error code als het slot niet bestaat:

`flock {{pad/naar/lock.lock}} --nonblock --conflict-exit-code {{error_code}} -c "{{commando}}"`
