Usage: man [OPTION...] [章节] 手册页...

  -C, --config-file=文件   使用该用户设置文件
  -d, --debug                输出调试信息
  -D, --default              将所有选项都重置为默认值
      --warnings[=警告]    开启 groff 的警告

 主要运行模式：
  -f, --whatis               等同于 whatis
  -k, --apropos              等同于 apropos
  -K, --global-apropos       search for text in all pages
  -l, --local-file
                             把“手册页”参数当成本地文件名来解读
  -w, --where, --path, --location
                             输出手册页的物理位置
  -W, --where-cat, --location-cat
                             输出 cat 文件的物理位置

  -c, --catman               由 catman 使用，用来对过时的 cat
                             页重新排版
  -R, --recode=编码        output source page encoded in ENCODING

 寻找手册页：
  -L, --locale=区域
                             定义本次手册页搜索所采用的区域设置
  -m, --systems=系统       use manual pages from other systems
  -M, --manpath=路径       设置搜索手册页的路径为“路径”

  -S, -s, --sections=列表  使用以半角冒号分隔的章节列表

  -e, --extension=扩展
                             将搜索限制在扩展类型为“扩展”的手册页之内

  -i, --ignore-case          查找手册页时不区分大小写字母
                             (默认)
  -I, --match-case           查找手册页时区分大小写字母。

      --regex                show all pages matching regex
      --wildcard             show all pages matching wildcard

      --names-only           make --regex and --wildcard match page names only,
                             not descriptions

  -a, --all                  寻找所有匹配的手册页
  -u, --update               强制进行缓存一致性的检查

      --no-subpages          don't try subpages, e.g. 'man foo bar' => 'man
                             foo-bar'

 控制格式化的输出：
  -P, --pager=PAGER          使用 PAGER 程序显示输出文本
  -r, --prompt=字符串     给 less pager 提供一个提示行

  -7, --ascii                显示某些 latin1 字符的 ASCII 翻译形式
  -E, --encoding=编码      use selected output encoding
      --no-hyphenation, --nh turn off hyphenation
      --no-justification,                              --nj   turn off justification
  -p, --preprocessor=字符串   字符串表示要运行哪些预处理器：
                             e - [n]eqn, p - pic, t - tbl,
g - grap, r - refer, v - vgrind

  -t, --troff                使用 groff 对手册页排版
  -T, --troff-device[=设备]   使用 groff 的指定设备

  -H, --html[=浏览器]     使用 elinks 或指定浏览器显示 HTML
                             输出
  -X, --gxditview[=分辨率]   使用 groff 并通过 gxditview (X11)
                             来显示：
                             -X = -TX75, -X100 = -TX100, -X100-12 = -TX100-12
  -Z, --ditroff              使用 groff 并强制它生成 ditroff

  -?, --help                 give this help list
      --usage                give a short usage message
  -V, --version              print program version
长选项的强制或可选参数也是强制或可选的
对于任何相应的短期期权。
向cjwatson@debian.org报告错误。
