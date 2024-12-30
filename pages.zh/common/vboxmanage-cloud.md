# vboxmanage-cloud

> 用于管理云实例和镜像的 VirtualBox 命令行接口。
> 更多信息：<https://www.virtualbox.org/manual/ch08.html#vboxmanage-cloud>。

- 列出属于指定区间的指定状态的实例：

`VBoxManage cloud --provider={{provider_name}} --profile={{profile_name}} list instances --state={{running|terminated|paused}} --compartment-id={{compartment_id}}`

- 创建一个新实例：

`VBoxManage cloud --provider={{provider_name}} --profile={{profile_name}} instance create --domain-name={{domain_name}} --image-id={{image_id}} | {{--options...}}`

- 收集有关特定实例的信息：

`VBoxManage cloud --provider={{provider_name}} --profile={{profile_name}} instance info --id={{unique_id}}`

- 终止一个实例：

`VBoxManage cloud --provider={{provider_name}} --profile={{profile_name}} instance terminate --id={{unique_id}}`

- 列出特定区间和状态内的镜像：

`VBoxManage cloud --provider={{provider_name}} --profile={{profile_name}} list images --compartment-id={{compartment_id}} --state={{state_name}}`

- 创建一个新镜像：

`VBoxManage cloud --provider={{provider_name}} --profile={{profile_name}} image create --instance-id={{instance_id}} --display-name={{display_name}} --compartment-id={{compartment_id}}`

- 检索有关特定镜像的信息：

`VBoxManage cloud --provider={{provider_name}} --profile={{profile_name}} image info --id={{unique_id}}`

- 删除一个镜像：

`VBoxManage cloud --provider={{provider_name}} --profile={{profile_name}} image delete --id={{unique_id}}`