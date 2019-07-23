#!/usr/bin/env python

"""hex2dfu

Usage:
    hex2dfu --hex=<hex> --dfu=<dfu> [--vid=<vid>] [--pid=<pid>]

--hex=<hex>    The source HEX file to be converted
--dfu=<dfu>    The destination DFU file to be created
--vid=<vid>    The vendor id [default: 0]
--pid=<pid>    The product id [default: 0]

"""

from intelhex import IntelHex
from docopt import docopt
import struct
import binascii


def hex_to_image(ih, segment):
    """
    Return an image object
    """
    print(segment)
    binstr = ih.tobinstr(*segment)
    return struct.pack('>LL', segment[0], segment[1] - segment[0]) + binstr


def hex_to_target(ih):
    """
    Return a target object
    """
    images = [hex_to_image(ih, segment) for segment in ih.segments()]
    image_data = ''.join(images)

    return struct.pack('>6sbb255sLL', 'Target', 0, 0, '', len(image_data), len(images)) + image_data


def hex_to_dfu(ih, vid, pid):
    """
    Convert the IntelHex object into a DFU and return it
    """

    target = hex_to_target(ih)

    prefix = struct.pack('>5sbLb', 'DfuSe', 1, 16 + 11 + len(target), 1)
    suffix = struct.pack('<HHHH3sb', 0xffff, pid, vid, 0x011a, 'UFD', 16)

    contents = prefix + target + suffix

    return contents + struct.pack('>L', binascii.crc32(contents))


def main():
    arguments = docopt(__doc__, version="hex2dfu version 0.1")

    ih = IntelHex(arguments['--hex'])

    dfu = hex_to_dfu(ih, vid=int(arguments['--vid'], 0), pid=int(arguments['--pid'], 0))

    with open(arguments['--dfu'], 'w') as f:
        f.write(dfu)


if __name__ == '__main__':
    main()