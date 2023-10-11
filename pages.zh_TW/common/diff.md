# diff

> 比較兩個檔案或目錄間的差異。
> 更多資訊：<https://man7.org/linux/man-pages/man1/diff.1.html>.

- 比較兩檔案，列出 `舊檔案` 相異於 `新檔案` 而需更改之處，以讓兩者相同：

`diff {{舊檔案}} {{新檔案}}`

- 忽略空格下，比較兩檔案：

`diff --ignore-all-space {{舊檔案}} {{新檔案}}`

- 比較兩檔案，並排顯示差異：

`diff --side-by-side {{舊檔案}} {{新檔案}}`

- 比較兩檔案，並以統一格式 (unified format) 顯示差異（為 `git diff` 預設格式）：

`diff --unified {{舊檔案}} {{新檔案}}`

- 遞迴比較兩目錄，顯示相異的檔名或目錄名，與檔案內更動：

`diff --recursive {{舊目錄}} {{新目錄}}`

- 比較兩目錄，只顯示相異檔案的檔名：

`diff --recursive --brief {{舊目錄}} {{新目錄}}`

- 由兩個文字檔之間差異建立一個補丁 (patch) 檔給 Git，不存在的檔案視為空白文件：

`diff --text --unified --new-file {{舊檔案}} {{新檔案}} > {{diff.patch}}`
