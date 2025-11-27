# espeak-ng

> A multi-lingual software speech synthesizer.
> See also: `speak-ng`, `espeak`.
> More information: <https://github.com/espeak-ng/espeak-ng/blob/master/src/espeak-ng.1.ronn>.

- Speak a phrase aloud:

`espeak-ng "{{text}}"`

- Speak text from `stdin`:

`echo "{{text}}" | espeak-ng`

- Speak the contents of a [f]ile:

`espeak-ng -f {{path/to/file}}`

- Speak using a specific [v]oice:

`espeak-ng -v {{voice}} "{{text}}"`

- Speak at a specific [s]peed (default is 175) and [p]itch (default is 50):

`espeak-ng -s {{speed}} -p {{pitch}} "{{text}}"`

- Output the audio to a [w]AV file instead of speaking it directly:

`espeak-ng -w {{path/to/output.wav}} "{{text}}"`

- List all available voices:

`espeak-ng --voices`
