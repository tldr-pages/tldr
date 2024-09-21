# renice

> Verander de scheduleringsprioriteit/niceness van lopende processen.
> Niceness waarden variëren van -20 (meest gunstig voor het proces) tot 19 (minst gunstig voor het proces).
> Zie ook: `nice`.
> Meer informatie: <https://manned.org/renice>.

- Stel de absolute prioriteit van een lopend [p]roces in:

`renice {{+3}} -p {{pid}}`

- Verhoog/verlaag de prioriteit van alle processen die eigendom zijn van een [g]ebruiker:

`renice --relative {{-4}} -u {{uid|user}}`

- Stel de prioriteit in van alle processen die behoren tot een proces[g]roep:

`renice --absolute {{5}} -g {{proces_groep}}`
