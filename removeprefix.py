links = [
    "www.github.com",
    "www.youtube.com",
    "www.google.com",
    "www.wikipedia.org"
]
for link in links:
    #print(link.lstrip("www."))
    print(link.removeprefix("www."))