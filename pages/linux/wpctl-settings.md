# wpctl settings

> Manage WirePlumber runtime settings.
> More information: <https://pipewire.pages.freedesktop.org/wireplumber/daemon/configuration/configuration_option_types.html>.

- List all settings:

`wpctl settings`

- View the value of a specific setting:

`wpctl settings {{setting_id}}`

- Set the whole system to have mono audio:

`wpctl settings node.features.audio.mono true`

- Set if disconnecting speakers will pause playback:

`wpctl settings linking.pause-playback {{true|false}}`
