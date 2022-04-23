# am

> Android 活動管理器。
> 更多資訊：<https://developer.android.com/studio/command-line/adb#am>.

- 啟動一個指定的活動：

`am start -n {{com.android.settings/.Settings}}`

- 啟動一個活動並將資料傳遞給它：

`am start -a {{android.intent.action.VIEW}} -d {{tel:123}}`

- 啟動與特定操作和類別匹配的活動：

`am start -a {{android.intent.action.MAIN}} -c {{android.intent.category.HOME}}`

- 將意圖（intent）轉換為 URI：

`am to-uri -a {{android.intent.action.VIEW}} -d {{tel:123}}`
