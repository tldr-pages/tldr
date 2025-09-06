# am

> Android 活动管理器。
> 更多信息：<https://developer.android.com/tools/adb#am>.

- 启动一个指定的活动：

`am start -n {{com.android.settings/.Settings}}`

- 启动一个活动并将数据传递给它：

`am start -a {{android.intent.action.VIEW}} -d {{tel:123}}`

- 启动与特定操作和类别匹配的活动：

`am start -a {{android.intent.action.MAIN}} -c {{android.intent.category.HOME}}`

- 将意图转换为 URI：

`am to-uri -a {{android.intent.action.VIEW}} -d {{tel:123}}`
