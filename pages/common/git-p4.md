# git-p4

> Import from and submit to Perforce repositories.
> More information: <https://git-scm.com/docs/git-p4>.

- Clone a Perforce depot into a new Git repository:

`git p4 clone {{path/to/p4_depot}}`

- Sync changes from Perforce into the current Git repository:

`git p4 sync {{path/to/p4_depot}}`

- Rebase local commits on top of the latest Perforce changes:

`git p4 rebase`

- Submit Git changes back to Perforce:

`git p4 submit`

- Clone the full Perforce history instead of only the latest changelist:

`git p4 clone {{p4-depot-path}}@all`
