# redshift

> Adjust the color temperature of your screen according to your surroundings.
> More information: <http://jonls.dk/redshift>.

- Turn on Redshift with a specific [t]emperature during day (e.g., 5700K) and at night (e.g., 3600K):

`redshift -t {{5700}}:{{3600}}`

- Turn on Redshift with a manually specified custom [l]ocation:

`redshift -l {{latitude}}:{{longitude}}`

- Turn on Redshift with a specific screen [b]rightness during the day (e.g, 70%) and at night (e.g., 40%):

`redshift -b {{0.7}}:{{0.4}}`

- Turn on Redshift with custom [g]amma levels (between 0 and 1):

`redshift -g {{red}}:{{green}}:{{blue}}`

- Turn on Redshift with a constant unchanging color temperature:

`redshift -O {{temperature}}`
