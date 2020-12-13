# tmpmail

> A temporary email right from your terminal written in POSIX sh
> More information: <https://github.com/sdushantha/tmpmail>.

- Create a temporary email:

`tmpmail --generate`

- Lists messages and their numeric ID:

`tmpmail`

- View a temporary email's most recent email:

`tmpmail --recent`

- Open user specified message:

'tmpmail {{email_id}}

- View email as raw text without HTML tags:

`tmpmail --text`

- Open email with given browser (default is w3m):

`tmpmail --browser {{browser}}`
