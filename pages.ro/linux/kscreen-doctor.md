# kscreen-doctor

> Modificați și manipulați configurarea ecranului din linia de comandă.
> Mai multe informaţii: <https://invent.kde.org/plasma/libkscreen>

- Afișează informațiile de ieșire de afișare:

`kscreen-doctor --outputs`

- Setați rotația unei ieșiri de afișare cu un ID de 1 spre dreapta:

`kscreen-doctor {{output.1.rotation.right}}`

- Setați scara unei ieșiri de afișare cu un ID de `HDMI-2` la 2 (200%):

`kscreen-doctor {{output.HDMI-2.scale.2}}`
