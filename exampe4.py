from bs4 import BeautifulSoup
from selenium import webdriver
import re


url = 'http://www.powerballgame.co.kr/?view=dayLog'
# driver = webdriver.PhantomJS('C:\\Users\\user\\Downloads\\phantomjs-2.1.1-windows\\phantomjs-2.1.1-windows\\bin\\phantomjs.exe')
driver = webdriver.PhantomJS('./pj/mac/phantomjs')
driver.get(url)
delay_time = 2
driver.implicitly_wait(delay_time)



html = driver.page_source
print(html)
soup = BeautifulSoup(html, 'html.parser')
table = soup.findall('table',{'class': 'numberText'})
realtime_round = soup.select('table.powerballBox > tbody.content > tr > td > span.numberText')

pattern = re.compile("(\d+)")
mat = pattern.search(realtime_round)

for round in realtime_round:
    print(round.text)

f = open('C:\ 새파일.txt' ,'w' , encoding="utf-8" )
f.write(round.text)
f.close()

realtime_result = soup.select('table.powerballBox > tbody.content > tr > td > div.sp-ball_bg')

for result in  realtime_result:
      print(result.text)


driver.get(url)
data=driver.find_element_by_xpath("//*[@id='powerballLogBox']/tbody[2]/tr[4]/td[3]/div")

for ii in data:
        print(ii.get_attritbute("href"))

