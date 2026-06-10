# az vm

> Կառավարեք վիրտուալ մեքենաները Azure-ում:.
> `azure-cli`-ի մի մասը (հայտնի է նաև որպես `az`):.
> Լրացուցիչ տեղեկություններ. <https://learn.microsoft.com/cli/azure/vm>:.

- Ցուցադրել առկա վիրտուալ մեքենաների աղյուսակը.:

`az vm list --output table`

- Ստեղծեք վիրտուալ մեքենա՝ օգտագործելով Ubuntu-ի լռելյայն պատկերը և ստեղծեք SSH ստեղներ.:

`az vm create {{[-g|--resource-group]}} {{rg}} {{[-n|--name]}} {{vm_name}} --image {{UbuntuLTS}} --admin-user {{azureuser}} --generate-ssh-keys`

- Դադարեցրեք վիրտուալ մեքենան.:

`az vm stop {{[-g|--resource-group]}} {{rg}} {{[-n|--name]}} {{vm_name}}`

- Վիրտուալ մեքենա հատկացնել.:

`az vm deallocate {{[-g|--resource-group]}} {{rg}} {{[-n|--name]}} {{vm_name}}`

- Սկսեք վիրտուալ մեքենա.:

`az vm start {{[-g|--resource-group]}} {{rg}} {{[-n|--name]}} {{vm_name}}`

- Վերագործարկեք վիրտուալ մեքենա.:

`az vm restart {{[-g|--resource-group]}} {{rg}} {{[-n|--name]}} {{vm_name}}`

- Թվարկեք VM պատկերները, որոնք հասանելի են Azure Marketplace-ում.:

`az vm image list`
