# vboxmanage-cloud

> VirtualBox command-line interface for managing cloud instances and images.
> More information: <https://www.virtualbox.org/manual/ch08.html#vboxmanage-cloud>.

- List the instances in the specified state belonging to the specified compartment:

`VBoxManage cloud --provider={{provider_name}} --profile={{profile_name}} list instances --state={{running|terminated|paused}} --compartment-id={{compartment_id}`

- To create a new instance, employ the command:

`VBoxManage cloud --provider={{provider_name}} --profile={{profile_name}} instance create --domain-name={{domain_name}} --image-id={{image_id}} | {{--options...}}`

- To gather information about a particular instance, use:

`VBoxManage cloud --provider={{provider_name}} --profile={{profile_name}} instance info --id={{unique_id}}`

- To terminate an instance, execute:

`VBoxManage cloud --provider={{provider_name}} --profile={{profile_name}} instance terminate --id={{unique_id}}`

- To list images within a specific compartment and state, utilize:

`VBoxManage cloud --provider={{provider_name}} --profile={{profile_name}} list images --compartment-id={{compartment_id}} --state={{state_name}}`

- To create a new image involves the command:

`VBoxManage cloud --provider={{provider_name}} --profile={{profile_name}} image create --instance-id={{instance_id}} --display-name={{display_name}} --compartment-id={{compartmet_id}}`

- To retrieve information about a particular image:

`VBoxManage cloud --provider={{provider_name}} --profile={{profile_name}} image info --id={{unique_id}}`

- To delete an image, use:

`VBoxManage cloud --provider={{provider_name}} --profile={{profile_name}} image delete --id={{unique_id}}`
