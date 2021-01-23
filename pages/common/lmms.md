# lmms

> Free, open source, multiplatform digital audio workstation.
> Render a `.mmp` or `.mmpz` project file, dump a `.mmpz` as XML, or start the GUI.
> More information: <https://lmms.io>.

- Start the GUI:

`lmms`

- Start the GUI and load external config:

`lmms --config {{path/to/config.xml}}`

- Start the GUI and import MIDI or Hydrogen file:

`lmms --import {{path/to/midi/or/hydrogen/file}}`

- Start the GUI with a specified window size:

`lmms --geometry {{x_size}}x{{y_size}}+{{x_offset}}+{{y_offset}}`

- Dump a `.mmpz` file:

`lmms dump {{path/to/mmpz/file.mmpz}}`

- Render a project file:

`lmms render {{path/to/mmpz_or_mmp/file}}`

- Render the individual tracks of a project file:

`lmms rendertracks {{path/to/mmpz_or_mmp/file}} {{path/to/dump/directory}}`

- Render with custom samplerate, format, and as a loop:

`lmms render --samplerate {{88200}} --format {{ogg}} --loop --output {{path/to/output/file.ogg}}`
