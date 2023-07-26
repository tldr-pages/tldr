# cam

> Frontend tool for `libcamera`.
> More information: <https://libcamera.org/docs.html>.

- List available cameras:

`cam --list`

- List controls of a camera:

`cam --camera {{camera_index}} --list-controls`

- Write frames to a folder:

`cam --camera {{camera_index}} --capture={{frames_to_capture}} --file`

- Display camera feed in a window:

`cam --camera {{camera_index}} --capture --sdl`
