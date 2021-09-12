# pm

> 顯示關於 Android 裝置上的應用程式的資訊。
> 更多資訊：<https://developer.android.com/studio/command-line/adb#pm>.

- 印出所有已安裝應用程式的列表：

`pm list packages`

- 印出所有已安裝的系統應用程式的列表：

`pm list packages -s`

- 印出所有已安裝的第三方應用程式的列表：

`pm list packages -3`

- 印出與指定關鍵字匹配的應用程式列表：

`pm list packages {{關鍵詞}}`

- 印出指定應用程式的 APK 的路徑：

`pm path {{應用名}}`
