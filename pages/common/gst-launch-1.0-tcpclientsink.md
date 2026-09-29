# gst-launch-1.0 tcpclientsink

> Send data to a server.
> More information: <https://gstreamer.freedesktop.org/documentation/tcp/tcpclientsink.html>.

- Send data to a server and specify its IP and port:

`gst-launch-1.0 {{pipeline}} ! tcpclientsink host={{server_ip_address}}`
