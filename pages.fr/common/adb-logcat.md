# adb-logcat

> Jeter une log des messages systèmes.
> Plus d'informations : <https://developer.android.com/tools/logcat>.

- Affiche les logs systèmes :

`adb logcat`

- Affiche les logs qui correspond à une expression régulière :

`adb logcat -e {{expression_régulière}}`

- Affiche les logs pour un tag donné, dans un mode spécifique ([V]erbose, [D]ebug, [I]nfo, [W]arning, [E]rror, [F]atal, [S]ilent) :

`adb logcat {{tag}}:{{mode}} *:S`

- Affiche les logs pour des applications React Native en mode [V]erbose et mes sous [S]ilence les autres tags :

`adb logcat ReactNative:V ReactNativeJS:V *:S`

- Affiche les logs avec un niveau de priorité supérieur à [W]arning :

`adb logcat *:W`

- Colorie les logs (souvent utilisé avec des filtres) :

`adb logcat -v color`
