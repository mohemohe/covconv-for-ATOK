covconv-for-ATOK
================

### これは何？

[ATOKダイレクトAPI][1] を利用して、入力した日本語をこふ語に変換します。  
ネットワーク接続のない環境では利用できません。ご了承ください。  
また、こふ語ダイレクトを呼び出すたびに、変換中の文節の文字列を  [こふ語コンバーターAPI][2] に送信します。  
covconvAPIサーバーでは接続日時などのサーバー運営に必要な最低限の情報しか記録していませんが、念のため個人情報をこふ語ダイレクトで変換するのは避けてください。

### 動作環境

- Windows もしくは Mac OS X
- ATOK 2008 以上
- Python 2.5.2 以上
- そこそこ速いネットワーク

開発環境は Windows8.1, ATOK 2014, Python 2.7.6 です。  
ATOKダイレクトAPI の仕様上、 Python 3.x では動作しません。

### 使い方

Windows かつ ATOK 2014 を使用している方は .\Windows\SETUP.EXE を使用してインストールしてください。  
それ以外のバージョンや、 OS X を使用している方は、 [http://www.atok.com/useful/developer/api/][3] より、該当するバージョンに対応したモジュールをダウンロードし、 解凍後の atok_direct_setuptool 内のファイルを .\Windows\に上書きしてからインストールしてください。

インストール後、すぐに使用可能な状態になっています。  
文字入力後、確定する前に ATOKダイレクトを起動（Ctrl + Insert） し、候補ありの表示が出てから ATOKダイレクト候補呼び出しキー（Ctrl + 0）で変換候補を表示します。

### ライセンス

covconv.py は [MIT/X11 License][4] の範囲でご利用ください。  
その他の ATOKダイレクトAPI 関連のファイルの権利は （株）ジャストシステム が保有しています。

### 謝辞

日々、こふ語の単語を提供して頂いている [@kenkov][5] 氏に感謝します。


  [1]: http://www.atok.com/useful/developer/api/
  [2]: https://api.ghippos.net/covconv/atok/
  [3]: http://www.atok.com/useful/developer/api/
  [4]: http://opensource.org/licenses/MIT
  [5]: https://twitter.com/kenkov
  [6]: http://api.ghippos.net/covconv/
