# llvd

> Linkedin Learning Video Downloader.
> More information: <https://github.com/knowbee/llvd>.

- Download a course using cookie-based authentication:

`llvd {{[-c|--course]}} {{course_slug}} --cookies`

- Download a course at a specific resolution:

`llvd {{[-c|--course]}} {{course_slug}} {{[-r|--resolution]}} 720`

- Download a course with captions (subtitles):

`llvd {{[-c|--course]}} {{course_slug}} {{[-ca|--caption]}}`

- Download a course path with throttling between 10 to 30 seconds:

`llvd {{[-p|--path]}} {{path_slug}} {{[-t|--throttle]}} {{10,30}} --cookies`
