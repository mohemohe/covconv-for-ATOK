#! /usr/bin/env python
# coding:utf-8

####################################################################
# covconv.py
# covconv for ATOK
# Copyright (c) 2014 mohemohe
#
# this code licensed under the MIT/X11 License .
# please visit ' http://opensource.org/licenses/mit-license.php '.
####################################################################

import re
import urllib
from xml.etree.ElementTree import *

# covconv for ATOKの更新確認用
__version__ = 2


def atok_plugin_run_process( request_data ):
  result_data = {} 
  candidate_array = []
  
  covconv_pack = tryCov( request_data['composition_string'] )
  
  # 変換に成功したときだけあれこれする
  # 成功しなかったら空のリストが返って、ATOKダイレクトAPI側で何とかしてくれる
  if covconv_pack['success'] == '1': 
    regex = re.compile(r'^(?:\xE3\x81[\x81-\xBF]|\xE3\x82[\x80-\x93]|\xe3\x83\xbc)+$')
    result = re.search(regex, request_data['composition_string'].encode('utf-8'))

    # ひらがなのみの場合
    if result != None:
      # 恐らく単語変換だから「っ」を自動的に付加しない方を先頭にすると扱いやすいはず
      candidate_array.append( {'hyoki' : covconv_pack['covlang_kana'].rstrip(u'っ')} )
      candidate_array.append( {'hyoki' : covconv_pack['covlang_kana']} )
    # それ以外の場合
    else:
      # 恐らく連文節変換だから「っ」を自動的に付加した方を先頭にすると扱いやすいはず
      candidate_array.append( {'hyoki' : covconv_pack['covlang_orig']} )
      candidate_array.append( {'hyoki' : covconv_pack['covlang_orig'].rstrip(u'っ')} )

  # 自身のバージョンよりもAPIから通知されるバージョンが大きい場合は変換候補に更新通知を出す
  # 確定するとブラウザで配布ページを開くはず
  if int( covconv_pack['covconv4atok_version'] ) > int( __version__ ):
    candidate_array.append( { 'hyoki'             : u"こふ語ダイレクト for ATOK の更新があります" , 
                              'alternative'       : u"http://ghippos.net/special/kovlang.php" , # あとでちゃんとページを作る
                              'alternative_type'  : u"url_jump_string" } )

  # リスト['candidate']はATOKダイレクトAPI側で強制
  result_data['candidate'] = candidate_array

  return result_data


def tryCov( ja_JP ):
  covconv_pack = {}

  # 自分でAPIサーバーを立てない限り変えないでね
  url = 'https://api.ghippos.net/covconv/atok/' 
  params = urllib.urlencode( {'ja_JP': ja_JP.encode('utf-8')} )

  try:
    # 接続するタイミングが urlopen() の時なのか read() の時なのか分からないから両方tryに入れちゃう
    xml = urllib.urlopen( url, params )
    element = fromstring( xml.read() )
  except Exception, e:
    # どうせAPIが落ちたときしかエラー吐かないからこれでいいでしょ
    # raise e
    covconv_pack['success'] = '-1'
    covconv_pack['covconv4atok_version'] = '-1'
  else:
    covconv_pack['success'] = element.findtext('.//success')
    covconv_pack['covlang_kana'] = element.findtext('.//covlang_kana')
    covconv_pack['covlang_orig'] = element.findtext('.//covlang_orig')
    covconv_pack['covconv4atok_version'] = element.findtext('.//covconv4atok_version')

  return covconv_pack
