# gst-launch-1.0 tcpcserversrc

> Receive data sent by a client.
> More information: <https://gstreamer.freedesktop.org/documentation/tcp/tcpserversrc.html>.

- Set up a server to receive data:

`gst-launch-1.0 tcpserversrc host={{accepted_ip_address}} ! {{pipeline}}`
