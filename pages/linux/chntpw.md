# chntpw

> Chntpw is utility that can edit windows registry, reset user password, promote users to administrator by modifying the Windows SAM.
> Supports all Windows from NT3.5 to Win8.1, also 64 bit and also the Server versions (like 2003, 2008, 2012). 
> Boot target machine with live cd like Kali Linux and run elevated privileges. More information: <http://pogostick.net/~pnh/ntpasswd>.

- [l]ist all users in the SAM file:

`chntpw -l {{path/to/SAM_file}}`

- Edit [u]ser interactively :

`chntpw -u {{user_name}} {{path/to/SAM_file}}`

- Use chntpw [i]nteractively
`chntpw -i {{path/to/SAM_file}}`
