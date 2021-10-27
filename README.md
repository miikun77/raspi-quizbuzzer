# raspi-quizbuzzer
### Quiz buzzer system that connects buttons and lights via GPIO on Raspberry Pi
### Raspberry Piを使用したクイズの早押し判定システム
<br>
高校のクイズ愛好会で使用するために作成しました。
<br>
Daisoで購入したプッシュライトを改造し、Raspberry Pi（以下Raspi）とGPIO接続して、早押し判定をしています。
<br>
現在は1着のボタンの点灯、音声（ブザーも可）に対応しています。  
2着以降の判定、時間差表示などの機能を追加を予定しています。

始めて作ったプログラムなので、まずは実際に動いて使えることを目的としています。  
ソースコードは見づらく稚拙なものですが、ご意見等ありましたらぜひコメントしてください。
<br>
## 配線図
![配線図](https://user-images.githubusercontent.com/64695370/139097194-b6ae511f-5cca-427c-8792-9ea4e0dd86b2.png)
<br>

RaspiのGPIOは**BCM**番号です。物理ピン番号ではありません。
<br>
番号は https://pinout.xyz を参照してください。
<br>
Pin番号は変数にしているので、任意に変更できます。ソースコードを変更してください。
<br><br>

### 1.GPIOに圧電ブザーをつなぐ場合
使用するものはquizbuzzer.pyのみです。
<br>

### 2.Raspiの音声出力を用いる場合
使用するものはquizaudio.pyとbuzzer.wavです。
<br><br>

## （追記）Daisoのプッシュライトでない場合
任意のLEDとタクトスイッチがあれば作動します。
<br>
スイッチはRaspiのプルアップ抵抗を使っているので問題ありませんが、
LEDと圧電ブザーは外部抵抗を使ってください。
<br>

## 実演映像

https://youtu.be/PUfAXo7mgTU

<br>

## Reference
https://monomonotech.jp/kurage/raspberrypi/daiso_mini_touch_light.html  
参考にさせていただきました。ありがとうございます。