# tc

> Show / manipulate traffic control settings.
> More information: <https://man7.org/linux/man-pages/man8/tc.8.html>.

- Add constant network delay to outbound packages:

`tc qdisc add dev eth0 root netem delay {{delay_in_milliseconds}}ms`

- Add normal distributed network delay to outbound packages:

`tc qdisc add dev eth0 root netem delay {{mean_delay_ms}}ms {{delay_std_ms}}ms`

- Add package loss to a portion of packages:

`tc qdisc add dev eth0 root netem loss {{effect_percentage}}%`

- Add package corruption to a portion of packages:

`tc qdisc add dev eth0 root netem corruption {{effect_percentage}}%`

- Add package duplication to a portion of packages:

`tc qdisc add dev eth0 root netem duplicate {{effect_percentage}}%`

- Limit bandwith, burst rate and max latency:

`tc qdisc add dev eth0 root tbf rate {{max_bandwith_mb}}mbit burst {{max_burst_rate_kb}}kbit latency {{max_latency_before_drop_ms}}ms`

- Show active traffic control policies:

`tc qdisc show dev eth0`

- Delete all trafic control rules:

`tc qdisc del dev eth0`

- Change traffic control rule:

`tc qdisc change dev eth0 root netem {{policy}} {{policy_parameters}}`
