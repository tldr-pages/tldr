# crackle

> Crack and decrypt Bluetooth Low Energy (BLE) encryption.
> More information: <https://github.com/mikeryan/crackle>.

- Check whether the recorded BLE communications contain the packets necessary for recovering temporary keys (TKs):

`crackle -i {{path/to/input.pcap}}`

- Use brute force to recover the TK of the recorded pairing events and use it to decrypt all subsequent communications:

`crackle -i {{path/to/input.pcap}} -o {{path/to/decrypted.pcap}}`

- Use the specified long-term key (LTK) to decrypt the recorded communication:

`crackle -i {{path/to/input.pcap}} -o {{path/to/decrypted.pcap}} -l {{81b06facd90fe7a6e9bbd9cee59736a7}}`
