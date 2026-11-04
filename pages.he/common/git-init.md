# git init

> אתחול מאגר Git מקומי חדש.
> למידע נוסף: <https://git-scm.com/docs/git-init>.

- אתחול מאגר מקומי חדש:

`git init`

- אתחול מאגר עם שם מוגדר לענף הראשוני:

`git init {{[-b|--initial-branch]}} {{branch_name}}`

- אתחול מאגר המשתמש ב-SHA256 לגיבוב אובייקטים (נדרשת גרסת Git 2.29 ומעלה):

`git init --object-format sha256`

- אתחול מאגר ללא תיקיית עבודה, המתאים לשימוש כמאגר מרוחק דרך SSH:

`git init --bare`
