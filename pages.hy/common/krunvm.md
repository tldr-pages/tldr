# krunvm

> Ստեղծեք MicroVM-ներ OCI պատկերներից:.
> Լրացուցիչ տեղեկություններ. <https://github.com/containers/krunvm/blob/main/docs/krunvm.1.txt>:.

- Ստեղծեք MicroVM Fedora-ի հիման վրա.:

`krunvm create {{docker.io/fedora}} --cpus {{number_of_vcpus}} --mem {{memory_in_megabytes}} --name "{{name}}"`

- Սկսեք կոնկրետ պատկեր.:

`krunvm start "{{image_name}}"`

- Ցուցակ նկարներ:

`krunvm list`

- Փոխել կոնկրետ պատկեր.:

`krunvm changevm --cpus {{number_of_vcpus}} --mem {{memory_in_megabytes}} --name "{{new_vm_name}}" "{{current_vm_name}}"`

- Ջնջել կոնկրետ պատկեր.:

`krunvm delete "{{image_name}}"`
