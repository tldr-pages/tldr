# kubectl վկայագիր

> Կառավարեք վկայագրի ստորագրման հարցումները:.
> Լրացուցիչ տեղեկություններ. <https://kubernetes.io/docs/reference/kubectl/generated/kubectl_certificate/>:.

- Հաստատել վկայականի ստորագրման հարցումը անունով.:

`kubectl certificate approve {{csr_name}}`

- Մերժել վկայագրի ստորագրման հարցումը անունով.:

`kubectl certificate deny {{csr_name}}`

- Հաստատել մանիֆեստի ֆայլում սահմանված վկայագրի ստորագրման հարցումը.:

`kubectl certificate approve --filename {{path/to/csr.yaml}}`

- Մերժել մանիֆեստի ֆայլում սահմանված վկայագրի ստորագրման հարցումը.:

`kubectl certificate deny --filename {{path/to/csr.yaml}}`

- Ստիպել վերահաստատել վկայագրի ստորագրման հարցումը, որը նախկինում մերժվել է.:

`kubectl certificate approve --force {{csr_name}}`
