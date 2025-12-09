# lvrename

> Rename a logical volume.
> More information: <https://manned.org/lvrename>.

- Rename an LV using full paths:

`sudo lvrename {{/dev/vg_name/old_lv}} {{/dev/vg_name/new_lv}}`

- Rename an LV using the volume group and names:

`sudo lvrename {{vg_name}} {{old_lv}} {{new_lv}}`

- Answer "yes" to any prompts:

`sudo lvrename {{[-y|--yes]}} {{/dev/vg_name/old_lv}} {{/dev/vg_name/new_lv}}`
