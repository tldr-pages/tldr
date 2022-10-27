# wondershaper

> Allows the user to limit the bandwidth of one or more network adapters.
> More information: <https://github.com/magnific0/wondershaper#usage>.

- Display [h]elp:

`wondershaper -h`

- Show the current [s]tatus of a specific [a]dapter:

`wondershaper -s -a {{adapter_name}}`

- Clear limits from a specific [a]dapter:

`wondershaper -c -a {{adapter_name}}`

- Set a specific maximum [d]ownload rate (in Kbps):

`wondershaper -a {{adapter_name}} -d {{1024}}`

- Set a specific maximum [u]pload rate (in Kbps):

`wondershaper -a {{adapter_name}} -u {{512}}`

- Set a specific maximum [d]ownload rate and [u]pload rate (in Kpbs):

`wondershaper -a {{adapter_name}} -d {{1024}} -u {{512}}`
