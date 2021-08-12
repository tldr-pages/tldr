# redshift

> Reglați temperatura de culoare a ecranului în funcție de împrejurimi.
> Mai multe informaţii: <http://jonls.dk/redshift>

- Activați Redshift cu o temperatură de 5700K în timpul zilei și 3600K pe timp de noapte:

`redshift -t {{5700}}:{{3600}}`

- Activați Redshift cu o locație personalizată specificată manual:

`redshift -l {{latitude}}:{{longitude}}`

- Activați Redshift cu 70% luminozitate ecran în timpul zilei și 40% luminozitate pe timp de noapte:

`redshift -b {{0.7}}:{{0.4}}`

- Activați Redshift cu niveluri gamma personalizate (între 0 și 1):

`redshift -g {{red}}:{{green}}:{{blue}}`

- Activați Redshift cu o temperatură constantă de culoare neschimbată:

`redshift -O {{temperature}}`
