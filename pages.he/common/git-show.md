# git show

> הצגת אובייקטים מסוגים שונים ב-Git (כגון commits ותגיות).
> למידע נוסף: <https://git-scm.com/docs/git-show>.

- הצגת מידע על ה-commit האחרון (מזהה, הודעה, שינויים ופרטים נוספים):

`git show`

- הצגת מידע על commit, תגית או ענף מסוימים (למשל `HEAD` עבור ה-commit האחרון):

`git show {{commit|tag|branch}}`

- הצגת רשימת הקבצים שנוספו, ששמם שונה או שנמחקו בלבד:

`git show --summary {{commit}}`

- התעלמות מתווי רווח בעת השוואת שורות:

`git show {{[-w|--ignore-all-space]}}`

- הצגת הודעת commit בשורה אחת, ללא הצגת ההבדלים:

`git show --oneline {{[-s|--no-patch]}} {{commit}}`

- הצגת נתונים סטטיסטיים על הקבצים שהשתנו (כגון מספר השורות שנוספו ונמחקו):

`git show --stat {{commit}}`

- הצגת רשימה פשוטה של כל הקבצים שהשתנו ב-commit (שונו, נוספו או נמחקו):

`git show --name-only {{commit}}`

- הצגת תוכן קובץ כפי שהיה בגרסה מסוימת (למשל ענף, תגית או commit):

`git show {{revision}}:{{path/to/file}}`
