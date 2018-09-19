# 概要
Theanoで実装された[skip-thoughtモデル](https://github.com/ryankiros/skip-thoughts)を日本語文に適用。

# 環境
Python2
他ライブラリ多数（MeCab等）

# 構成
Sent2vec : ryankiros氏のskip-thoughtモデルを日本語に対応させたもの。  
skip-thought : 実行ファイル(Similarity_a_file.py)と自作関数ファイル(funcs_treatData.py)  

# 使用方法
実行ファイルSimilarity_a_fileに辞書作成・訓練・テストが記述されている。  
実行の際は必要に応じてコメントアウトする。

## 実行例
`$ THEANO_FLAGS=mode=FAST_RUN,device=cpu,floatX=float32 python Similarity_a_file.py`

## 注意
`embed_map = word2vec.load('ja.bin')`  
※学習済みword2vecモデルを[リンク](https://github.com/Kyubyong/wordvectors)等から別途ダウンロードする必要がある。  

# 参考
[skip-thoughtモデル](https://github.com/ryankiros/skip-thoughts)  
[日本語学習済みword2vecモデル](https://github.com/Kyubyong/wordvectors)  
[Skip-thoughtを用いたテキストの数値ベクトル化 - Platinum Data Blog](http://blog.brainpad.co.jp/entry/2017/06/12/160000#f-0191a609)  
