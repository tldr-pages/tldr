# exec

> Voer een commando uit zonder een child-proces te creëren.
> Meer informatie: <https://www.gnu.org/software/bash/manual/bash.html#index-exec>.

- Voer een specifiek commando uit:

`exec {{commando -with -flags}}`

- Voer een commando uit met een (grotendeels) lege omgeving:

`exec -c {{commando -with -flags}}`

- Voer een commando uit als een login-shell:

`exec -l {{commando -with -flags}}`

- Voer een commando uit met een andere naam:

`exec -a {{naam}} {{commando -with -flags}}`
