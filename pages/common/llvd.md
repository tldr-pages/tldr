# llvd

> Linkedin Learning Video Downloader.
> More information: <https://github.com/knowbee/llvd>.

- Download a [c]ourse using cookie-based authentication:

`llvd -c {{course-slug}} --cookies`

- Download a course at a specific [r]esolution:

`llvd -c {{course-slug}} -r 720`

- Download a course with [ca]ptions (subtitles):

`llvd -c {{course-slug}} --caption`

- Download a course [p]ath with [t]hrottling between 10 to 30 seconds:

`llvd -p {{path-slug}} -t {{10,30}} --cookies`
