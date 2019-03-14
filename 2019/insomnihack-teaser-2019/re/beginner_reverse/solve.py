#!/usr/bin/env python
# coding=utf-8

from struct import unpack

int_list = unpack('32I', '\x0E\x01\x00\x00\x12\x01\x00\x00f\x01\x00\x00\xC6\x01\x00\x00\xCE\x01\x00\x00\xEA\x00\x00\x00\xFE\x01\x00\x00\xE2\x01\x00\x00V\x01\x00\x00\xAE\x01\x00\x00V\x01\x00\x00\xE2\x01\x00\x00\xE6\x00\x00\x00\xAE\x01\x00\x00\xEE\x00\x00\x00V\x01\x00\x00\x8A\x01\x00\x00\xFA\x00\x00\x00\xE2\x01\x00\x00\xBA\x01\x00\x00\xA6\x01\x00\x00\xEA\x00\x00\x00\xE2\x01\x00\x00\xE6\x00\x00\x00V\x01\x00\x00\xE2\x01\x00\x00\xE6\x00\x00\x00\xF2\x01\x00\x00\xE6\x00\x00\x00\xE2\x01\x00\x00\xE6\x01\x00\x00\xE6\x00\x00\x00') + (0x1e2, 0x1de)
res = bytearray([(i>>2)^10 for i in int_list])
print res
