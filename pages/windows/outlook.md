# outlook

> Microsoft Outlook (Classic), the email and calendar client.
> More information: <https://support.microsoft.com/office/command-line-switches-for-microsoft-office-products-079164cd-4ef5-4178-b235-441737deb3a6#category=classic_outlook>.

- Launch classic Outlook:

`outlook`

- Launch with a specific profile:

`outlook /profile "{{profile_name}}"`

- Launch with the Reading Pane off:

`outlook /nopreview`

- Launch in Safe Mode (no Reading Pane, toolbar customizations, or COM add-ins):

`outlook /safe`

- Launch and open a specific folder (e.g. the default calendar) in a new window:

`outlook /select {{outlook:calendar}}`

- Compose a new email message:

`outlook /c ipm.note`

- Compose a new email message addressed to a specific recipient:

`outlook /c ipm.note /m {{email@example.com}}`

- Open a specified message (`.msg`) file:

`outlook /f {{path\to\file.msg}}`
