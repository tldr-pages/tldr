# ytfzf

> یافتن و بارگیری ویدئو و موسیقی. نوشته‌شده با پوستهٔ POSIX.
> همچنین : `youtube-dl`, `yt-dlp`, `instaloader`.
> اطلاعات بیشتر: <https://manned.org/ytfzf>.

- جست‌وجوی ویدئو در YouTube با پیش‌نمایش بندانگشتی:

`ytfzf {{[-t|--show-thumbnails]}} {{search_pattern}}`

- پخش حلقه‌ای فقط صدای نخستین مورد:

`ytfzf {{[-m|--audio-only]}} {{[-a|--auto-select]}} {{[-l|--loop]}} {{search_pattern}}`

- بارگیری ویدئو از تاریخچه:

`ytfzf {{[-d|--download]}} --choose-from-history`

- پخش همهٔ موسیقی‌های یافت‌شده در جست‌وجو:

`ytfzf {{[-m|--audio-only]}} {{[-A|--select-all]}} {{search_pattern}}`

- مشاهدهٔ ویدئوهای پرطرفدار در منوی خارجی:

`ytfzf --trending --ext-menu {{search_pattern}}`

- جست‌وجو در PeerTube به‌جای YouTube:

`ytfzf --peertube {{search_pattern}}`
