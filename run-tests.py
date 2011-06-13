#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import StringIO
import protobuf

class TestVarintValue(unittest.TestCase):

    def setUp(self):
        self.mappings = (
            (0, '\x00'),
            (3, '\x03'),
            (270, '\x8E\x02'),
            (86942, '\x9E\xA7\x05')
        )
        
    def test_dump(self):
        for k, v in self.mappings:
            s = StringIO.StringIO()
            value = protobuf.VarintValue(k)
            value.dump(s)
            self.assertEqual(s.getvalue(), v)
    
    def test_load(self):
        for k, v in self.mappings:
            s = StringIO.StringIO(v)
            value = protobuf.VarintValue()
            value.load(s)
            self.assertEqual(value.get_value(), k)

class TestMessageValue(unittest.TestCase):
        
    def test_dump(self):
        message_type = protobuf.MessageType(('a', protobuf.VarintType))
        message_value = message_type()
        message_value['a'] = 150
        fp = StringIO.StringIO()
        message_value.dump(fp)
        self.assertEqual(fp.getvalue(), '\x08\x96\x01')

if __name__ == '__main__':
    unittest.main()

