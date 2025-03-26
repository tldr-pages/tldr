# git add

> يضيف الملفات المعدلة إلى منطقة التجميع (staging area).
> لمزيد من التفاصيل: <https://git-scm.com/docs/git-add>.

- إضافة ملف إلى منطقة التجميع (staging area):

`git add {{path/to/file}}`

- إضافة جميع الملفات (المتتبَّعة وغير المتتبَّعة Tracked & Untracked):

`git add {{[-A|--all]}}`

- إضافة جميع الملفات بشكل متكرر (recursively) بدءًا من المُجَلَّد الحالي:

`git add .`

- إضافة الملفات المتتبَّعة (Tracked) فقط:

`git add {{[-u|--update]}}`

- إضافة الملفات المتجاهلة (Ignored) أيضًا:

`git add {{[-f|--force]}}`

- إضافة أجزاء من الملفات بشكل تفاعلي (Interactive):

`git add {{[-p|--patch]}}`

- إضافة أجزاء من ملف معين بشكل تفاعلي:

`git add {{[-p|--patch]}} {{path/to/file}}`

- إضافة ملف بشكل تفاعلي:

`git add {{[-i|--interactive]}}`
