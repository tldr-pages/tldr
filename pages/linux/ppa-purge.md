# ppa-purge

> Disable a PPA and revert its packages to the official versions.
> More information: <https://manned.org/ppa-purge>.

- Disable a PPA and downgrade its packages to the official versions:

`sudo ppa-purge ppa:{{owner}}/{{ppa_name}}`

- Disable a PPA given only its [o]wner (the PPA name defaults to `ppa`):

`sudo ppa-purge -o {{owner}}`

- Disable a PPA given its [o]wner and [p]PA name:

`sudo ppa-purge -o {{owner}} -p {{ppa_name}}`

- Answer [y]es to all package manager prompts:

`sudo ppa-purge -y ppa:{{owner}}/{{ppa_name}}`

- Use a specific [d]istribution instead of the detected one:

`sudo ppa-purge -d {{distribution}} ppa:{{owner}}/{{ppa_name}}`

- Display [h]elp:

`ppa-purge -h`
