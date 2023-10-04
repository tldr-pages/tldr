# mkdir

> 建立目錄。
> 更多資訊：<https://www.gnu.org/software/coreutils/mkdir>.

- 在目前所在目錄或指定路徑中建立新目錄：

`mkdir {{目錄/完整/路徑}}`

- 遞迴建立目錄，若上層目錄尚未被建立則會一併建立：

`mkdir -p {{目錄/完整/路徑}}`

- 使用指定的權限建立新目錄：

`mkdir -m {{rwxrw-r--}} {{目錄/完整/路徑}}`
