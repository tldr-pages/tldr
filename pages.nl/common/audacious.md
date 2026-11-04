# audacious

> Een open-source audiospeler. Indirect gebaseerd op XMMS.
> Zie ook: `audtool`, `clementine`, `mpc`, `ncmpcpp`.
> Meer informatie: <https://manned.org/audacious>.

- Start de GUI:

`audacious`

- Start een nieuwe instantie en speel een audiobestand af:

`audacious {{[-N|--new-instance]}} {{pad/naar/audio}}`

- Voeg een specifieke map met audiobestanden toe aan de wachtrij:

`audacious {{[-e|--enqueue]}} {{pad/naar/map}}`

- Start of stop de weergave:

`audacious {{[-t|--play-pause]}}`

- Spring vooruit ([fwd]) of achteruit ([rew]) in de afspeellijst:

`audacious --{{fwd|rew}}`

- Stop de weergave:

`audacious {{[-s|--stop]}}`

- Start in CLI-modus (headless):

`audacious {{[-H|--headless]}}`

- Sluit af zodra de weergave stopt of er niets meer is om af te spelen:

`audacious {{[-q|--quit-after-play]}}`
