# nvidia-smi mig

> Manage multi-instance GPUs.
> More information: <https://docs.nvidia.com/datacenter/tesla/mig-user-guide/index.html>.

- Create a compute instance from device 0:

`nvidia-smi mig {{[-cgi|--create-gpu-instance]}} {{0}} {{[-C|--default-compute-instance]}}`

- List GPU instances:

`nvidia-smi mig {{[-lgi|--list-gpu-instances]}}`
