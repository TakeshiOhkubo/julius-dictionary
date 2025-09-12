# julius-4.5-4.6dictionary
Python3 script to add vocabulary for julius4.5 and julius4.6 (automatic speech recognition). julius4.5 can be downloaded from  https://github.com/julius-speech/dictation-kit. julius4.6 can be downloaded from https://github.com/julius-speech/julius. Find the dictionary files "bccwj.60k.htkdic" and "bccwj.60k.pdp.htkdic" in the path "model\lang_m".

julius4.5 および julius4.6 はoff-line音声認識ソフトウェアです。
julius4.5は
https://github.com/julius-speech/dictation-kit
からダウンロード出来ます。
その中から
model\lang_m
とフォルダを辿ります。
bccwj.60k.htkdic
と
bccwj.60k.pdp.htkdic
が辞書ファイルです。音声記号を手書きで書くのは苦痛なので、Windows IMEの辞書ファイル型式 (output1.txt)から単語と読みを抽出して音声記号に変換します。最後に空白行が入るので手作業で消去してください。
