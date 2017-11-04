import webbrowser,bs4,requests,sys,os
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
srch_key=' '.join(sys.argv[1:])
url='http://wallpapercave.com'
srch='/search?q='
os.makedirs(srch_key,exist_ok=True)
resp=requests.get(url+srch+srch_key,headers=headers)
resp.raise_for_status()
#print(urls)
#Beautiful soup object
soup=bs4.BeautifulSoup(resp.text,'html5lib')
#get the url of the first group of pics
pic_url=url+soup.select('a[class="albumthumbnail even"]')[0].get('href')

#Navigate to that page and find the link to the images
resp_p=requests.get(pic_url)
resp_p.raise_for_status()
soup_p=bs4.BeautifulSoup(resp_p.text,'html5lib')
#print(soup_p.prettify)
img_list=soup_p.select('[slug='+soup.select('a[class="albumthumbnail even"]')[0].get('href')[1:]+']')
print(img_list)
#soup_p.select('[slug="1080p-wallpaper"]')
val=0
for i in img_list:
    print(i)
    resp_img=requests.get(url+i.get('src'))
    resp_img.raise_for_status()
    fl=open(os.path.join(srch_key,str(val)+'.jpg'),'wb')
    print('Writing to {}.jpg'.format(val))
    for chunk in resp_img.iter_content(1000000):
        fl.write(chunk)
    fl.close()
    val+=1
