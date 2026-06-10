# kubectl autoscale

> Ստեղծեք ավտոմատ սանդղակ՝ խելացիորեն մեծացնելու պատիճների քանակը՝ հիմնվելով kubernetes կլաստերի պահանջների վրա:.
> Լրացուցիչ տեղեկություններ. <https://kubernetes.io/docs/reference/kubectl/generated/kubectl_autoscale/>:.

- Ավտոմատ մասշտաբի տեղակայումը առանց թիրախային պրոցեսորի օգտագործման նշված.:

`kubectl autoscale {{[deploy|deployment]}} {{deployment_name}} --min {{min_replicas}} --max {{max_replicas}}`

- Ավտոմատ մասշտաբի տեղակայումը թիրախային պրոցեսորի օգտագործմամբ.:

`kubectl autoscale {{[deploy|deployment]}} {{deployment_name}} --max {{max_replicas}} --cpu-percent {{target_cpu}}`
