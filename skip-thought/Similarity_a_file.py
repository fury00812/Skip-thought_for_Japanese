# -*- coding: utf-8 -*-

import sys
import funcs_treatData as tdata
sys.path.append('..')
from sent2vec.training import train, vocab, tools
import gensim
from gensim.models.word2vec import Word2Vec as word2vec
import numpy as np

#cos類似度計算器
def cos_sim(v1, v2):
    return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))

sentList = [] #分かち書きした文のリスト

#①前準備：辞書作成のためのsentList[]作成---------------------------------------------
lines = tdata.getLinesFromTxt('声を出さないと、決めました!!_edit') #作品の行リスト
print '文の数 ： '+str(len(lines))
for line in lines:
    sent = tdata.getWakatiSentFromline(line)
    sentList.append(sent)
#①-----------------------------------------------------------------------------

#②辞書(dictironary.pkl)作成フェーズ------------------------------------------------
worddict, _ = vocab.build_dictionary(sentList)
vocab.save_dictionary(worddict, _, loc='dictionary.pkl')
#②---------------------------------------------


#③学習フェーズ--------------------------------------------------------------------
train.trainer(sentList, dictionary='dictionary.pkl', saveto='model.npz', dim_word=300, dim=1200, max_epochs=1)
#③-----------------------------------------------------------------------------

#④実行テスト----------------------------------------------------------------------
tools.path_to_dictionary = 'dictionary.pkl'
tools.path_to_model = 'model.npz'

embed_map = word2vec.load('ja.bin')
#embed_map = gensim.models.KeyedVectors.load('ja.bin')

model = tools.load_model(embed_map=embed_map)
vector = tools.encode(model, [u'こんにちは、今日もいい天気ですね。'], verbose=False)
vector2 = tools.encode(model, [u'こんにちは、明日もいい気分ですか???'], verbose=False)
vector3 = tools.encode(model, [u'あああー暑い、嫌な気分、宿題明日やろう'], verbose=False)

#print(vector)
#print(vector.reshape(-1,))
print(cos_sim(vector.reshape(-1,),vector2.reshape(-1,)))
print(cos_sim(vector.reshape(-1,),vector3.reshape(-1,)))
print(cos_sim(vector2.reshape(-1,),vector3.reshape(-1,)))
#④-----------------------------------------------------------------------------
