# vboxmanage-cloud

> VirtualBox command-line interface for managing cloud instances and images.
> More information: <https://www.virtualbox.org/manual/ch08.html#vboxmanage-cloud>.

- List Instances:

`VBoxManage cloud {{provider=name}} {{profile=name}} list instances {{--state=string}} {{--compartment-id=string}}`

- Create Instance:

`VBoxManage cloud {{--provider=name}} {{--profile=name}} instance create {{--domain-name=name}} {{--image-id=id}} | {{--options...}}`

- Instance Information:

`VBoxManage cloud {{--provider=name}} {{--profile=name}} instance info {{--id=unique id}}`

- Terminate Instance:

`VBoxManage cloud {{--provider=name}} {{--profile=name}} instance terminate {{--id=unique id}}`

- List Images:

`VBoxManage cloud {{--provider=name}} {{--profile=name}} list images {{--compartment-id=string}} {{--state=string}}`

- Create Image:

`VBoxManage cloud {{--provider=name}} {{--profile=name}} image create {{--instance-id=id}} {{--display-name=name}} {{--compartment-id=id}}`

- Image Information:

`VBoxManage cloud {{--provider=name}} {{--profile=name}} image info {{--id=unique id}}`

- Delete Image:

`VBoxManage cloud {{--provider=name}} {{--profile=name}} image delete {{--id=unique id}}`
