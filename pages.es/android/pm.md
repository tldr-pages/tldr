# pm

> Muestra información sobre aplicaciones en un dispositivo Android.
> Más información: <https://developer.android.com/studio/command-line/adb#pm>.

- Genera una lista de todas las aplicaciones instaladas:

`pm list packages`

- Genera una lista de todas las aplicaciones del sistema instaladas:

`pm list packages -s`

- Genera una lista de todas las aplicaciones de terceros instaladas:

`pm list packages -3`

- Genera una lista de aplicaciones que coinciden con determinadas palabras clave:

`pm list packages {{palabras_clave}}`

- Imprime la ruta del APK de una aplicación específica:

`pm path {{app}}`
