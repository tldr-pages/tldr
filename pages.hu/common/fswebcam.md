# fswebcam

> Kicsi és egyszerű webkamera \*nixhez. További információ: <https://www.sanslogic.co.uk/fswebcam>.

- Készítsen egy képet:

`fswebcam {{filename}}`

- Készítsen képet egyéni felbontással:

`fswebcam -r {{width}}x{{height}} {{filename}}`

- Készítsen képet a kiválasztott eszközről(alapértelmezett: `/dev/video0`):

`fswebcam -d {{device}} {{filename}}`

- Készítsen képet időbélyeggel(az időbélyeg string strftime-mal van formázva):

`fswebcam --timestamp {{timestamp}} {{filename}}`
