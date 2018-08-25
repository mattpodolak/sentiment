import requests
def news_search(keyword):
    url = ('https://newsapi.org/v2/everything?'
        'q='+keyword+'&'
        'from=2018-08-20&'
        'to=2018-08-21&'
        'language=en&'
        'sortBy=popularity&'
        'apiKey=a81c4da648bd4945ba2a4d15413ff608')
    response = requests.get(url)
    r = response.json()
    for titles in r['articles']:
        print(titles['title'])
    print('TOTAL ENTRIES:', r['totalResults'])
    print(keyword)