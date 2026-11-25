# tc

> نمایش یا تغییر تنظیمات کنترل ترافیک.
> اطلاعات بیشتر: <https://manned.org/tc>.

- افزودن تأخیر ثابت شبکه به بسته‌های خروجی:

`sudo tc {{[q|qdisc]}} {{[a|add]}} dev {{eth0}} root netem delay {{delay_in_milliseconds}}ms`

- افزودن تأخیر شبکه با توزیع نرمال به بسته‌های خروجی:

`sudo tc {{[q|qdisc]}} {{[a|add]}} dev {{eth0}} root netem delay {{mean_delay_ms}}ms {{delay_std_ms}}ms`

- افزودن خرابی، از دست رفتن یا تکرار به بخشی از بسته‌ها:

`sudo tc {{[q|qdisc]}} {{[a|add]}} dev {{eth0}} root netem {{corruption|loss|duplication}} {{effect_percentage}}%`

- محدود کردن پهنای باند، نرخ burst و حداکثر تأخیر:

`sudo tc {{[q|qdisc]}} {{[a|add]}} dev eth0 root tbf rate {{max_bandwidth_mb}}mbit burst {{max_burst_rate_kb}}kbit latency {{max_latency_before_drop_ms}}ms`

- نمایش سیاست‌های فعال کنترل ترافیک:

`tc {{[q|qdisc]}} {{[s|show]}} dev {{eth0}}`

- حذف همهٔ قوانین کنترل ترافیک:

`sudo tc {{[q|qdisc]}} {{[d|delete]}} dev {{eth0}}`

- تغییر قانون کنترل ترافیک:

`sudo tc {{[q|qdisc]}} {{[c|change]}} dev {{eth0}} root netem {{policy}} {{policy_parameters}}`
