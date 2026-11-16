# mkdir

> יצירת תיקיות והגדרת הרשאות.
> למידע נוסף: <https://www.gnu.org/software/coreutils/manual/html_node/mkdir-invocation.html>.

- יצירת תיקיות ספציפיות:

`mkdir {{path/to/directory1 path/to/directory2 ...}}`

- יצירת תיקיות ספציפיות ואת תיקיות האב שלהן במידת הצורך:

`mkdir {{[-p|--parents]}} {{path/to/directory1 path/to/directory2 ...}}`

- יצירת תיקיות עם הרשאות ספציפיות:

`mkdir {{[-m|--mode]}} {{u=rwx,g=rw,o=r}} {{path/to/directory1 path/to/directory2 ...}}`

- יצירת תיקיות מקוננות באופן רקורסיבי:

`mkdir {{[-p|--parents]}} {{path/to/{a,b}/{x,y,z}/{h,i,j}}}`
