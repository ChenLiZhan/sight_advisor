# encoding=utf-8
import jieba
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

s = '欸鄧'
print s
seg_list = jieba.cut(s, cut_all=False)
print("Full Mode: " + "/ ".join(seg_list))