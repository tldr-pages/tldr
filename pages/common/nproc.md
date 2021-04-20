# nproc

> Print the number of processing units (normally CPUs) available.
> More information: <https://www.gnu.org/software/coreutils/nproc>.

- Display the number of available processing units:

`nproc`

- Display the number of installed processing units, including any inactive ones:

`nproc --all`

- If possible, subtract a given number of units from the returned value:

`nproc --ignore {{count}}`
