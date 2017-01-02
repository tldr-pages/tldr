# sox

> Sound eXchange: play, record and convert audio files.
> Audio formats are identified by the extension.

- Merge two audio files into one:

`sox -m {{input_audiofile1}} {{input_audiofile2}} {{output_audiofile}}`

- Trim an audio file to the specified times:

`sox {{input_audiofile}} {{output_audiofile}} trim {{start}} {{end}}`

- Normalize an audio file (adjust volume to the maximum peak level, without clipping):

`sox --norm {{input_audiofile}} {{output_audiofile}}`

- Reverse and save an audio file:

`sox {{input_audiofile}} {{output_audiofile}} reverse`

- Print statistical data of an audio file:

`sox {{input_audiofile}} -n stat`
