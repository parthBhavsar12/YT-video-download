import webbrowser
url = input('Enter the URL to be downloaded : ')
url = 'ss' + url[:12] + url[12:]
#print(url)
webbrowser.open(url)
