# Gammastep

> Adjust the screen's color temperature according to the time of day.
> More information: <https://gitlab.com/chinstrap/gammastep>.

- Turn on Gammastep with a specific [t]emperature during the day (e.g. 5700k) and at night (e.g. 3600k):

`gammastep -t {{5700}}:{{3600}}`

- Turn on Gammastep with a manually specified custom [l]ocation:

`gammastep -l {{latitude}}:{{longitude}}`

- Turn on Gammastep with a specific screen [b]rightness during the day (e.g. 70%) and at night (e.g. 40%), with minimum brightness 10% and maximum brightness 100%:

`gammastep -b {{0.7}}:{{0.4}}`

- Turn on Gammastep with custom [g]amma levels (between 0 and 1):

`gammastep -g {{red}}:{{green}}:{{blue}}`

- Turn on Gammastep with a c[O]nstant unchanging color temperature:

`gammastep -O {{temperature}}`

- Reset temperature adjustments applied by Gammastep:

`gammastep -x`
