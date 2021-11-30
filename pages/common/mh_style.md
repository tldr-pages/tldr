# mh_style

> Style check and auto-format MATLAB or Octave code.
> More information: <https://misshit.org/>.

- Style check a MATLAB file:

`mh_style {{filename.m}}`

- Style check an Octave file:

`my_style --octave {{filename.m}}`

- Style check embedded code inside a Simulink model:

`mh_style --process-slx {{filename.slx}}`

- Auto-fix format problems in a file:

`mh_style --fix {{filename.m}}`

- Process an entire directory:

`mh_style {{path/to/<placeholder>}}`

- Process and fix everything in the current directory:

`mh_style --fix`
