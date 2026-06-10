# gst-launch-1.0 libcamerasrc

> Կարդացեք շրջանակները libcamera սարքից:.
> Լրացուցիչ տեղեկություններ. <https://libcamera.org/getting-started.html#using-gstreamer-plugin>:.

- Դիտեք տեսանյութը պատուհանում.:

`gst-launch-1.0 libcamerasrc ! videoconvert ! autovideosink`

- Նշեք սարքը, որտեղից պետք է կարդալ.:

`gst-launch-1.0 libcamerasrc camera-name={{camera_name}} ! {{videoconvert ! autovideosink}}`
