# asusctl

> Control various features of ASUS laptops on Linux. More information: <https://github.com/OpenGamingCollective/asusctl>.

- Show the current profile:

`asusctl profile get`

- List available profiles:

`asusctl profile list`

- Set the active performance profile:

`asusctl profile set performance`

- Set the keyboard LED brightness:

`asusctl leds set {{off|low|med|high}}`

- Set the battery charge limit:

`asusctl battery limit {{80}}`

- Show the current battery charge limit:

`asusctl battery info`

- Get enabled fan profiles:

`asusctl fan-curve --get-enabled`

- Show system and supported-feature information:

`asusctl info --show-supported`
