# lame

> Encode WAV to MP3 files.
> More information: <https://svn.code.sf.net/p/lame/svn/trunk/lame/USAGE>.

- Encode an audio file to MP3 using CBR 320 kbit/second:

`lame -b 320 {{path/to/file}}.wav {{path/to/output}}.mp3`

- Encode an audio file to MP3 using the V0 preset:

`lame -V 0 {{path/to/file}}.wav {{path/to/output}}.mp3`

- Encode an audio file to AAC:

`lame {{path/to/file}}.wav {{path/to/output}}.aac`
