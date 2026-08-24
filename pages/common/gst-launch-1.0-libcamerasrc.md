# gst-launch-1.0 libcamerasrc

> Read frames from a libcamera device.
> More information: <https://libcamera.org/getting-started.html#using-gstreamer-plugin>.

- View video in a window:

`gst-launch-1.0 libcamerasrc ! videoconvert ! autovideosink`

- Specify the device to read from:

`gst-launch-1.0 libcamerasrc camera-name={{camera_name}} ! {{videoconvert ! autovideosink}}`
