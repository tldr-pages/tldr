# fswebcam

> Cameră web mică și simplă pentru *nix.
> Mai multe informaţii: <https://www.sanslogic.co.uk/fswebcam>

- Fă o poză:

`fswebcam {{filename}}`

- Faceți o fotografie cu rezoluție personalizată:

`fswebcam -r {{width}}x{{height}} {{filename}}`

- Realizarea unei fotografii de pe dispozitivul selectat (Implicit este `/dev/video0`):

`fswebcam -d {{device}} {{filename}}`

- Faceți o fotografie cu timestamp (șirul timestamp este formatat de strftime):

`fswebcam --timestamp {{timestamp}} {{filename}}`
