# spa-resample

> Resample an audio file using the PipeWire resampler.
> Note: This utility is primarily intended for testing and debugging the resampler.
> More information: <https://docs.pipewire.org/page_man_spa-resample_1.html>.

- Resample an audio file:

`spa-resample {{path/to/input.wav}} {{path/to/output.wav}}`

- Resample an audio file to a specific sample rate:

`spa-resample {{[-r|--rate]}} {{48000}} {{path/to/input.wav}} {{path/to/output.wav}}`

- Resample an audio file to a specific format:

`spa-resample {{[-f|--format]}} {{s8|s16|s32|f32|f64}} {{path/to/input.wav}} {{path/to/output.wav}}`

- Resample an audio file with a specific quality (0 is lowest, 14 is highest):

`spa-resample {{[-q|--quality]}} {{0..14}} {{path/to/input.wav}} {{path/to/output.wav}}`
