# reg.py

> Query, add, delete, save or backup registry keys/values on a remote Windows machine over SMB/RPC.
> Part of the Impacket suite.
> More information: <https://github.com/fortra/impacket>.

- Query subkeys and values under a registry path:

`reg.py {{domain}}/{{username}}:{{password}}@{{target}} query -keyName {{HKLM\\SOFTWARE\\Microsoft\\Windows}}`

- Query all subkeys and values under a registry path recursively:

`reg.py {{domain}}/{{username}}:{{password}}@{{target}} query -keyName {{HKLM\\SOFTWARE\\Microsoft\\Windows}} -s`

- Add a new registry key or value (default value type is `REG_SZ`):

`reg.py {{domain}}/{{username}}:{{password}}@{{target}} add -keyName {{HKLM\\SOFTWARE\\Example}} -v {{value_name}} -vt {{REG_SZ|REG_NONE|REG_EXPAND_SZ|REG_BINARY|REG_DWORD|REG_DWORD_BIG_ENDIAN|REG_LINK|REG_MULTI_SZ|REG_QWORD}} -vd {{value_data}}`

- Delete a registry key or value:

`reg.py {{domain}}/{{username}}:{{password}}@{{target}} delete -keyName {{HKLM\\SOFTWARE\\Example}} -v {{value_name}}`

- Save a registry key (and subkeys) to a file on the target via UNC path:

`reg.py {{domain}}/{{username}}:{{password}}@{{target}} save -keyName {{HKLM\\SOFTWARE\\Example}} -o \\\\{{target}}\\{{share}}\\{{output_file.reg}}`

- Backup SAM, SYSTEM and SECURITY hives to a file on a target via UNC path (requires SYSTEM privileges):

`reg.py {{domain}}/{{username}}:{{password}}@{{target}} backup -o \\\\{{target}}\\{{share}}`
