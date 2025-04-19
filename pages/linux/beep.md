# beep

> A utility to beep the PC speaker.
> More information: <https://github.com/spkr-beep/beep>.

- Play a beep:

`beep`

- Play a beep that repeats:

`beep -r {{repetitions}}`

- Play a beep at a specified frequency (Hz) and duration (milliseconds):

`beep -f {{frequency}} -l {{duration}}`

- Play each new frequency and duration as a distinct beep:

`beep -f {{frequency}} -l {{duration}} {{[-n|--new]}} -f {{frequency}} -l {{duration}}`

- Play the C major scale:

`beep -f {{262}} {{[-n|--new]}} -f {{294}} {{[-n|--new]}} -f {{330}} {{[-n|--new]}} -f {{349}} {{[-n|--new]}} -f {{392}} {{[-n|--new]}} -f {{440}} {{[-n|--new]}} -f {{494}} {{[-n|--new]}} -f {{523}}`
