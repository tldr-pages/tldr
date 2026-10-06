# renice

> Verander de scheduleringsprioriteit/niceness van lopende processen.
> Niceness waarden variëren van -20 (meest gunstig voor het proces) tot 19 (minst gunstig voor het proces).
> Zie ook: `nice`.
> Meer informatie: <https://manned.org/renice>.

- Stel de absolute prioriteit van een lopend proces in:

`renice --priority {{3}} {{[-p|--pid]}} {{proces_id}}`

- Verhoog de prioriteit van een lopend proces:

`sudo renice --relative {{-4}} {{[-p|--pid]}} {{proces_id}}`

- Verlaag de prioriteit van alle processen die eigendom zijn van een gebruiker:

`renice --relative {{4}} {{[-u|--user]}} {{uid|gebruiker}}`

- Stel de prioriteit in van alle processen die behoren tot een procesgroep:

`sudo renice {{-5}} {{[-g|--pgrp]}} {{process_group}}`
