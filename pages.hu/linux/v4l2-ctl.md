# v4l2-ctl

> Videóeszközök vezérlése. További információ: <https://manned.org/v4l2-ctl>.

- Az összes videóeszköz listázása:

`v4l2-ctl --list-devices`

- Az alapértelmezett videóeszköz támogatott videóformátumainak és felbontásainak listája `/dev/video0`:

`v4l2-ctl --list-formats-ext`

- Egy adott videokészülék támogatott videóformátumainak és felbontásainak listázása:

`v4l2-ctl --list-formats-ext --device {{path/to/video_device}}`

- Egy videóeszköz összes adatának lekérdezése:

`v4l2-ctl --all --device {{path/to/video_device}}`

- JPEG-fotó készítése egy adott felbontású videóeszközről:

`v4l2-ctl --device {{path/to/video_device}} --set-fmt-video=width={{width}},height={{height}},pixelformat=MJPG --stream-mmap --stream-to={{path/to/output.jpg}} --stream-count=1`

- Nyers videófolyam rögzítése a videóeszközről:

`v4l2-ctl --device {{path/to/video_device}} --set-fmt-video=width={{width}},height={{height}},pixelformat={{format}} --stream-mmap --stream-to={{path/to/output}} --stream-count={{number_of_frames_to_capture}}`

- A videóeszköz összes vezérlőelemének és értékeinek listázása:

`v4l2-ctl --list-ctrls --device {{/path/to/video_device}}`
