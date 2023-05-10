#!/usr/bin/env python3
#Shane Birrenkott, SBirrenkott@MadisonCollege.edu

import requests, bs4

res = requests.get('https://notpurple.com')
res.raise_for_status()

res2 = bs4.BeautifulSoup(res.text, "html.parser")

links = res2.select('a')

title = res2.title
ln1 = links[0]
ln2 = links[1]

print(f"{title.text}\n{ln1.text}\n{ln2.text}")