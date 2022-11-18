path: lab7/WWW/htmls/00/services/publications/
URL : http://www.lab7.kuis.kyoto-u.ac.jp/publications/

Publicationのディレクトリ
論文リストをdoc、htmlファイルの両方で管理
　※htmlファイルはWordファイルを変換により生成のこと！

英語版もhtml変換時にsjis保存されているので、文字コードを変更する必要がある。
　※ヘッダーを削除

replace.plによりquote/backquoteを全角→半角処理する必要がある
bash.txtも参考に。

論文ファイルを各年代毎にディレクトリで分割

英語ファイルが海外で読めるかどうかの確認は
falcon：/usr/local/acroread/bin/acroread
goose,dodo：acroread-en
で行う。
　※各ファイルの各ページを確認のこと！

エラーメッセージ：
　Warning: charset "STRING" not supported, using "ISO8859-1".
解決法：
　文字通り、キャラクタセット"STRING"はサポートしてないから"ISO8859-1"を使用するという意味。
　フォントには関係なくロカール(ロケール)に関係する。問題ないWarningらしい。

エラーメッセージ：
　A font contains a bad CMap /Encoding.
解決法：
　英語版のacroreadを使っている場合は、そこに日本語が混っていると思われます。
　日本語フォントの除去が必要

エラーメッセージ：
　Unable to find or create the font 'Ryumin-Light-Identity-H'. Some characters may not display or print correctly
解決法：
　リューミンライト体が使用されている。代替フォントに置換する必要がある。
　日本語フォントの除去が必要


日本語の除去方法について
1.ソースファイルから訂正
　特に、WordファイルからPDF化したものには有効
2.psファイルをエディタで直接編集
　Ryumin-Light-Identity-H　→　Times　等のフォント名と置換
3.最終手段
　Ghostscript を使い、
	gs -sDEVICE=pswrite -sOutputFile=english.ps japanese.ps


エラーメッセージ：
　Invalidad Color Space
解決法：
　再度、最新バージョンで確認する。カラースペースの定義の違い。


