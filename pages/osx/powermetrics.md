# powermetrics

> Gather power-related CPU, GPU, battery, disk, and network measurements.
> More information: <https://keith.github.io/xcode-man-pages/powermetrics.1.html>.

- Take one sample using the default sample interval:

`sudo powermetrics {{[-n|--sample-count]}} 1`

- Take 10 samples, one second apart:

`sudo powermetrics {{[-n|--sample-count]}} 10 {{[-i|--sample-rate]}} 1000`

- Take one sample using specific samplers:

`sudo powermetrics {{[-s|--samplers]}} {{tasks,battery}} {{[-n|--sample-count]}} 1`

- Show per-process energy measurements:

`sudo powermetrics {{[-s|--samplers]}} tasks --show-process-energy {{[-n|--sample-count]}} 1`

- Write one machine-readable property list sample to a file:

`sudo powermetrics {{[-f|--format]}} plist {{[-o|--output-file]}} {{path/to/file.plist}} {{[-n|--sample-count]}} 1`
