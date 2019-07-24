from unittest import TestCase
from intelhex import IntelHex
import hex2dfu
from cStringIO import StringIO
import binascii

class TestConvert(TestCase):
    def test_sample_1(self):
        hex = StringIO("""\
:020000021000EC
:10C20000E0A5E6F6FDFFE0AEE00FE6FCFDFFE6FD93
:10C21000FFFFF6F50EFE4B66F2FA0CFEF2F40EFE90
:10C22000F04EF05FF06CF07DCA0050C2F086F097DF
:10C23000F04AF054BCF5204830592D02E018BB03F9
:020000020000FC
:04000000FA00000200
:00000001FF
""")
        ih = IntelHex(hex)
        dfu = hex2dfu.hex_to_dfu(ih)
        self.assertEqual(binascii.hexlify(dfu), """\
44667553650100000180015461726765740000000000000000000000000000000000000000000000\
00000000000000000000000000000000000000000000000000000000000000000000000000000000\
00000000000000000000000000000000000000000000000000000000000000000000000000000000\
00000000000000000000000000000000000000000000000000000000000000000000000000000000\
00000000000000000000000000000000000000000000000000000000000000000000000000000000\
00000000000000000000000000000000000000000000000000000000000000000000000000000000\
00000000000000000000000000000000000000000000000000000000000000000000000000560000\
00020000000000000004fa000002ff0001c20000000040e0a5e6f6fdffe0aee00fe6fcfdffe6fdff\
fff6f50efe4b66f2fa0cfef2f40efef04ef05ff06cf07dca0050c2f086f097f04af054bcf5204830\
592d02e018bb03ffffff000000001a01554644102129e996\
""")