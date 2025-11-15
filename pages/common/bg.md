# bg

> Resume suspended jobs (e.g. using `<Ctrl z>`), and keeps them running in the background.
> See also: `jobs`, `fg`, `disown`.
> More information: <https://www.gnu.org/software/bash/manual/bash.html#index-bg>.

- Resume the most recently suspended job and run it in the background:

`bg`

- Resume a specific job and run it in the background (run `jobs` to find the job number):

`bg %{{job_number}}`
