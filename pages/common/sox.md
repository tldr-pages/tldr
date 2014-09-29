# sox

> SoX - Sound eXchange
> Play, record and convert audio files
> Audioformats are identified by extension

- Merge two audio files into one

`sox -m {{audiofile1}} {{audiofile2}} {{output_filename}}`

- Trim an audio file to the specified times

`sox {{input_audiofile}} {{output_audiofile}} trim {{start}} {{end}}`

- Normalize an audio file (adjust volume to the maximum peak level, without clipping)

`sox --norm {{input_audiofile}} {{output_audiofile}}`

- Reverse and save an audio file

`sox {{input_audiofile}} {{output_audiofile}} reverse`

- Print statistical data of an audio file

`sox {{audiofile}} -n stat`
