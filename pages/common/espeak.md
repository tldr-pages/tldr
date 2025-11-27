# espeak

> A multi-lingual software speech synthesizer.
> Note: `espeak` is considered discontinued, as development has shifted to `espeak-ng`.
> More information: <https://manned.org/espeak>.

- Speak a phrase aloud:

`espeak "{{text}}"`

- Speak text from `stdin`:

`echo "{{text}}" | espeak`

- Speak the contents of a file:

`espeak -f {{path/to/file}}`

- Speak using a specific voice:

`espeak -v {{voice}} "{{text}}"`

- Speak at a specific speed (default is 160) and pitch (default is 50):

`espeak -s {{speed}} -p {{pitch}} "{{text}}"`

- Output the audio to a WAV file instead of speaking it directly:

`espeak -w {{path/to/output.wav}} "{{text}}"`

- List all available voices:

`espeak --voices`
