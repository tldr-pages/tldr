# am

> Android Activity Manager（アクティビティ マネージャー）
> もっと詳しく: <https://developer.android.com/tools/adb#am>。

- 指定したコンポーネントとパッケージ名でアクティビティを開始します:

`am start -n {{com.android.settings/.Settings}}`

- インテントアクションを開始させ、データを渡します:

`am start -a {{android.intent.action.VIEW}} -d {{tel:123}}`

- 指定したカテゴリーとマッチしたアクティビティを実行します:

`am start -a {{android.intent.action.MAIN}} -c {{android.intent.category.HOME}}`

- インテントをURIに変換します:

`am to-uri -a {{android.intent.action.VIEW}} -d {{tel:123}}`
