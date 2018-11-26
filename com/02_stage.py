import lib1.crawl_to_file as saver

url = 'http://www.powerballgame.co.kr/?view=dayLog'
saver.getTextAndSave(url, "powerball.html")

