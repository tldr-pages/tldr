# ts

> Add timestamps to input lines.
> More information: <https://joeyh.name/code/moreutils/>.

- Add current timestamp to beginning of each line:

`{{some_command}} | ts`

- Add timestamps with microsecond precision:

`{{some_command}} | ts "%b %d %H:%M:%.S"`

- Add [i]ncremental timestamps, and show microseconds:

`{{some_command}} | ts -i "%H:%M:%.S"`

- Convert existing timestamps in log file into [r]elative format:

`cat /var/log/syslog | ts -r`
