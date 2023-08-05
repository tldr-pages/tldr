# krunvm

> Create MicroVMs from OCI images.
> More information: <https://github.com/containers/krunvm>.

- Create MicroVM based on Fedora:

`krunvm create {{docker.io/fedora}} --cpus {{number_of_vcpus}} --mem {{memory_in_megabytes}} --name "{{name}}"`

- Start a specific image:

`krunvm start "{{image_name}}"`

- List images:

`krunvm list`

- Change a specific image:

`krunvm changevm --cpus {{number_of_vcpus}} --mem {{memory_in_megabytes}} --name "{{new_vm_name}}" "{{current_vm_name}}"`

- Delete a specific image:

`krunvm delete "{{image_name}}"`
