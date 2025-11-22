# audacious

> An open-source audio player. Indirectly based on XMMS.
> See also: `audtool`, `clementine`, `mpc`, `ncmpcpp`.
> More information: <https://manned.org/audacious>.

- Launch the GUI:

`audacious`

- Start a new instance and play an audio:

`audacious {{[-N--new-instance]}} {{path/to/audio}}`

- Enqueue a specific directory of audio files:

`audacious {{[-e|--enqueue]}} {{path/to/directory}}`

- Start or stop playback:

`audacious {{[-t|--play-pause]}}`

- Skip forwards ([fwd]) or backwards ([rew]) in the playlist:

`audacious --{{fwd|rew}}`

- Stop playback:

`audacious {{[-s|--stop]}}`

- Start in CLI mode (headless):

`audacious {{[-H|--headless]}}`

- Exit as soon as playback stops or there is nothing to playback:

`audacious {{[-q|--quit-after-play]}}`
