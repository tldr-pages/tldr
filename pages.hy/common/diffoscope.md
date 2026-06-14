# դիֆոսկոպ

> Համեմատեք ֆայլերը, արխիվները և գրացուցակները:.
> Լրացուցիչ տեղեկություններ. <https://manned.org/diffoscope>:.

- Համեմատեք երկու ֆայլ.:

`diffoscope {{path/to/file1}} {{path/to/file2}}`

- Համեմատեք երկու ֆայլ առանց առաջընթացի տող ցուցադրելու.:

`diffoscope --no-progress {{path/to/file1}} {{path/to/file2}}`

- Համեմատեք երկու ֆայլ և գրեք HTML հաշվետվություն ֆայլի մեջ (օգտագործեք `-` `stdout`-ի համար):

`diffoscope --html {{path/to/outfile|-}} {{path/to/file1}} {{path/to/file2}}`

- Համեմատեք երկու դիրեկտորիաներ, բացառությամբ ֆայլերի, որոնք համապատասխանում են նշված օրինակին.:

`diffoscope --exclude {{pattern}} {{path/to/directory1}} {{path/to/directory2}}`

- Համեմատեք երկու գրացուցակ և վերահսկեք, թե արդյոք գրացուցակի մետատվյալները համարվում են.:

`diffoscope --exclude-directory-metadata {{auto|yes|no|recursive}} {{path/to/directory1}} {{path/to/directory2}}`
