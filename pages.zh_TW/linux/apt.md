# apt

> 以 Debian 為基底的發行版的套件管理器。
> 旨在作為用於互動式使用的 `apt-get` 使用者友善的替代方案。
> 對於其他套件管理器同等的指令，請參見 <https://wiki.archlinux.org/title/Pacman/Rosetta>.
> 更多資訊：<https://manned.org/apt.8>.

- 更新套件可用版本列表（推薦在執行其他 `apt` 指令前先執行）：

`sudo apt update`

- 搜尋套件的名稱或描述：

`apt search {{package}}`

- 只搜尋套件的名稱（支援萬用字元 `*`）：

`apt list {{package}}`

- 顯示詳細的套件資訊：

`apt show {{package}}`

- 安裝或是更新套件到最新版本：

`sudo apt install {{package}}`

- 移除套件（使用 `purge` 會一併移除設定檔）：

`sudo apt remove {{package}}`

- 升級所有安裝的套件到最新的版本：

`sudo apt upgrade`

- 列出所有安裝的套件：

`apt list {{[-i|--installed]}}`
