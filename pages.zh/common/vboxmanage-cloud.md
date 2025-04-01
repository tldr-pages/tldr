# vboxmanage-cloud

> 用于管理云实例和映像的 VirtualBox 命令行接口。
> 更多信息：<https://www.virtualbox.org/manual/ch08.html#vboxmanage-cloud>。

- 列出指定隔间中处于指定状态的实例：

`VBoxManage cloud --provider={{provider_name}} --profile={{profile_name}} list instances --state={{running|terminated|paused}} --compartment-id={{compartment_id}}`

- 创建新实例：

`VBoxManage cloud --provider={{provider_name}} --profile={{profile_name}} instance create --domain-name={{domain_name}} --image-id={{image_id}} | {{--options...}}`

- 获取特定实例的信息：

`VBoxManage cloud --provider={{provider_name}} --profile={{profile_name}} instance info --id={{unique_id}}`

- 终止实例：

`VBoxManage cloud --provider={{provider_name}} --profile={{profile_name}} instance terminate --id={{unique_id}}`

- 列出特定隔间和状态下的映像：

`VBoxManage cloud --provider={{provider_name}} --profile={{profile_name}} list images --compartment-id={{compartment_id}} --state={{state_name}}`

- 创建新映像：

`VBoxManage cloud --provider={{provider_name}} --profile={{profile_name}} image create --instance-id={{instance_id}} --display-name={{display_name}} --compartment-id={{compartment_id}}`

- 获取特定映像的信息：

`VBoxManage cloud --provider={{provider_name}} --profile={{profile_name}} image info --id={{unique_id}}`

- 删除映像：

`VBoxManage cloud --provider={{provider_name}} --profile={{profile_name}} image delete --id={{unique_id}}`