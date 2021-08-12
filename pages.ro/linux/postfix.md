# postfix

> Programul de control al agenţilor de transfer poştă electronică Postfix (MTA).
> A se vedea, de asemenea, `dovecot`, un agent de livrare a corespondenței (MDA) care se integrează cu Postfix.
> Mai multe informaţii: <http://www.postfix.org>

- Verificați configurația:

`sudo postfix check`

- Verificați starea daemonului Postfix:

`sudo postfix status`

- Start Postfix:

`sudo postfix start`

- Opriți grațios Postfix:

`sudo postfix stop`

- Spălați coada de corespondență:

`sudo postfix flush`

- Reîncarcă fișierele de configurare:

`sudo postfix reload`
