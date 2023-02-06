# xctool

> Xcode projektek létrehozására szolgáló eszköz. További információ: <https://github.com/facebook/xctool>.

- Egyetlen projekt építése munkaterület nélkül:

`xctool -project {{YourProject.xcodeproj}} -scheme {{YourScheme}} build`

- Egy munkaterület részét képező projekt építése:

`xctool -workspace {{YourWorkspace.xcworkspace}} -scheme {{YourScheme}} build`

- Tisztítsa meg, építse meg és hajtsa végre az összes tesztet:

`xctool -workspace {{YourWorkspace.xcworkspace}} -scheme {{YourScheme}} clean build test`
