# mp4decrypt

> Decrypt an MP4 file. Part of the Bento4 tools.
> More information: <https://www.bento4.com/documentation/mp4decrypt/>.

- Decrypt a file using a specific key (key ID in hex, key in hex):

`mp4decrypt --key {{key_id_hex}}:{{key_hex}} {{path/to/input_file.mp4}} {{path/to/output_file.mp4}}`

- Decrypt a file using a specific key for a track ID (track ID in decimal, key in hex):

`mp4decrypt --key {{track_id}}:{{key_hex}} {{path/to/input_file.mp4}} {{path/to/output_file.mp4}}`

- Decrypt a file using multiple keys while displaying the progress of the decryption:

`mp4decrypt --key {{key_id_1}}:{{key_1}} --key {{key_id_2}}:{{key_2}} --show-progress {{path/to/input_file.mp4}} {{path/to/output_file.mp4}}`
