# audacious

> An open-source audio player. Indirectly based on XMMS.
> See also: `audtool`, `clementine`, `mpc`, `ncmpcpp`.
> More information: <https://audacious-media-player.org>.

- Launch the GUI:

`audacious`

- Start a new instance and play an audio:

`audacious --new-instance {{path/to/audio}}`

- Enqueue a specific directory of audio files:

`audacious --enqueue {{path/to/directory}}`

- Start or stop playback:

`audacious --play-pause`

- Skip forwards ([fwd]) or backwards ([rew]) in the playlist:

`audacious --{{fwd|rew}}`

- Stop playback:

`audacious --stop`

- Start in CLI mode (headless):

`audacious --headless`

- Exit as soon as playback stops or there is nothing to playback:

`audacious --quit-after-play`
