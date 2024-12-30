# am

> Android 活动管理器。
> 更多信息：<https://developer.android.com/tools/adb#am>。

- 使用特定组件和包 [n]ame 启动活动：

`am start -n {{com.android.settings/.Settings}}`

- 启动一个意图 [a]ction 并传递 [d]ata：

`am start -a {{android.intent.action.VIEW}} -d {{tel:123}}`

- 启动与特定意图和 [c]ategory 匹配的活动：

`am start -a {{android.intent.action.MAIN}} -c {{android.intent.category.HOME}}`

- 将意图转换为 URI：

`am to-uri -a {{android.intent.action.VIEW}} -d {{tel:123}}`