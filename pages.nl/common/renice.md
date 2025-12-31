# renice

> Verander de scheduleringsprioriteit/niceness van lopende processen.
> Niceness waarden variëren van -20 (meest gunstig voor het proces) tot 19 (minst gunstig voor het proces).
> Zie ook: `nice`.
> Meer informatie: <https://manned.org/renice.1p>.

- Verhoog/verlaag de prioriteit van een lopend [p]roces:

`renice -n {{3}} -p {{pid}}`

- Verhoog/verlaag de prioriteit van alle processen die eigendom zijn van een [g]ebruiker:

`renice -n {{-4}} -u {{uid|user}}`

- Verhoog/verlaag de prioriteit van alle processen die behoren tot een proces[g]roep:

`renice -n {{5}} -g {{proces_groep}}`
