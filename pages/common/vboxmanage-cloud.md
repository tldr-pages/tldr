# vboxmanage-cloud

> VirtualBox command-line interface for managing cloud instances and images.
> More information: <https://www.virtualbox.org/manual/ch08.html#vboxmanage-cloud>.

- List the instances in the specified state belonging to the specified compartment:

`VBoxManage cloud --provider={{provider_name}} --profile={{profile_name}} list instances --state={{running|terminated|paused}} --compartment-id={{compartment_id}`

- Create Instance:

`VBoxManage cloud --provider={{provider_name}} --profile={{profile_name}} instance create --domain-name={{domain_name}} --image-id={{image_id}} | {{--options...}}`

- Instance Information:

`VBoxManage cloud --provider={{provider_name}} --profile={{profile_name}} instance info --id={{unique_id}}`

- Terminate Instance:

`VBoxManage cloud --provider={{provider_name}} --profile={{profile_name}} instance terminate --id={{unique_id}}`

- List Images:

`VBoxManage cloud --provider={{provider_name}} --profile={{profile_name}} list images --compartment-id={{compartment_id}} --state={{state_name}}`

- Create Image:

`VBoxManage cloud --provider={{provider_name}} --profile={{profile_name}} image create --instance-id={{instance_id}} --display-name={{display_name}} --compartment-id={{compartmet_id}}`

- Image Information:

`VBoxManage cloud --provider={{provider_name}} --profile={{profile_name}} image info --id={{unique_id}}`

- Delete Image:

`VBoxManage cloud --provider={{provider_name}} --profile={{profile_name}} image delete --id={{unique_id}}`
