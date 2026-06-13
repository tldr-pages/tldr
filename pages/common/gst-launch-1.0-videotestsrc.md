# gst-launch-1.0 videotestsrc

> Produce test video data.
> More information: <https://gstreamer.freedesktop.org/documentation/videotestsrc/index.html>.

- Produce a video with SMPTE color bars:

`gst-launch-1.0 videotestsrc ! {{autovideosink}}`

- Define what type of test video to produce:

`gst-launch-1.0 videotestsrc pattern={{smpte|snow|green|ball|circular|...}} ! {{autovideosink}}`
