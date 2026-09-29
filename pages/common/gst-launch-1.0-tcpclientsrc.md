# gst-launch-1.0 tcpclientsrc

> Receive data from a server.
> More information: <https://gstreamer.freedesktop.org/documentation/tcp/tcpclientsrc.html>.

- Receive data from a server that is waiting to transmit it:

` gst-launch-1.0 tcpclientsrc port={{port}} ! {{pipeline}}`
