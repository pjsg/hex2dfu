# hex2dfu
A HEX file to DFU converter which understands sparse files. This will generate a multi-element image
so that the flasher will (may) not erase the bits of the flash that should not be affected.

## Usage

    hex2dfu --hex=<hexfile> --dfu=<dfufile> [ --pid=<pid> ] [ --vid=<vid> ]


