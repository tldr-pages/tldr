# du

> 硬碟使用量：估算每個檔案以及目錄所佔用的硬碟容量。
> 更多資訊：<https://www.gnu.org/software/coreutils/manual/html_node/du-invocation.html>.

- 以給定單位（B/KiB/MiB）列出目錄和所有子目錄的大小：

`du -{{b|k|m}} {{目錄路徑}}`

- 以人類可讀形式（自動選擇單位）列出目錄和所有子目錄的大小：

`du {{[-h|--human-readable]}} {{目錄路徑}}`

- 以人類可讀形式（自動選擇單位）列出單一目錄大小：

`du {{[-sh|--summarize --human-readable]}} {{目錄路徑}}`

- 以人類可讀形式（自動選擇單位）列出目錄以及底下所有檔案大小：

`du {{[-ah|--all --human-readable]}} {{目錄路徑}}`

- 以人類可讀形式列出目錄和任何子目錄的大小，最多 N 層：

`du {{[-h|--human-readable]}} {{[-d|--max-depth]}} N {{目錄路徑}}`

- 以人類可讀形式列出目前目錄子目錄中所有 `.jpg` 檔案的大小，並在最後顯示累積總數：

`du {{[-ch|--total --human-readable]}} {{*/*.jpg}}`
