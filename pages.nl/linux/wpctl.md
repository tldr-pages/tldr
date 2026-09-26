# wpctl

> Beheer WirePlumber, een sessie- en beleidsbeheerder voor PipeWire.
> Opmerking: je kunt de speciale naam `@DEFAULT_SINK@` gebruiken in plaats van `id` om de standaard sink te beheren.
> Zie ook: `pw-cli`.
> Meer informatie: <https://pipewire.pages.freedesktop.org/wireplumber/>.

- Toon alle objecten die door WirePlumber worden beheerd:

`wpctl status`

- Toon alle eigenschappen van een object:

`wpctl inspect {{object_id}}`

- Stel een object in als standaard binnen zijn groep:

`wpctl set-default {{object_id}}`

- Verkrijg het volume van een sink:

`wpctl get-volume {{sink_id}}`

- Stel het volume van een sink in op `n` procent:

`wpctl set-volume {{sink_id}} {{n}}%`

- Verhoog/verlaag het volume van een sink met `n` procent:

`wpctl set-volume {{sink_id}} {{n}}%{{+|-}}`

- Verhoog het volume van een sink met `n` procent, maar begrens het volume onder 100%:

`wpctl set-volume {{[-l|--limit]}} 1 {{sink_id}} {{n}}%-`

- Dempen/Opheffen van demping van de standaard audio sink of source (1 is dempen, 0 is opheffen):

`wpctl set-mute @DEFAULT_{{SINK|SOURCE}}@ {{1|0|toggle}}`
