# spa-acp-tool

> Debug ALSA card profile probing without running PipeWire.
> More information: <https://docs.pipewire.org/page_man_spa-acp-tool_1.html>.

- List all ALSA objects:

`spa-acp-tool {{[l|list]}}`

- Probe a specific ALSA card by ID:

`spa-acp-tool {{[c|card]}} {{card_id}}`

- List available ALSA profiles for a card:

`spa-acp-tool {{[lpr|list-profiles]}} {{card_id}}`

- Set the active ALSA profile by ID:

`spa-acp-tool {{[spr|set-profile]}} {{profile_id}}`

- List available devices for a card:

`spa-acp-tool {{[ld|list-devices]}} {{card_id}}`

- Get volume from a device:

`spa-acp-tool {{[gv|get-volume]}} {{device_id}}`

- Set volume on a device:

`spa-acp-tool {{[v|set-volume]}} {{device_id}} {{volume_level}}`

- Toggle mute state on a device:

`spa-acp-tool {{[m|toggle-mute]}} {{device_id}}`
