# cat

> הדפסה ושרשור של קבצים.
> למידע נוסף: <https://manned.org/cat.1posix>.

- הדפסת תוכן של קובץ ל-`stdout`:

`cat {{path/to/file}}`

- שרשור מספר קבצים לקובץ פלט:

`cat {{path/to/file1 path/to/file2 ...}} >{{path/to/output_file}}`

- הוספת מספר קבצים לסוף קובץ פלט:

`cat {{path/to/file1 path/to/file2 ...}} >>{{path/to/output_file}}`

- העתקת תוכן של קובץ לקובץ פלט ללא חציצה (buffering):

`cat -u {{/dev/tty12}} >{{/dev/tty13}}`

- כתיבה מ-`stdin` לקובץ:

`cat - >{{path/to/file}}`
