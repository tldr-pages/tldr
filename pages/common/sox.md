# sox

> Sound eXchange: play, record and convert audio files.
> Audio formats are identified by the extension.

- Merge two audio files into one:

`sox -m {{input_audiofile1}} {{input_audiofile2}} {{output_audiofile}}`

- Trim an audio file, providing the start point and the length of the new clip:

`sox {{input_audiofile}} {{output_audiofile}} trim {{start}} {{length}}`

- Normalize an audio file (adjust volume to the maximum peak level, without clipping):

`sox --norm {{input_audiofile}} {{output_audiofile}}`

- Reverse and save an audio file:

`sox {{input_audiofile}} {{output_audiofile}} reverse`

- Print statistical data of an audio file:

`sox {{input_audiofile}} -n stat`

- Increase the volume of an audio file by 2x

`sox -v 2.0 {{input_audiofile}} {{output_audiofile}}`
