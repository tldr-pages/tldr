# cmd

> Android service manager.
> More information: <https://cs.android.com/android/platform/superproject/+/main:frameworks/native/cmds/cmd/>.

- [l]ist all running services:

`cmd -l`

- Call a specific service:

`cmd {{service}}`

- Call a service with specific arguments:

`cmd {{service}} {{argument1 argument2 ...}}`
- Dump activity manager state:

`cmd activity dump`

- Force-stop an app using activity manager:

`cmd activity force-stop {{package_name}}`

- List running processes:

`cmd activity processes`

- Trigger garbage collection system-wide:

`cmd activity gc`

- Show device idle (Doze) state:

`cmd deviceidle get`

- Force device into idle mode:

`cmd deviceidle force-idle`

- Exit idle mode:

`cmd deviceidle unforce`

- Show current battery status:

`cmd battery get`

- Simulate low battery:

`cmd battery set level 10`

- Reset battery to normal behavior:

`cmd battery reset`

- List all jobs scheduled by JobScheduler:

`cmd jobscheduler get`

- Run a specific job immediately:

`cmd jobscheduler run {{package_name}} {{job_id}}`