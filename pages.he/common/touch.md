# touch

> יצירת קבצים וקביעת זמני הגישה והשינוי שלהם.
> למידע נוסף: <https://www.gnu.org/software/coreutils/manual/html_node/touch-invocation.html>.

- יצירת קבצים מסוימים, או עדכון חותמות הזמן שלהם אם הם כבר קיימים:

`touch {{path/to/file1 path/to/file2 ...}}`

- קביעת זמן הגישה או זמן השינוי של הקבצים לזמן הנוכחי, בלי ליצור קובץ שאינו קיים:

`touch {{[-c|--no-create]}} {{-a|-m}} {{path/to/file1 path/to/file2 ...}}`

- קביעת זמן הקבצים לערך מסוים, בלי ליצור קובץ שאינו קיים:

`touch {{[-c|--no-create]}} -t {{YYYYMMDDHHMM.SS}} {{path/to/file1 path/to/file2 ...}}`

- קביעת חותמת הזמן של הקבצים לפי חותמת הזמן של קובץ ייחוס, בלי ליצור קובץ שאינו קיים:

`touch {{[-c|--no-create]}} {{[-r|--reference]}} {{path/to/reference_file}} {{path/to/file1 path/to/file2 ...}}`

- קביעת חותמת הזמן מתוך מחרוזת:

`touch {{[-d|--date]}} "{{last year|5 hours|next thursday|nov 14|...}}" {{path/to/file}}`

- יצירת מספר קבצים עם מספר עולה:

`touch {{path/to/file{1..10}}}`

- יצירת מספר קבצים לפי טווח אותיות:

`touch {{path/to/file{a..z}}}`
