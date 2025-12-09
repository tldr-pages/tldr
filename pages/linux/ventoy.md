# ventoy

> A tool to create bootable USB drives using ISO files.
> More information: <https://www.ventoy.net/en/doc_start.html#doc_linux_cli>.

- Install Ventoy to a specific drive with the defaults:

`sudo ventoy -i {{/dev/sdX}}`

- Install Ventoy with GPT partition style instead of MBR:

`sudo ventoy -i -g {{/dev/sdX}}`

- Install Ventoy with GPT partition style and a custom partition label and secure boot disabled:

`sudo ventoy -i -g -S -L {{LABEL_NAME}} {{/dev/sdX}}`

- Install Ventoy and reserve space at the end of the disk:

`sudo ventoy -i -r {{SIZE_MB}} {{/dev/sdX}}`

- Force install Ventoy (overwrites existing installation):

`sudo ventoy -I {{/dev/sdX}}`

- Update Ventoy on a drive:

`sudo ventoy -u {{/dev/sdX}}`

- Display Ventoy information for a drive:

`sudo ventoy -l {{/dev/sdX}}`

- Try non-destructive installation if possible (Ventoy will not reformat the disk):

`sudo ventoy -i -n {{/dev/sdX}}`
