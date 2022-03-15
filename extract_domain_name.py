"""
Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. For example:

domain_name("http://github.com/carbonfive/raygun") == "github"
domain_name("http://www.zombie-bites.com") == "zombie-bites"
domain_name("https://www.cnet.com") == "cnet"

test.assert_equals(domain_name("http://google.com"), "google")
test.assert_equals(domain_name("http://google.co.jp"), "google")
test.assert_equals(domain_name("www.xakep.ru"), "xakep")
test.assert_equals(domain_name("https://youtube.com"), "youtube")


"""


def domain_name(url):
    url_split = ""
    found = ""
    for i in range(0, len(url)):
        if url[i] == "p":
            url_split = url.split("/")
            if url_split[0] == "http:" or url_split[0] == "https:":
                found = url_split[2].split('.')
                if len(found) == 2:
                    found = found[0]
                elif len(found) == 3:
                    found = found[1]
                else:
                    found = found[0]
            elif url_split[0] == "www":
                found = url_split[2].split('.')
                found = found[2]
        else:
            url_split = url.split(".")
            found = url_split[1]
    print(found)





domain = "http://github.com/carbonfive/raygun"
cnet = "https://www.cnet.com"
xakep = "www.xakep.ru"
youtube = "https://youtube.com"
zombie = "http://www.zombie-bites.com"
google = "http://google.co.jp"
google_2 = "http://google.com"
domain_name(google)