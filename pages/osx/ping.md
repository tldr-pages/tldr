# ping

> Send ICMP ECHO_REQUEST packets to network hosts.
> More information: <https://keith.github.io/xcode-man-pages/ping.8.html>.

- Ping the specified host:

`ping "{{hostname}}"`

- Ping a host a specific number of times:

`ping -c {{count}} "{{host}}"`

- Ping `host`, specifying the interval in `seconds` between requests (default is 1 second):

`ping -i {{seconds}} "{{host}}"`

- Ping `host` without trying to lookup symbolic names for addresses:

`ping -n "{{host}}"`

- Ping `host` and ring the bell when a packet is received (if your terminal supports it):

`ping -a "{{host}}"`

- Ping `host` and prints the time a packet was received (this option is an Apple addition):

`ping --apple-time "{{host}}"`
