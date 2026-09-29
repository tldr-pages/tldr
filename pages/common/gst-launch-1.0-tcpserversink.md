# gst-launch-1.0 tcpserversink

> Send data to a client.
> More information: <https://gstreamer.freedesktop.org/documentation/tcp/tcpserversink.html>.

- Set up a server to send data to a client:

`gst-launch-1.0 {{pipeline}} ! tcpserversink port={{port}}`
