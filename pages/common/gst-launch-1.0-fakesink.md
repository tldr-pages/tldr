# gst-launch-1.0 fakesink

> Dummy sink that swallows everything.
> Useful for testing what part of a pipeline is breaking.
> More information: <https://gstreamer.freedesktop.org/documentation/coreelements/fakesink.html>.

- Consume data from a pipeline without outputting it:

`gst-launch-1.0 {{pipeline}} ! fakesink`
