# flock

> Beheer locks van shell scripts.
> Het kan gebruikt worden om ervoor te zorgen dat slechts één proces van een commando draait.
> Meer informatie: <https://manned.org/flock>.

- Voer een commando met een bestandslock uit zodra de lock niet meer nodig is voor anderen:

`flock {{pad/naar/lock.lock}} {{[-c|--command]}} "{{commando}}"`

- Voer een opdracht uit met een bestandslock en sluit af als de lock niet bestaat:

`flock {{pad/naar/lock.lock}} {{[-n|--nonblock]}} {{[-c|--command]}} "{{commando}}"`

- Voer een opdracht uit met een bestandslock en sluit af met een specifieke foutcode als de lock niet bestaat:

`flock {{pad/naar/lock.lock}} {{[-n|--nonblock]}} {{[-E|--conflict-exit-code]}} {{error_code}} {{[-c|--command]}} "{{commando}}"`
