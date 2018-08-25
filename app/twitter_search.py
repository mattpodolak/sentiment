import requests
def news_search(keyword):
    url = ('https://newsapi.org/v2/everything?'
        'q='+keyword+'&'
        'from=2018-08-20&'
        'sortBy=popularity&'
        'apiKey=a81c4da648bd4945ba2a4d15413ff608')
    response = requests.get(url)
    r = response.json()
    #print(r)
    print(r['totalResults'])
    for titles in r['articles']:
        print(titles['title'])
