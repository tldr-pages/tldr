# networkQuality

> Measure the network quality by connecting to the internet.
> More information: <https://support.apple.com/HT212313>.

- Test the network quality for the default interface:

`networkQuality`

- Test the upload and download speeds sequentially instead of in parallel:

`networkQuality -s`

- Test a specified network interface:

`networkQuality -I {{en0}}`

- Test the network quality with verbose output:

`networkQuality -v`
