# say

> Converts text to speech.

- Speak a phrase aloud:

`say {{"I like to ride my bike."}}`

- Speak a file aloud:

`say -f {{filename}}`

- Speak a phrase with a custom voice and speech rate:

`say -v {{voice}} -r {{words_per_minute}} {{"I'm sorry Dave, I can't let you do that."}}`

- List the available voices:

`say -v ?`

- Create an audio file of the spoken text:

`say -o {{filename.aiff}} {{"Everyone loves iTunes."}}`
