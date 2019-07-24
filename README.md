# hex2dfu

A HEX file to DFU converter which understands sparse files. This will generate a multi-element image
so that the flasher will (may) not erase the bits of the flash that should not be affected. This
generates the DfuSe form of file (i.e. version 1.1a). 

## Usage

    hex2dfu --hex=<hexfile> --dfu=<dfufile> [ --pid=<pid> ] [ --vid=<vid> ]

There are no other options. The program may display tracebacks if things do not work correctly. 

There are no options to name the image target. 

## Rationale

I needed this to generate a binary file that was compact and had a "hole" in the middle where my firmware was keeping data.
In my case, the update process is as follows:

* Copy the DFU file from the build system and save it at the end of the flash memory.
* Validate that the file is correct (i.e. the CRC32 is valid)
* Disable interrupts
* Jump to updater in RAM
* Reflash the firmware from the DFU image
* Jump to the reset vector.

## Comments, Bugs

Please submit issues on the github page: https://github.com/pjsg/hex2dfu
