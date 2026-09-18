# onenote

> Microsoft OneNote (Classic), the note-taking application.
> More information: <https://support.microsoft.com/onenote/command-line-switches-in-onenote-2016>.

- Launch OneNote:

`onenote`

- Open a specific `.one` file:

`onenote "{{path\to\file.one}}"`

- Create a new section in the currently viewed notebook:

`onenote /new`

- Open a file as read-only:

`onenote /openro "{{path\to\file.one}}"`

- Print a `.one` file:

`onenote /print "{{path\to\file.one}}"`

- Start OneNote in a miniature window with the Quick Notes section open:

`onenote /sidenote`

- Immediately start recording audio or video on the current page:

`onenote /audionote|/videonote`

- Stop any active recording session:

`onenote /stoprecording`

- Paste the contents of the clipboard onto the current page:

`onenote /paste`

- Start OneNote in Safe Mode:

`onenote /safe`
