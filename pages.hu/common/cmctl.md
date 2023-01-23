# cmctl

> Egy CLI eszköz, amely segít a cert-manager erőforrások kezelésében a fürtön belül. Ellenőrizze a tanúsítványok aláírásának állapotát, hagyja jóvá/tagadja le a kérelmeket, és adjon ki új tanúsítványkérelmeket. További információ: <https://cert-manager.io/docs/usage/cmctl/>.

- Ellenőrizze, hogy a cert-manager API készen áll-e:

`cmctl check api`

- Ellenőrizze egy tanúsítvány állapotát:

`cmctl status certificate {{cert_name}}`

- Új tanúsítványkérelem létrehozása egy meglévő tanúsítvány alapján:

`cmctl create certificaterequest my-cr --from-certificate-file {{cert.yaml}}`

- Új tanúsítványkérelem létrehozása, az aláírt tanúsítvány lekérése és maximális várakozási idő beállítása:

`cmctl create certificaterequest my-cr --from-certificate-file {{cert.yaml}} --fetch-certificate --timeout {{20m}}`
