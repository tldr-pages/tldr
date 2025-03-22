# reflector

> Arch script to fetch and sort mirrorlists.
> More information: <https://manned.org/reflector>.

- Get all mirrors, sort for download speed and save them:

`sudo reflector --sort {{rate}} --save {{/etc/pacman.d/mirrorlist}}`

- Only get German HTTPS mirrors:

`reflector --country {{Germany}} --protocol {{https}}`

- Only get the 10 recently sync'd mirrors:

`reflector --latest {{10}}`

- Use a configuration file to fetch mirrors:

`sudo reflector @{{/etc/xdg/reflector/reflector.conf}}`

- Display help:

`reflector {{[-h|--help]}}`
