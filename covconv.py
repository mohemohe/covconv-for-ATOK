#! /usr/bin/env python
# coding:utf-8

# covconv.py
# こふ語ダイレクト for ATOK
# Copyright (c) 2014 mohemohe
#
# this code licensed under MIT/X11 License.
# please visit ' http://opensource.org/licenses/mit-license.php '.
__version__ = 1

import re
import urllib
from xml.etree.ElementTree import *

def atok_plugin_run_process( request_data ):
  result_data = {}
  candidate_array = []

  regex = re.compile(r'^(?:\xE3\x81[\x81-\xBF]|\xE3\x82[\x80-\x93])+$')
  result = regex.search( request_data['composition_string'] )
  if result != None :
    # TODO: 直接変換 
  else :
    # TODO: 複数の候補

  target_string = request_data['composition_string']

  covconv_pack = tryCov( request_data['composition_string'].encode('utf-8') )

  if covconv_pack['success'].decode('utf-8') == '1':
    candidate_array.append( {'hyoki' : covconv_pack['covlang_kana'].rstrip('っ').decode('utf-8')} )
    candidate_array.append( {'hyoki' : covconv_pack['covlang_kana'].decode('utf-8')} )
    candidate_array.append( {'hyoki' : covconv_pack['covlang_orig'].rstrip('っ').decode('utf-8')} )
    candidate_array.append( {'hyoki' : covconv_pack['covlang_orig'].decode('utf-8')} )

  if int(covconv_pack['covconv4atok_version'].decode('utf-8')) > int(__version__):
    candidate_array.append( { 'hyoki'             : u"こふ語ダイレクト for ATOK の更新があります" , 
                              'alternative'       : u"http://ghippos.net/special/kovlang.php" , # あとでちゃんとページを作る
                              'alternative_type'  : u"url_jump_string" } )

  result_data['candidate'] = candidate_array

  return result_data

def tryCov( ja_JP ):
  covconv_pack = {}

  url = 'https://api.ghippos.net/covconv/atok/'
  params = urllib.urlencode( {'ja_JP': ja_JP} )
  xml = urllib.urlopen( url, params )

  element = fromstring( xml.read() )

  covconv_pack['success'] = element.findtext('.//success')
  covconv_pack['covlang_kana'] = element.findtext('.//covlang_kana').encode('utf-8')
  covconv_pack['covlang_orig'] = element.findtext('.//covlang_orig').encode('utf-8')
  covconv_pack['covconv4atok_version'] = element.findtext('.//covconv4atok_version').encode('utf-8')

  return covconv_pack
