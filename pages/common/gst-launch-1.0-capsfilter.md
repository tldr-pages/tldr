# gst-launch-1.0 capsfilter

> Filter pipeline capabilities.
> More information: <https://gstreamer.freedesktop.org/documentation/coreelements/capsfilter.html>.

- Filter to only allow greyscale format:

`gst-launch-1.0 videotestsrc ! capsfilter caps=video/x-raw,format=GRAY8 ! videoconvert ! autovideosink`

- Do the same but in shortform:

`gst-launch-1.0 videotestsrc ! video/x-raw,format=GRAY8 ! videoconvert ! autovideosink`

- Limit video capabilities to specific dimensions:

`gst-launch-1.0 videotestsrc ! video/x-raw,width={{640}},height={{480}} ! videoconvert ! autovideosink`

- Specify a specific framerate:

`gst-launch-1.0 videotestsrc ! video/x-raw,framerate={{30}}/1 ! videoconvert ! autovideosink`
