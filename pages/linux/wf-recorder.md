# wf-recorder

> Screencast for Wayland optionally with audio.
> By default you need to end the process with `<Ctrl c>`.
> More information: <https://github.com/ammen99/wf-recorder>.

- Record storing to an MP4 file:

`wf-recorder {{[-f|--file]}} {{output.mp4}}`

- Record including audio, both with mic and system sounds:

`wf-recorder {{[-a|--audio]}} {{[-f|--file]}} {{/path/to/file_with_audio.webm}}`

- Select and record a portion of the screen using `slurp`, outputting to default `recording.mp4`:

`wf-recorder {{[-g|--geometry]}} "$(slurp)"`
