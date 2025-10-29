# redshift

> Adjust the color temperature of a screen according to its surroundings.
> More information: <https://manned.org/redshift>.

- Turn on Redshift with a specific [t]emperature during day (e.g., 5700K) and at night (e.g., 3600K):

`redshift -t 5700:3600`

- Turn on Redshift with a manually specified custom [l]ocation:

`redshift -l {{latitude}}:{{longitude}}`

- Turn on Redshift with a specific screen [b]rightness during the day (e.g, 70%) and at night (e.g., 40%):

`redshift -b 0.7:0.4`

- Turn on Redshift with custom [g]amma levels (between 0 and 1):

`redshift -g {{red}}:{{green}}:{{blue}}`

- [P]urge existing temperature changes and set a constant unchanging color temperature in [O]ne-shot mode:

`redshift -PO {{temperature}}`
