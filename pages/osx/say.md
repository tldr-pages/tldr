# say

> Converts text to speech.
> More information: <https://ss64.com/osx/say.html>.

- Say a phrase aloud:

`say "{{I like to ride my bike.}}"`

- Read a file aloud:

`say -f {{filename.txt}}`

- Say a phrase with a custom voice and speech rate:

`say -v {{voice}} -r {{words_per_minute}} "{{I'm sorry Dave, I can't let you do that.}}"`

- List the available voices:

`say -v "?"`

- Create an audio file of the spoken text:

`say -o {{filename.aiff}} "{{Here's to the Crazy Ones.}}"`
