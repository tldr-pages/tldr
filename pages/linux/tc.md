# tc

> Show / manipulate traffic control settings.
> More information: <https://manned.org/tc>.

- Add constant network delay to outbound packages:

`tc qdisc add dev {{eth0}} root netem delay {{delay_in_milliseconds}}ms`

- Add normal distributed network delay to outbound packages:

`tc qdisc add dev {{eth0}} root netem delay {{mean_delay_ms}}ms {{delay_std_ms}}ms`

- Add package corruption/loss/duplication to a portion of packages:

`tc qdisc add dev {{eth0}} root netem {{corruption|loss|duplication}} {{effect_percentage}}%`

- Limit bandwidth, burst rate and max latency:

`tc qdisc add dev eth0 root tbf rate {{max_bandwidth_mb}}mbit burst {{max_burst_rate_kb}}kbit latency {{max_latency_before_drop_ms}}ms`

- Show active traffic control policies:

`tc qdisc show dev {{eth0}}`

- Delete all traffic control rules:

`tc qdisc del dev {{eth0}}`

- Change traffic control rule:

`tc qdisc change dev {{eth0}} root netem {{policy}} {{policy_parameters}}`
