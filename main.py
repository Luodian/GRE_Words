from urllib.request import urlretrieve

url = "http://download.dogwood.com.cn/online/grecylj"

# http://download.dogwood.com.cn/online/grecylj/WordList01.mp3

for i in range(1,58):
    print ("It's requesting {}th file".format(i))
    url_i = "{}/WordList{:0>2d}.mp3".format(url, i)
    print(url_i)
    urlretrieve(url_i, "WordList{}.mp3".format(i))