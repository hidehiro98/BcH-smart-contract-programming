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

## 現状
```
KeyError: "Unknown chain: 'bch' - Must be one of ['mainnet', 'ropsten', 'temp', 'tester', 'testrpc']"
```
が出てしまい、チェーンの名前をtestrpc, testerなどにしても下記のエラーが出て動かず

```
Traceback (most recent call last):
  File "deploy.py", line 42, in <module>
    a = Greeter('0x857b97371202791b18d415179c0fbfe16d28802d', 'password')
  File "deploy.py", line 20, in __init__
    args=[]
  File "/Users/hidehiro/.pyenv/versions/anaconda3-5.0.0/lib/python3.6/site-packages/web3/contract.py", line 311, in deploy
    txn_hash = cls.web3.eth.sendTransaction(deploy_transaction)
  File "/Users/hidehiro/.pyenv/versions/anaconda3-5.0.0/lib/python3.6/site-packages/web3/eth.py", line 216, in sendTransaction
    get_buffered_gas_estimate(self.web3, transaction),
  File "/Users/hidehiro/.pyenv/versions/anaconda3-5.0.0/lib/python3.6/site-packages/web3/utils/transactions.py", line 28, in get_buffered_gas_estimate
    gas_estimate = web3.eth.estimateGas(gas_estimate_transaction)
  File "/Users/hidehiro/.pyenv/versions/anaconda3-5.0.0/lib/python3.6/site-packages/web3/eth.py", line 263, in estimateGas
    [transaction],
  File "/Users/hidehiro/.pyenv/versions/anaconda3-5.0.0/lib/python3.6/site-packages/web3/manager.py", line 93, in request_blocking
    response = self._make_request(method, params)
  File "/Users/hidehiro/.pyenv/versions/anaconda3-5.0.0/lib/python3.6/site-packages/web3/manager.py", line 76, in _make_request
    return request_func(method, params)
  File "/Users/hidehiro/.pyenv/versions/anaconda3-5.0.0/lib/python3.6/site-packages/web3/middleware/attrdict.py", line 20, in middleware
    response = make_request(method, params)
  File "/Users/hidehiro/.pyenv/versions/anaconda3-5.0.0/lib/python3.6/site-packages/web3/middleware/formatting.py", line 23, in middleware
    response = make_request(method, formatted_params)
  File "/Users/hidehiro/.pyenv/versions/anaconda3-5.0.0/lib/python3.6/site-packages/web3/middleware/formatting.py", line 25, in middleware
    response = make_request(method, params)
  File "/Users/hidehiro/.pyenv/versions/anaconda3-5.0.0/lib/python3.6/site-packages/web3/middleware/exception_handling.py", line 20, in middleware
    return make_request(method, params)
  File "/Users/hidehiro/.pyenv/versions/anaconda3-5.0.0/lib/python3.6/site-packages/web3/providers/tester.py", line 89, in middleware
    return make_request(method, params)
  File "/Users/hidehiro/.pyenv/versions/anaconda3-5.0.0/lib/python3.6/site-packages/web3/providers/tester.py", line 119, in make_request
    response = rpc_fn(*params)
  File "/Users/hidehiro/.pyenv/versions/anaconda3-5.0.0/lib/python3.6/site-packages/testrpc/rpc.py", line 138, in eth_estimateGas
    return self.client.estimate_gas(**formatted_transaction)
  File "/Users/hidehiro/.pyenv/versions/anaconda3-5.0.0/lib/python3.6/site-packages/testrpc/client/client.py", line 253, in estimate_gas
    txn_hash = self.send_transaction(*args, **kwargs)
  File "/Users/hidehiro/.pyenv/versions/anaconda3-5.0.0/lib/python3.6/site-packages/testrpc/client/client.py", line 263, in send_transaction
    self._send_transaction(*args, **kwargs)
  File "/Users/hidehiro/.pyenv/versions/anaconda3-5.0.0/lib/python3.6/site-packages/testrpc/client/client.py", line 58, in inner
    return client_method(self, *args, **kwargs)
  File "/Users/hidehiro/.pyenv/versions/anaconda3-5.0.0/lib/python3.6/site-packages/testrpc/client/utils.py", line 104, in inner
    return fn(*bytes_args, **bytes_kwargs)
  File "/Users/hidehiro/.pyenv/versions/anaconda3-5.0.0/lib/python3.6/site-packages/testrpc/client/client.py", line 199, in _send_transaction
    sender = t.keys[t.accounts.index(_from)]
ValueError: b'\x85{\x977\x12\x02y\x1b\x18\xd4\x15\x17\x9c\x0f\xbf\xe1m(\x80-' is not in list
```

## ハマったところメモ
