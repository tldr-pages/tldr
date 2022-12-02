# sox

> Sound eXchange: play, record and convert audio files.
> Audio formats are identified by the extension.
> More information: <http://sox.sourceforge.net>.

- Merge two audio files into one:

`sox -m {{path/to/file}} {{path/to/file}} {{path/to/file}}`

- Trim an audio file to the specified times:

`sox {{path/to/file}} {{path/to/file}} trim {{start}} {{end}}`

- Normalize an audio file (adjust volume to the maximum peak level, without clipping):

`sox --norm {{path/to/file}} {{path/to/file}}`

- Reverse and save an audio file:

`sox {{path/to/file}} {{path/to/file}} reverse`

- Print statistical data of an audio file:

`sox {{path/to/file}} -n stat`

- Increase the volume of an audio file by 2x:

`sox -v 2.0 {{path/to/file}} {{path/to/file}}`
