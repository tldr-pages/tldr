# nvidia-smi mig

> Nvidia multi-instance GPU를 관리.
> 더 많은 정보: <https://docs.nvidia.com/datacenter/tesla/mig-user-guide/index.html>.

- GPU 0에서 compute instance 생성:

`nvidia-smi mig {{[-cgi|--create-gpu-instance]}} {{0}} {{[-C|--default-compute-instance]}}`

- GPU 인스턴스 목록 표시:

`nvidia-smi mig {{[-lgi|--list-gpu-instances]}}`

- 도움말 표시:

`nvidia-smi mig {{[-h|--help]}}`
