# pwck

> Verify the integrity of the password files (`/etc/passwd` and `/etc/shadow`).
> See also: `grpck`, `vipw`.
> More information: <https://manned.org/pwck>.

- Check the password files and interactively fix errors:

`sudo pwck`

- Check the password files without making any changes:

`sudo pwck {{[-r|--read-only]}}`

- Check the password files and only report errors, ignoring warnings:

`sudo pwck {{[-q|--quiet]}}`

- Sort entries in the password files by user ID (modifies the files; cannot be combined with `--read-only`):

`sudo pwck {{[-s|--sort]}}`

- Check specific password and shadow files:

`sudo pwck {{[-r|--read-only]}} {{path/to/passwd}} {{path/to/shadow}}`
