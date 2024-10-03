# chntpw

> A utility that can edit windows registry, reset user password, promote users to administrator by modifying the Windows SAM.
> Boot target machine with live cd like Kali Linux and run with elevated privileges.
> More information: <https://pogostick.net/~pnh/ntpasswd>.

- List all users in the SAM file:

`chntpw -l {{path/to/sam_file}}`

- Edit user interactively:

`chntpw -u {{username}} {{path/to/sam_file}}`

- Use chntpw interactively:

`chntpw -i {{path/to/sam_file}}`
