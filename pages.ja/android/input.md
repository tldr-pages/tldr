# input

> イベントコードまたはタッチスクリーンジェスチャーをAndroidデバイスに送信します。
> このコマンドは `adb shell` 経由でのみ実行できます。
> もっと詳しく: <https://developer.android.com/reference/android/view/KeyEvent.html#constants_1>。

- Androidデバイスに1文字のイベントコードを送信します:

`input keyevent {{event_code}}`

- Androidデバイスにテキストを送信します。(`%s` はスペースを表します):

`input text "{{text}}"`

- Androidデバイスに単一のタップを送信します:

`input tap {{x_position}} {{y_position}}`

- Android デバイスにスワイプジェスチャーを送信します:

`input swipe {{x_start}} {{y_start}} {{x_end}} {{y_end}} {{duration_in_ms}}`

- Androidデバイスにホールドをスワイプジェスチャーを利用して送信します:

`input swipe {{x_position}} {{y_position}} {{x_position}} {{y_position}} {{duration_in_ms}}`
