# espeak

> Uses text-to-speech to speak through the default sound device.

- Speak a phrase aloud:

`espeak "I like to ride my bike."`

- Speak a file aloud:

`espeak -f {{filename}}`

- Save output to a WAV audio file, rather than speaking it directly:

`espeak -w {{filename.wav}} "It's GNU plus Linux"`

- Use a different voice:

`espeak -v {{voice}}`
