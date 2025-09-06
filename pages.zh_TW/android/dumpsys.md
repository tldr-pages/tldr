# dumpsys

> 提供關於 Android 系統服務的資訊。
> 此命令只能透過 `adb shell` 使用。
> 更多資訊：<https://developer.android.com/tools/dumpsys>.

- 獲取所有系統服務的診斷輸出：

`dumpsys`

- 獲取指定系統服務的診斷輸出：

`dumpsys {{服務}}`

- 列出 `dumpsys` 可以提供的所有服務資訊：

`dumpsys -l`

- 列出服務的指定服務引數：

`dumpsys {{服務}} -h`

- 從診斷輸出中排除指定服務：

`dumpsys --skip {{服務}}`

- 指定超時時間，以秒為單位（預設為 10 秒）：

`dumpsys -t {{秒數}}`
