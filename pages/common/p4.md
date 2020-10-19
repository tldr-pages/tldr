# p4

> Perforce Version Control System.
> More information: <https://www.perforce.com/manuals/cmdref>.

- Log in to the Perforce service:

`p4 login -a`

- Create a client:

`p4 client`

- Copy files from depot into the client workspace:

`p4 sync`

- Create or edit changelist description:

`p4 change`

- Open a file to edit:

`p4 edit -c {{changelist_number}} {{filename}}`

- Open a new file to add it to the depot:

`p4 add`

- Display list of files modified by changelist:

`p4 describe -c {{changelist_number}}`

- Submit a changelist to the depot:

`p4 submit -c {{changelist_number}}`
