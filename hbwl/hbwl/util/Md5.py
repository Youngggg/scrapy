# -*- coding: utf-8 -*-

import hashlib


class Md5(object):

    def get_md5_value(self, src):
        myMd5 = hashlib.md5()
        myMd5.update(src)
        myMd5_Digest = myMd5.hexdigest()

        return myMd5_Digest
