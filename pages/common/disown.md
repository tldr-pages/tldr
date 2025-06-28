# disown

> Allow sub-processes to live beyond the shell that they are attached to.
> See also: `jobs` for finding job numbers.
> More information: <https://www.gnu.org/software/bash/manual/bash.html#index-disown>.

- Disown the current job:

`disown`

- Disown a specific job (run `jobs` to find the job number):

`disown %{{job_number}}`

- Disown all jobs (Bash only):

`disown -a`

- Keep job (do not disown it), but mark it so that no future SIGHUP is received on shell exit (Bash only):

`disown -h %{{job_number}}`
