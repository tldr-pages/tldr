# pm2

> Manager de proces pentru Node.js.
> Utilizat pentru gestionarea jurnalelor, monitorizarea și configurarea proceselor.
> Mai multe informaţii: <https://pm2.keymetrics.io>

- Începeți un proces cu un nume care poate fi utilizat pentru operațiuni ulterioare:

`pm2 start {{app.js}} --name {{myapp}}`

- Lista proceselor:

`pm2 list`

- Monitorizează toate procesele:

`pm2 monit`

- Opreşte un proces:

`pm2 stop {{myapp}}`

- Reporniți un proces:

`pm2 restart {{myapp}}`

- Dump toate procesele pentru învierea lor mai târziu:

`pm2 save`

- Reînvierea proceselor care fac obiectul unui dumping anterior:

`pm2 resurrect`
