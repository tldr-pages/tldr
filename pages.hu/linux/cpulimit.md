# cpulimit

> Eszköz más folyamatok CPU-használatának korlátozására. További információ: <http://cpulimit.sourceforge.net/>.

- Korlátozza a PID 1234 azonosítóval rendelkező meglévő folyamatot, hogy csak a CPU 25%-át használja:

`cpulimit --pid {{1234}} --limit {{25%}}`

- Egy meglévő program korlátozása a futtatható neve alapján:

`cpulimit --exe {{program}} --limit {{25}}`

- Egy adott program elindítása és korlátozza, hogy csak a CPU 50%-át használja:

`cpulimit --limit {{50}} -- {{program arg1 arg2 ...}}`

- Indítson el egy programot, korlátozza a CPU-használatát 50%-ra, és futtassa a cpulimit-et a háttérben:

`cpulimit --limit {{50}} --background -- {{program}}`

- A program folyamatának leállítása, ha a program CPU-használata 50% fölé emelkedik:

`cpulimit --limit 50 --kill -- {{program}}`

- A program és a gyermekfolyamatai között is korlátozza, hogy egyik sem haladja meg a 25%-os CPU-értéket:

`cpulimit --limit {{25}} --monitor-forks -- {{program}}`
