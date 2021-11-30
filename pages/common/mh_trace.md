# mh_trace

> Extract tracing tags from MATLAB or Octave code.
> More information: <https://misshit.org/>.

- Add this comment to tag a function/block/class/file:

`%| pragma Tag ({{"my_tag"}});`

- Add this comment to exclude a function/block/class/file:

`%| pragma No_Tracing;`

- Or use the existing TestTags feature from MATLAB:

`classdef (TestTags = {{{'my_tag'}}})`

- Extract tracing tags from all files:

`mh_trace`

- Extract tracing tags from all files in a file:

`mh_trace {{filename.m}}`

- Specify the name of the JSON file:

`mh_trace --json={{filename.json}}`
