# betterlockscreen

> Simple, minimal lock screen.
> More information: <https://github.com/betterlockscreen/betterlockscreen>.

- Lock the screen:

`betterlockscreen {{[-l|--lock]}}`

- Change the lock screen background:

`betterlockscreen {{[-u|--update]}} {{path/to/image.png}}`

- Lock the screen, showing some custom text:

`betterlockscreen {{[-l|--lock]}} pixel --text "{{custom lock screen text}}"`

- Lock the screen, with a custom monitor off timeout in seconds:

`betterlockscreen --off {{5}} {{[-l|--lock]}}`
