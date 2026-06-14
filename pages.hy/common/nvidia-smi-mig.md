# nvidia-smi mig

> Կառավարեք Nvidia բազմատյան GPU-ները:.
> Լրացուցիչ տեղեկություններ. <https://docs.nvidia.com/datacenter/tesla/mig-user-guide/index.html>:.

- Ստեղծեք հաշվարկային օրինակ 0 սարքից:

`nvidia-smi mig {{[-cgi|--create-gpu-instance]}} {{0}} {{[-C|--default-compute-instance]}}`

- Ցուցակել GPU-ի դեպքերը.:

`nvidia-smi mig {{[-lgi|--list-gpu-instances]}}`

- Ցուցադրել օգնությունը.:

`nvidia-smi mig {{[-h|--help]}}`
