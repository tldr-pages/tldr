# speak-ng

> A multi-lingual software speech synthesizer.
> See also: `espeak-ng`, `espeak`.
> More information: <https://github.com/espeak-ng/espeak-ng/blob/master/src/speak-ng.1.ronn>.

- Speak a phrase aloud:

`speak-ng "{{text}}"`

- Speak text from `stdin`:

`echo "{{text}}" | speak-ng`

- Speak the contents of a [f]ile:

`speak-ng -f {{path/to/file}}`

- Speak using a specific [v]oice:

`speak-ng -v {{voice}} "{{text}}"`

- Speak at a specific [s]peed (default is 175) and [p]itch (default is 50):

`speak-ng -s {{speed}} -p {{pitch}} "{{text}}"`

- Output the audio to a [w]AV file instead of speaking it directly:

`speak-ng -w {{path/to/output.wav}} "{{text}}"`

- List all available voices:

`espeak-ng --voices`
