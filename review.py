

#Author: Md.Fazlul Hoque
#Source: Stackoverflow and answered by the author
#Source link: https://stackoverflow.com/questions/74863250/python3-script-skips-pages-when-scraping-a-website-with-beautifulsoup/74863943#74863943


from bs4 import BeautifulSoup
import requests
import pandas as pd
headers = {'User-Agent':'Mozilla/5.0'}

data = []
for page in range(1,51):
    res = requests.get(f"https://www.glassdoor.com/Reviews/Microsoft-Reviews-E1651_P{page}.htm?filter.iso3Language=eng", headers = headers)
    #print(res)
    soup = BeautifulSoup(res.content, "html.parser")

    for review in soup.select('div.gdReview'):
       
        data.append({
            "review_title": review.select_one('h2[class="mb-xxsm mt-0 css-93svrw el6ke055"] > a').get_text(strip=True),
            "pros": review.select_one('span[data-test="pros"]').text,
            'cons': review.select_one('span[data-test="cons"]').text,
            "review_decision": review.select_one('div[class="common__EiReviewDetailsStyle__socialHelpfulcontainer pt-std"]').text

        })

df = pd.DataFrame(data).to_csv('out.csv', index=False)
#print(df)