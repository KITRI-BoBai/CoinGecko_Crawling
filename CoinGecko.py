from bs4 import BeautifulSoup
from mylib import *
import requests
from bs4 import BeautifulSoup


if __name__=='__main__':
    driver = make_driver()
    url = 'https://www.coingecko.com/en?page='

    rank, name, slug =[],[],[]
    for i in range(1,101):
        try:
            driver.get(url+str(i))
            driver.implicitly_wait(2)
            for j in range(1,101):
                rank.append( driver.find_element_by_xpath('/html/body/div[3]/div[4]/div[7]/div[1]/div/table/tbody/tr[{}]/td[2]'.format(j)).text )
                name.append( driver.find_element_by_xpath('/html/body/div[3]/div[4]/div[7]/div[1]/div/table/tbody/tr[{}]/td[3]/div/div[2]/a[1]'.format(j)).text )
                slug.append( driver.find_element_by_xpath('/html/body/div[3]/div[4]/div[7]/div[1]/div/table/tbody/tr[{}]/td[3]/div/div[2]/span'.format(j)).text )
            print(len(name))
            print(name)

        except Exception as e:
            print(e)
    print(rank)
    print(name)
    print(slug)
    data ={
        'rank' : rank,
        'name' : name,
        'slug' : slug
    }

    frame = pd.DataFrame(data)
    print(frame)
    frame.to_csv('CoinGecko.csv',index=False)


   