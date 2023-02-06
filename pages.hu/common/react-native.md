# react-native

> Egy keretrendszer natív alkalmazások építéséhez React segítségével. További információ: <https://reactnative.dev>.

- Inicializáljon egy új React Native projektet egy azonos nevű könyvtárban:

`react-native init {{project_name}}`

- Indítsa el a metro bundlert:

`react-native start`

- Indítsa el a metro bundlert tiszta gyorsítótárral:

`react-native start --reset-cache`

- Építse az aktuális alkalmazást, és indítsa el egy csatlakoztatott Android-eszközön vagy emulátoron:

`react-native run-android`

- Építse az aktuális alkalmazást, és indítsa el egy iOS-szimulátoron:

`react-native run-ios`

- Az aktuális alkalmazás elkészítése `release` módban és elindítása egy csatlakoztatott Android-eszközön vagy emulátoron:

`react-native run-android --variant={{release}}`

- A `logkitty` elindítása és a naplók kinyomtatása a `stdout` címre:

`react-native log-android`

- A `tail system.log` elindítása egy iOS-szimulátoron, és a naplók kinyomtatása a `stdout` címre:

`react-native log-ios`
