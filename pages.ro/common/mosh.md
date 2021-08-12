# mosh

> Mobile Shell (`mosh`) este un înlocuitor robust și receptiv pentru SSH.
> `mosh` persistă conexiuni la servere la distanță în roaming între rețele.
> Mai multe informaţii: <https://mosh.org>

- Conectează-te la un server de la distanță:

`mosh {{username}}@{{remote_host}}`

- Conectați-vă la un server de la distanță cu o anumită identitate (cheie privată):

`mosh --ssh="ssh -i {{path/to/key_file}}" {{username}}@{{remote_host}}`

- Conectați-vă la un server de la distanță utilizând un anumit port:

`mosh --ssh="ssh -p {{2222}}" {{username}}@{{remote_host}}`

- Rulați o comandă pe un server la distanță:

`mosh {{remote_host}} -- {{command -with -flags}}`

- Selectați portul Mosh UDP (util atunci când `{{remote_host}}` este în spatele unui NAT):

`mosh -p {{124}} {{username}}@{{remote_host}}`

- Utilizare atunci când `mosh-server` binar este în afara calea standard:

`mosh --server={{path/to/bin/}}mosh-server {{remote_host}}`
