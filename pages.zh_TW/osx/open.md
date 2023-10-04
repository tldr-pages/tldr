# open

> 開啟檔案、目錄或應用程式.
> 更多資訊: <https://ss64.com/osx/open.html>.

- 使用預設的應用程式開啟檔案:

`open {{檔案.副檔名}}`

- 使用指定應用程式打開檔案:

`open -a {{Application}} {{檔案.副檔名}}`

- 基於 [b]undle 標識符運行圖形 macOS 應用程式（有關獲取此標識符的簡單方法，請參閱“osascript”）:

`open -b {{com.domain.application}}`

- Open the current directory in Finder:

`open .`

- [R]eveal a file in Finder:

`open -R {{path/to/file}}`

- Open all the files of a given extension in the current directory with the associated application:

`open {{*.ext}}`

- Open a [n]ew instance of an application specified via [b]undle identifier:

`open -n -b {{com.domain.application}}`
