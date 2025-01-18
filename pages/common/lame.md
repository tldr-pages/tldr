# lame

> LAME is a high quality MPEG Audio Layer III (MP3) encoder licensed under the LGPL.
> Documentation: <https://svn.code.sf.net/p/lame/svn/trunk/lame/USAGE>.
> More information: <https://lame.sourceforge.io/index.php>.

- Encode an audio file to MP3 using CBR 320 kbit/second:

`lame -b 320 {{path/to/file}}.wav {{path/to/output}}.mp3`

- Encode an audio file to MP3 using the V0 preset:

`lame -V 0 {{path/to/file}}.wav {{path/to/output}}.mp3`

- Encode an audio file to AAC:

`lame {{path/to/file}}.wav {{path/to/output}}.aac`
