# mh_metric

> Calculate and enforce code metrics for MATLAB or Octave code.
> More information: <https://misshit.org/>.

- Display code metrics for a MATLAB file:

`mh_metric {{filename.m}}`

- Display code metrics for an Octave file:

`mh_metric --octave {{filename.m}}`

- Display code metrics for everything in a directory:

`mh_metric {{path/to/<placeholder>}}`

- Display code metrics for everything in the current directory tree:

`mh_metric`

- Produce an HTML report instead of plain text:

`mh_metric --html {{filename.html}}`

- Produce a JSON report instead of plain text:

`mh_metric --json {{filename.json}}`
