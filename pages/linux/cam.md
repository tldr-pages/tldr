# cam

> Frontend tool for `libcamera`.
> See also: `v4l2-ctl`.
> More information: <https://libcamera.org/docs.html>.

- List available cameras:

`cam {{[-l|--list]}}`

- List controls of a camera:

`cam {{[-c|--camera]}} {{camera_index}} --list-controls`

- Write frames to a folder:

`cam {{[-c|--camera]}} {{camera_index}} {{[-C|--capture=]}}{{frames_to_capture}} {{[-F|--file]}}`

- Display camera feed in a window:

`cam {{[-c|--camera]}} {{camera_index}} {{[-C|--capture]}} {{[-S|--sdl]}}`
