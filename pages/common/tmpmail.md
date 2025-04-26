# tmpmail

> A temporary email right from your terminal written in POSIX sh.
> More information: <https://github.com/sdushantha/tmpmail#usage>.

- Create a temporary inbox:

`tmpmail {{[-g|--generate]}}`

- List messages and their numeric ID:

`tmpmail`

- Display the most recent received email:

`tmpmail {{[-r|--recent]}}`

- Open a specific message:

`tmpmail {{email_id}}`

- View email as raw text without HTML tags:

`tmpmail {{[-t|--text]}}`

- Open email with a specific browser (default is w3m):

`tmpmail {{[-b|--browser]}} {{browser}}`
