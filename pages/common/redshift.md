# redshift

> Adjust the color temperature of a screen according to its surroundings.
> Note: Redshift does not support Wayland.
> See also: `gammastep`.
> More information: <https://manned.org/redshift>.

- Turn on Redshift with [t]emperature set to 5700k during the day and 3600k at night:

`redshift -t 5700:3600`

- Turn on Redshift with a manually specified custom [l]ocation:

`redshift -l {{latitude}}:{{longitude}}`

- Turn on Redshift with screen [b]rightness set to 70% during the day and 40% at night:

`redshift -b 0.7:0.4`

- Turn on Redshift with custom [g]amma levels (between 0 and 1):

`redshift -g {{red}}:{{green}}:{{blue}}`

- [P]urge existing temperature changes and set a constant unchanging color temperature in [O]ne-shot mode:

`redshift -PO {{temperature}}`
