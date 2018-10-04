# p4-change

> Command line tool for the Perforce version control system.

- Create a new changelist number:

`p4 change`

- Edit description corresponding to a changelist number:

`p4 change -c {{changelist_number}}`

- Checking files modified by changelist:

`p4 change -c {{changelist_number}}`

- Deleting a changelist: 

`p4 change -d {{changelist_number}}`

- Display list of pending and submitted changelists by a user:

`p4 changes -u {{user_name}}`
