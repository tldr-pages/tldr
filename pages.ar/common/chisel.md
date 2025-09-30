# chisel

> إنشاء أنفاق TCP/UDP، يتم نقلها عبر HTTP، وتأمينها عبر SSH.
> يتضمن كل من العميل والخادم في نفس الملف التنفيذي `chisel`.
> لمزيد من التفاصيل: <https://github.com/jpillora/chisel>.

- تشغيل خادم Chisel:

`chisel server`

- تشغيل خادم Chisel يستمع إلى منفذ محدد:

`chisel server {{[-p|--port]}} {{server_port}}`

- تشغيل خادم Chisel يقبل الاتصالات المصادق عليها باستخدام اسم المستخدم وكلمة المرور:

`chisel server --auth {{username}}:{{password}}`

- الاتصال بخادم Chisel وإنشاء نفق لمنفذ محدد إلى خادم طرف ثالث ومنفذ:

`chisel client {{server_ip}}:{{server_port}} {{local_port}}:{{remote_server}}:{{remote_port}}`

- الاتصال بخادم Chisel وإنشاء نفق لجهاز ومنفذ محددين إلى خادم طرف ثالث ومنفذ:

`chisel client {{server_ip}}:{{server_port}} {{local_host}}:{{local_port}}:{{remote_server}}:{{remote_port}}`

- الاتصال بخادم Chisel باستخدام المصادقة باسم المستخدم وكلمة المرور:

`chisel client --auth {{username}}:{{password}} {{server_ip}}:{{server_port}} {{local_port}}:{{remote_server}}:{{remote_port}}`

- تهيئة خادم Chisel في الوضع العكسي على منفذ محدد، مع تمكين وظيفة وكيل SOCKS5 (على المنفذ 1080):

`chisel server {{[-p|--port]}} {{server_port}} --reverse --socks5`

- الاتصال بخادم Chisel على عنوان IP ومنفذ محددين، وإنشاء نفق عكسي يتم تعيينه إلى وكيل SOCKS محلي:

`chisel client {{server_ip}}:{{server_port}} R:socks`
