# mumble

> Low-latency, high quality voice chat software.
> More information: <https://www.mumble.info>.

- Open Mumble:

`mumble`

- Open Mumble and immediately connect to a server:

`mumble mumble://{{username}}@{{example.com}}`

- Open Mumble and immediately connect to a password protected server:

`mumble mumble://{{username}}:{{password}}@{{example.com}}`

- Mute/unmute the microphone in a running Mumble instance:

`mumble rpc {{mute|unmute}}`

- Mute/unmute the microphone and the audio output of Mumble:

`mumble rpc {{deaf|undeaf}}`
