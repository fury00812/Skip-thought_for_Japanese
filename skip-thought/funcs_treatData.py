# -*- coding: utf-8 -*-
'''
テキストデータを加工する関数群
'''
import MeCab


'''
テキストファイルから1行ずつ取り出しlines[]に格納
'''
def getLinesFromTxt(path):
    lines = []

    f = open(path,'r')
    lines = f.read().split('\n')
    f.close()
    return lines

'''
文章を分かち書きしtoken_list[]に格納
'''
def getTokenlistFromline(text,hinshi):
    token_list = []
    m = MeCab.Tagger('-Ochasen') #茶筅ご関係式で出力
    m.parse(text) #parseToNodeを使うために必要
    node = m.parseToNode(text) #形態素1個1個をいじるため

    while node: #形態素の先頭からたどる
        feats = node.feature.split(',') #featureをカンマで区切ってリスト化。feats[0]に品詞情報。
        if feats[0] in hinshi:
            token_list.append(node.surface)
        node = node.next #次の形態素へ
    return token_list

'''
分かち書き1文を返す
'''
def getWakatiSentFromline(text):
    m = MeCab.Tagger('-Owakati')
    wakati_sent = m.parse(text)
    return wakati_sent.strip()
