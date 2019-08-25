from bs4 import BeautifulSoup

html = '''<a href="argument_transcripts/2016/16-399_3f14.pdf" 
id="ctl00_ctl00_MainEditable_mainContent_rptTranscript_ctl01_hypFile" 
target="_blank">16-399. </a>'''

soup = BeautifulSoup(html, features="html.parser")

for a in soup.find_all('a', href=True):
    url = a['href'].split('/')
    print (url[-1])