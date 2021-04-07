import os
import urllib
# 数据下载代码
# 只下载前五个数据集
with open('raw_data_urls.txt') as data_urls:
  for line, url in enumerate(data_urls):
    if line == 5:
      break