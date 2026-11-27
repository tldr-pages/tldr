# mv

> העברה או שינוי שם של קבצים ותיקיות.
> למידע נוסף: <https://www.gnu.org/software/coreutils/manual/html_node/mv-invocation.html>.

- שינוי שם של קובץ או תיקייה, כשהיעד אינו תיקייה קיימת:

`mv {{path/to/source}} {{path/to/target}}`

- העברת קובץ או תיקייה לתוך תיקייה קיימת:

`mv {{path/to/source}} {{path/to/existing_directory}}`

- העברת מספר קבצים לתוך תיקייה קיימת, בלי לשנות את שמות הקבצים:

`mv {{path/to/source1 path/to/source2 ...}} {{path/to/existing_directory}}`

- דריסת קבצים קיימים בלי לבקש אישור:

`mv {{[-f|--force]}} {{path/to/source}} {{path/to/target}}`

- בקשת אישור באופן אינטראקטיבי לפני דריסת קבצים קיימים, בלי קשר להרשאות הקבצים:

`mv {{[-i|--interactive]}} {{path/to/source}} {{path/to/target}}`

- העברה בלי לדרוס קבצים קיימים ביעד:

`mv {{[-n|--no-clobber]}} {{path/to/source}} {{path/to/target}}`

- העברת קבצים במצב מפורט, עם הצגת הקבצים אחרי שהועברו:

`mv {{[-v|--verbose]}} {{path/to/source}} {{path/to/target}}`

- ציון תיקיית היעד, כדי שאפשר יהיה לאסוף את הקבצים להעברה בעזרת כלים חיצוניים:

`{{find /var/log -type f -name '*.log' -print0}} | {{xargs -0}} mv {{[-t|--target-directory]}} {{path/to/target_directory}}`
