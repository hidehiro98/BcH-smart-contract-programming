# イーサリアム(Ethereum)入門 スマートコントラクトプログラミング
## このプロジェクトについて
このプロジェクトは斉藤賢爾さんの[イーサリアム(Ethereum)入門](https://speakerdeck.com/ks91/introduction-to-ethereum-1)で使われたプロジェクト元に自分で改良なども追加しているものです。

## 使い方
* gethをインストール
* solidityをインストール
* populusをインストール

* プロジェクトをコンパイル
`populus compile`

* テスト
`py.test .`

* populus.json を更新し、genesis.json を生成
`python init.py`

* イーサリアムのジェネシスブロックを作る
`geth init genesis.json`

* イーサリアムのアカウントを生成し、作成されたアカウントの16進数文字列をコピー
`geth account new`

* run.py を編集
  * --etherbaseの隣に、さっき作成したアカウントを 0x から始まる文字列で置きます

* ローカルチェーンを実行。止めたいときは、process id を指定して kill
`python run.py`

* 別のターミナルウィンドウで実行状況をモニタリング
`tail -f geth.log`

* “deploy.py” を編集します
  * __main__ で Greeter オブジェクトを生成しているところで、アカウントを 0xから始まる文字列で指定し、パスフレーズも指定します

* デプロイ & テストを実行
`python deploy.py`



## ハマったところメモ
