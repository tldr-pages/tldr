# runas

> Run a program as another user.
> More information: <https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/cc771525(v=ws.11)>.

- Run a program as the Administrator local user:

`runas /user:.\Administrator "{{command}}"`

- Run a program as a specific user:

`runas /user:{{domain\username}} "{{command}}"`

- Run a program without loading the user's profile:

`runas /noprofile /user:{{domain\username}} "{{command}}"`

- Open Command Prompt as another user:

`runas /user:{{domain\username}} cmd`

- Run Notepad as a specific user with the current user's environment variables, opening a file with escaped quotes:

`runas /env /user:{{domain\username}} "notepad \"{{C:\path\to\file.txt}}\""`

- Run Active Directory Users and Computers as a specific user:

`runas /env /user:{{domain\username}} "mmc %windir%\system32\dsa.msc"`
