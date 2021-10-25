# raspi-quizbuzzer
Quiz buzzer system that connects buttons and lights via GPIO on Raspberry Pi

Raspberry Piを使用したクイズの早押し判定システム


Seriaで購入したプッシュライトを改造し、Raspberry Pi（以下Raspi）とGPIO接続して、早押し判定をしています。
現在は1着のボタンの点灯、音声（ブザーも可）に対応しています。

2着以降の判定、時間差表示などの機能を追加を予定しています。

始めて作ったプログラムなので、まずは実際に動いて使えることを目的としています。
ソースコードは見づらく稚拙なものですが、ご意見等ありましたらぜひコメントしてください。

音声出力の際に、
GPIOに圧電ブザーをつなぐ場合はquizbuzzer.py
Raspiの音声出力を用いる場合はquizaudio.pyとbuzzer.wavを使用してください。