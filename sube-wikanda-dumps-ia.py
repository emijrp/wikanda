#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (C) 2016 emijrp <emijrp@gmail.com>
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import datetime
import os
import sys

def main():
    locapedias = [
        ['almeriapedia', 'wiki-almeriapediawikandaes_w'], 
        ['cadizpedia', 'wiki-cadizpediawikandaes_w'], 
        ['cordobapedia', 'wiki-cordobapediawikandaes_w'], 
        ['granadapedia', 'wiki-granadapediawikandaes_w'], 
        ['huelvapedia', 'wiki-huelvapediawikandaes_w'], 
        ['jaenpedia', 'wiki-jaenpediawikandaes_w'], 
        ['malagapedia', 'wiki-malagapediawikandaes_w'], 
        ['sevillapedia', 'wiki-sevillapediawikandaes_w'], 
        ['wikanda', 'wiki-wikandaes_w'], 
    ]
    d = datetime.datetime.now().strftime('%Y%m%d')
    for locapedia, iaitem in locapedias:
        os.system('curl https://dumps.wikanda.es/%s/xml/%s-%s.xml.7z | ia upload %s - --remote-name=%swikandaes_w-%s-history.xml.7z ' % (locapedia, locapedia, d, iaitem, locapedia, d))

if __name__ == '__main__':
    main()

