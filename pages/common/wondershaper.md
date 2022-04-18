# wondershaper

> Wonder Shaper is a script that allows the user to limit the bandwidth of one or more network adapters.
> More information: <https://github.com/magnific0/wondershaper#usage>.

- Display help:

`wondershaper -h`

- Show the current status of adapter:

`wondershaper -s -a {{adapter_name}}`

- Clear the limits from adapter:

`wondershaper -c -a {{adapter_name}}`

- Set maximum download rate (in Kbps):

`wondershaper -a {{adapter_name}} -d 1024`

- Set maximum upload rate (in Kbps):

`wondershaper -a {{adapter_name}} -u 512`

- Set both maximum download rate and upload rate (in Kpbs):

`wondershaper -a {{adapter_name}} -d 1024 -u 512`