# ac

> Print statistics on how long users have been connected.
> More information: <https://www.gnu.org/software/acct/manual/accounting.html#ac>.

- Print how long the current user has been connected in hours:

`ac`

- Print how long users have been connected in hours:

`ac {{[-p|--individual-totals]}}`

- Print how long a particular user has been connected in hours:

`ac {{[-p|--individual-totals]}} {{username}}`

- Print how long a particular user has been connected in hours per day (with total):

`ac {{[-d|--daily-totals]}} {{[-p|--individual-totals]}} {{username}}`

- Also display additional details:

`ac --compatibility`
