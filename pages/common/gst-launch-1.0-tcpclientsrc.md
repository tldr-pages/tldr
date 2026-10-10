# gst-launch-1.0 tcpclientsrc

> Receive data from a server.
> More information: <https://gstreamer.freedesktop.org/documentation/tcp/tcpclientsrc.html>.

- Receive data from a server on localhost:

`gst-launch-1.0 tcpclientsrc ! {{pipeline}}`

- Receive data from a server:

`gst-launch-1.0 tcpclientsrc host={{server_ip_address}} ! {{pipeline}}`
