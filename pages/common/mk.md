# mk

> Task runner for targets described in Mkfile.
> Mostly used to control the compilation of an executable from source code.
> More information: <http://doc.cat-v.org/plan_9/4th_edition/papers/mk>.

- Call the first target specified in the Mkfile (usually named "all"):

`mk`

- Call a specific target:

`mk {{target}}`

- Call a specific target, executing 4 jobs at a time in parallel:

`NPROC=4 mk {{target}}`

- Force mking of a target, even if source files are unchanged:

`mk -w{{target}} {{target}}`

- Assume all targets to be out of date. Thus, update `target` and all of its dependencies:

`mk -a {{target}}`

- Keep going as far as possible on error:

`mk -k`
