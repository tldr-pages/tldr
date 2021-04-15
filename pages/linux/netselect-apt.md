# netselect-apt

> Create a `sources.list` file for a Debian mirror with the lowest latency.
> More information: <https://manpages.debian.org/buster/netselect-apt/netselect-apt.1.html>.

- Create `sources.list` using the lowest latency server:

`sudo netselect-apt`

- Specify Debian branch, stable is used by default:

`sudo netselect-apt {{testing}}`

- Include non-free section:

`sudo netselect-apt --non-free`

- Specify a country for the mirror list lookup:

`sudo netselect-apt -c {{India}}`
