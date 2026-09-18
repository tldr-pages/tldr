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

- Create a new item of the specified message class (e.g. an email, appointment, or contact):

`outlook /c {{ipm.note|ipm.appointment|ipm.contact}}`

- Create an email addressed to a specific recipient (used together with `/c ipm.note`):

`outlook /c ipm.note /m {{email@example.com}}`

- Open a specified message (`.msg`), calendar (`.ics`/`.vcs`), or contact (`.vcf`) file:

`outlook /f {{path\to\file.msg}} /ical {{path\to\file.ics}} /vcal {{path\to\file.vcs}} /v {{path\to\file.vcf}}`

- Create an item with a specified file attached:

`outlook /a {{path\to\file}}`

- Reset the Folder Pane (navigation pane) for the current profile:

`outlook /resetnavpane`
