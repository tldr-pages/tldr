# jmap

> Java memory map eszköz. További információ: <https://docs.oracle.com/javase/7/docs/technotes/tools/share/jmap.html>.

- Megosztott objektum leképezések nyomtatása egy Java folyamathoz (kimenet, mint a pmap):

`jmap {{java_pid}}`

- Heap-összefoglaló információk nyomtatása:

`jmap -heap {{filename.jar}} {{java_pid}}`

- A halomhasználat hisztogramjának nyomtatása típusonként:

`jmap -histo {{java_pid}}`

- A heap tartalmának bináris fájlba történő kiürítése a jhat segítségével történő elemzéshez:

`jmap -dump:format=b,file={{path/to/file}} {{java_pid}}`
