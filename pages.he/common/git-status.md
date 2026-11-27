# git status

> הציגו את השינויים בקבצים במאגר Git.
> מפרט קבצים ששונו, נוספו או נמחקו בהשוואה ל-commit הנוכחי.
> למידע נוסף: <https://git-scm.com/docs/git-status>.

- הציגו קבצים שאינם במעקב וקבצים ששונו וטרם נוספו ל-commit:

`git status`

- הציגו את הפלט בפורמט מקוצר:

`git status {{[-s|--short]}}`

- הציגו את הפלט בפורמט מקוצר יחד עם מידע על הענף:

`git status {{[-sb|--short --branch]}}`

- הציגו את השינויים בקבצים שהוכנו ל-commit (כמו `git diff --cached`):

`git status {{[-v|--verbose]}}`

- הציגו את השינויים בכל הקבצים שבמעקב (כמו `git diff HEAD`):

`git status {{[-vv|--verbose --verbose]}}`

- הציגו את מספר הרשומות השמורות כעת ב-stash:

`git status --show-stash`

- הסתירו מהפלט קבצים שאינם במעקב:

`git status {{[-uno|--untracked-files=no]}}`
