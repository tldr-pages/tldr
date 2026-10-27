# asusctl

> Control various features of ASUS laptops on Linux.
> More information: <https://github.com/OpenGamingCollective/asusctl>.

- Show the current profile:

`asusctl profile get`

- List available profiles:

`asusctl profile list`

- Switch to the next profile:

`asusctl profile next`

- Set the active performance profile:

`asusctl profile set {{balanced|performance|quiet|low-power|custom}}`

- Set the keyboard LED brightness:

`asusctl leds set {{off|low|med|high}}`

- Set the battery charge limit to a percentage between 20 and 100:

`asusctl battery limit {{20..100}}`

- Show the current battery charge limit:

`asusctl battery info`

- Show system and supported-feature information:

`asusctl info --show-supported`
