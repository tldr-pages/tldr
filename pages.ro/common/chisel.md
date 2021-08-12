# chisel

> Creați tuneluri TCP. Include atât client, cât și server.
> Mai multe informaţii: <https://github.com/jpillora/chisel>

- Rulează un server de daltă:

`chisel server`

- Rulați un server Chisel ascultând un anumit port:

`chisel server -p {{server_port}}`

- Rulați un server daltă care acceptă conexiuni autentificate utilizând numele de utilizator și parola:

`chisel server --auth {{username}}:{{password}}`

- Conectați-vă la un server de daltă și tunel un anumit port la un server de la distanță și port:

`chisel client {{server_ip}}:{{server_port}} {{local_port}}:{{remote_server}}:{{remote_port}}`

- Conectați-vă la un server de daltă și tunel o gazdă specifică și port la un server de la distanță și port:

`chisel client {{server_ip}}:{{server_port}} {{local_host}}:{{local_port}}:{{remote_server}}:{{remote_port}}`

- Conectați-vă la un server Chisel utilizând autentificarea numelui de utilizator și a parolei:

`chisel client --auth {{username}}:{{password}} {{server_ip}}:{{server_port}} {{local_port}}:{{remote_server}}:{{remote_port}}`
