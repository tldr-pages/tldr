# speaker-test

> Speaker test tone generator for ALSA.
> See also: `aplay`, `arecord`, `amixer`.
> More information: <https://manned.org/speaker-test>.

- Test the default speakers with pink noise:

`speaker-test`

- Test the default speakers with a sine wave:

`speaker-test {{[-t|--test]}} sine {{[-f|--frequency]}} {{frequency}}`

- Test the default speakers with a predefined WAV file:

`speaker-test {{[-t|--test]}} wav`

- Test the default speakers with a WAV file:

`speaker-test {{[-t|--test]}} wav {{[-w|--wavfile]}} {{path/to/file}}`
