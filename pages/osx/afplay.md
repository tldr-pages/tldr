# afplay

> Command-line audio player.
> More information: <https://keith.github.io/xcode-man-pages/afplay.1.html>.

- Play a sound file (waits until playback ends):

`afplay {{path/to/file}}`

- Play a sound file at 2x speed (playback rate):

`afplay --rate {{2}} {{path/to/file}}`

- Play a sound file at half speed:

`afplay --rate {{0.5}} {{path/to/file}}`

- Play the first N seconds of a sound file:

`afplay --time {{seconds}} {{path/to/file}}`
