import requests
import bs4


try:
    url = 'https://twitter.com/KMbappe' #url to be fetched
    data = requests.get(url)
    data_parser = bs4.BeautifulSoup(data.text, 'html.parser') #parsing the content of the web page
    follower = data_parser.body.find('a', {'data-nav':"followers"}) # extracting the followers

    if follower:
        try:
            user_name = data_parser.find('title') # extracting the title
            user_name = user_name.contents[0]
            print(user_name.split("(@")[0]+"has "+follower.attrs.get('title'))
        except:
            print(follower.attrs.get('title'))
    else:
        print("Unable to find the followers")
except Exception as e:
    print("Error has occured during execution error is "+str(e))

