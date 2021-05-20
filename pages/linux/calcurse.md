# calcurse

> A text-based calendar and scheduling application for the command-line.
> More information: <https://calcurse.org>.

- Start calcurse on interactive mode:

`calcurse`

- Print the appointments and events for the current day and exit:

`calcurse --appointment`

- Remove all local calcurse items and import remote objects:

`calcurse-caldav --init=keep-remote`

- Remove all remote objects and push local calcurse items:

`calcurse-caldav --init=keep-local`

- Copy local objects to the CalDAV server and vice versa:

`calcurse-caldav --init=two-way`
