# systemd-run

> Run programs in transient units.
> More information: <https://manned.org/systemd-run>.

- Start a transient service:

`sudo systemd-run {{command}} {{[args...]}}`

- Start a transient service under the service manager of the current user (no privileges):

`systemd-run --user {{command}} {{[args...]}}`

- Start a transient service with a custom unit name and description:

`sudo systemd-run --unit={{name}} --description={{desc}} {{command}} {{[args...]}}`

- Start a transient service that does not get cleaned up after it terminates with a custom environment variable:

`sudo systemd-run --remain-after-exit --set-env={{name}}={{val}} {{command}} {{[args...]}}`

- Start a transient timer that periodically runs its transient service (see `man systemd.time` for calendar event format):

`sudo systemd-run --on-calendar={{calendar event}} {{command}} {{[args...]}}`
