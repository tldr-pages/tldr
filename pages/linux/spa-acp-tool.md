# spa-acp-tool

> Debug ALSA card profile probing without running PipeWire.
> More information: <https://docs.pipewire.org/page_man_spa-acp-tool_1.html>.

- List all ALSA objects:

`undefined{{[l|list]}}`

- Probe a specific ALSA card by ID:

`undefined{{c|card}} {{card_id}}`

- List available ALSA profiles for a card:

`undefined{{[lpr|list-profiles]}} {{card_id}}`

- Set the active ALSA profile by ID:

`undefined{{[spr|set-profile]}} {{profile_id}}`

- List available devices for a card:

`undefined{{[ld|list-devices]}} {{card_id}}`

- Get volume from a device:

`undefined{{[gv|get-volume]}} {{device_id}}`

- Set volume on a device:

`undefined{{[v|set-volume]}} {{device_id}} {{volume_level}}`

- Toggle mute state on a device:

`undefined{{[m|toggle-mute]}} {{device_id}}`
