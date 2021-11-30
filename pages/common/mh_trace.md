# mh_trace

> Extract tracing tags from MATLAB or Octave code.
> More information: <https://misshit.org/>.

- Add this comment to tag a function/block/class/file:

`%| pragma Tag ("{{tag_name}}");`

- Add this comment to exclude a function/block/class/file:

`%| pragma No_Tracing;`

- Or use the existing TestTags feature from MATLAB:

`classdef (TestTags = {'{{tag_name}}'})`

- Extract tracing tags from all files:

`mh_trace`

- Extract tracing tags from all files in a file:

`mh_trace {{path/to/file.m}}`

- Specify the name of the JSON file:

`mh_trace --json={{path/to/file.json}}`
