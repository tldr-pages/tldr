# ip stats

> مدیریت و نمایش آمار واسط‌ها.
> اطلاعات بیشتر: <https://manned.org/ip-stats>.

- نمایش همهٔ آمار واسط‌ها در همهٔ دستگاه‌های شبکه:

`ip {{[st|stats]}}`

- نمایش آمار واسط شبکهٔ مشخص:

`ip {{[st|stats]}} show dev {{network_interface}}`

- نمایش آمار لایهٔ پیوند (مانند `ip -statistics link show`):

`ip {{[st|stats]}} show group link`

- نمایش آمار بارسپاری سخت‌افزاری همهٔ دستگاه‌ها:

`ip {{[st|stats]}} show group offload`

- نمایش آمار بارسپاری واسط مشخص:

`ip {{[st|stats]}} show dev {{network_interface}} group offload`

- نمایش زیرگروه مشخص بارسپاری:

`ip {{[st|stats]}} show dev {{network_interface}} group offload subgroup {{l3_stats|cpu_hit|hw_stats_info}}`

- نمایش آمار مختص خانوادهٔ آدرس (مانند MPLS):

`ip {{[st|stats]}} show group afstats subgroup {{mpls}}`

- فعال کردن جمع‌آوری آمار سخت‌افزاری لایهٔ ۳ روی دستگاه:

`ip {{[st|stats]}} set dev {{network_interface}} l3_stats on`
