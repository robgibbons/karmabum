#!/usr/bin/env python

from xml.dom import minidom
import webbrowser
import urllib2
import time

# Scrape interval
interval = 30

# Feed endpoints
feeds = [
	['http://feeds.arstechnica.com/arstechnica/index?format=xml', ''],
	['http://wired.com/feed', ''],
	['http://feeds.feedburner.com/TechCrunch', ''],
	['http://pando.com/feed', ''],
	['http://feeds.gawker.com/gizmodo/full', ''],
	['http://www.engadget.com/rss.xml', ''],
	['http://www.cnet.com/rss/all/', ''],
	['http://www.digitaltrends.com/feed/', ''],
	['https://gigaom.com/feed/', ''],
	['http://thenextweb.com/feed/', ''],
	['http://feeds.webservice.techradar.com/us/rss', ''],
	['http://valleywag.gawker.com/rss', ''],
	['http://online.wsj.com/xml/rss/3_7455.xml', ''],
	['http://phys.org/rss-feed/breaking/', ''],
	['http://feeds.macrumors.com/MacRumors-All?format=xml', ''],
	['https://www.eff.org/rss/updates.xml', ''],
	['http://www.newyorker.com/feed/tech', ''],
	['http://feeds.washingtonpost.com/rss/blogs/rss_the-switch', ''],
	['http://feeds.bbci.co.uk/news/technology/rss.xml', ''],
	['http://feeds.venturebeat.com/VentureBeat', ''],
	['http://www.popsci.com/rss.xml', ''],
	['http://motherboard.vice.com/rss?trk_source=motherboard', ''],
]

# Scrape feeds & post new articles to HN
while True:
	for feed in feeds:
		try:
			rss = minidom.parseString(urllib2.urlopen(feed[0]).read())
			items = rss.getElementsByTagName('item')
			latest = items[0]
			title = latest.getElementsByTagName('title')[0].childNodes[0].data
			href = urllib2.urlopen(urllib2.Request(latest.getElementsByTagName('link')[0].childNodes[0].data)).geturl().split('#', 1)[0].split('?', 1)[0]
			if feed[1] != href:
				feed[1] = href
				print('Posting ' + href)
				post_url = 'http://news.ycombinator.com/submitlink?u=' + href.encode('utf8') + '&t=' + title.encode('utf8')
				webbrowser.open(post_url)
				time.sleep(3)
		except urllib2.URLError, e:
			print('ERROR on: ' + feed[0])
			print(e)
	time.sleep(interval)
