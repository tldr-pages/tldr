# mkdir

> יצירת תיקיות והגדרת ההרשאות שלהן.
> למידע נוסף: <https://www.gnu.org/software/coreutils/manual/html_node/mkdir-invocation.html>.

- יצירת תיקיות מסוימות:

`mkdir {{path/to/directory1 path/to/directory2 ...}}`

- יצירת תיקיות מסוימות ואת תיקיות האב שלהן במידת הצורך:

`mkdir {{[-p|--parents]}} {{path/to/directory1 path/to/directory2 ...}}`

- יצירת תיקיות עם הרשאות מסוימות:

`mkdir {{[-m|--mode]}} {{u=rwx,g=rw,o=r}} {{path/to/directory1 path/to/directory2 ...}}`

- יצירת מספר תיקיות מקוננות באופן רקורסיבי:

`mkdir {{[-p|--parents]}} {{path/to/{a,b}/{x,y,z}/{h,i,j}}}`
