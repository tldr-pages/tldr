# wondershaper

> Wonder Shaper is a script that allows the user to limit the bandwidth of one or more network adapters.
> More information: <https://github.com/magnific0/wondershaper#usage>.

- Print the [h]elp:

`wondershaper -h`

- Show the current [s]tatus of [a]dapter:

`wondershaper -s -a {{adapter_name}}`

- Clear the limits from [a]dapter:

`wondershaper -c -a {{adapter_name}}`

- Set maximum [d]ownload rate (in Kbps):

`wondershaper -a {{adapter_name}} -d 1024`

- Set maximum [u]pload rate (in Kbps):

`wondershaper -a {{adapter_name}} -u 512`

- Set both maximum [d]ownload rate and [u]pload rate (in Kpbs):

`wondershaper -a {{adapter_name}} -d 1024 -u 512`
