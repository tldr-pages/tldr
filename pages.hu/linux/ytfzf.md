# ytfzf

> Egy POSIX szkript, amely segít videók és zenék keresésében és letöltésében. További információ: <https://github.com/pystardust/ytfzf>.

- Videók keresése a YouTube-on miniatűr előnézettel:

`ytfzf --show-thumbnails {{search_pattern}}`

- Csak az első elem hangjának lejátszása egy ciklusban:

`ytfzf --audio-only --auto-select --loop {{search_pattern}}`

- Videó letöltése az előzményekből:

`ytfzf --download --choose-from-history`

- A keresés során talált összes zene lejátszása:

`ytfzf --audio-only --select-all {{search_pattern}}`

- A trendi videók megtekintése egy külső menüben:

`ytfzf --trending --ext-menu {{search_pattern}}`

- Keresés a PeerTube-on a YouTube helyett:

`ytfzf --peertube {{search_pattern}}`
