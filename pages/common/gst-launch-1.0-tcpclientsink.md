# gst-launch-1.0 tcpclientsink

> Send data to a server.
> More information: <https://gstreamer.freedesktop.org/documentation/tcp/tcpclientsink.html>.

- Send data to a server on localhost:

`gst-launch-1.0 {{pipeline}} ! tcpclientsink`

- Send data to a server:

`gst-launch-1.0 {{pipeline}} ! tcpclientsink host={{server_ip_address}}`
