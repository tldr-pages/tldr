# IPXNET

> Emulate IPX networking for multiplayer games (client-server model).
> More information: <https://www.dosbox.com/wiki/Connectivity>.

- Start IPX server (default UDP port 213):

`IPXNET startserver`

- Start server on specific port:

`IPXNET startserver {{19900}}`

- Connect client to server IP:

`IPXNET connect {{192.168.2.100}}`

- Connect with specific port:

`IPXNET connect {{192.168.2.100}} {{19900}}`

- Check network status:

`IPXNET status`

- Ping to test speed/clients:

`IPXNET ping`

- Disconnect client:

`IPXNET disconnect`

- Stop server (after clients disconnect):

`IPXNET stopserver`
