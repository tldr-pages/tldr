# cpulimit

> Un instrument pentru accelerarea utilizării CPU a altor procese.
> Mai multe informaţii: <http://cpulimit.sourceforge.net/>

- Limita un proces existent cu PID 1234 pentru a utiliza doar 25% din CPU:

`cpulimit --pid {{1234}} --limit {{25%}}`

- Limitați un program existent după numele său executabil:

`cpulimit --exe {{program}} --limit {{25}}`

- Lansați un anumit program și limitați-l să utilizeze doar 50% din CPU:

`cpulimit --limit {{50}} -- {{program arg1 arg2 ...}}`

- Lansați un program, limitați utilizarea procesorului la 50% și executați cpulimit în fundal:

`cpulimit --limit {{50}} --background -- {{program}}`

- Omoară procesul în cazul în care utilizarea CPU programului trece peste 50%:

`cpulimit --limit 50 --kill -- {{program}}`

- Accelerație atât ea și procesele sale copil, astfel încât nici unul merge aproximativ 25% CPU:

`cpulimit --limit {{25}} --monitor-forks -- {{program}}`
