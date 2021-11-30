# mh_style

> Style check and auto-format MATLAB or Octave code.
> More information: <https://misshit.org/>.

- Style check a MATLAB file:

`mh_style {{path/to/file.m}}`

- Style check an Octave file:

`my_style --octave {{path/to/file.m}}`

- Style check embedded code inside a Simulink model:

`mh_style --process-slx {{path/to/file.slx}}`

- Auto-fix format problems in a file:

`mh_style --fix {{path/to/file.m}}`

- Process an entire directory:

`mh_style {{path/to/directory}}`

- Process and fix everything in the current directory:

`mh_style --fix`
