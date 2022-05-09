#Complete the function/method so that it returns the url with anything after the anchor (#) removed.

Examples
"www.codewars.com#about" --> "www.codewars.com"
"www.codewars.com?page=1" -->"www.codewars.com?page=1"


def remove_url_anchor(url):
  no_anchor = None
  for i in range(0, len(url)):
    if url[i] == '#':
      no_anchor = url[0:i]
    if '#' not in url:
      no_anchor = url
  return no_anchor