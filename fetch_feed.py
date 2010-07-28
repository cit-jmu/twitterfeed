import feedparser


FEED = 'http://twitter.com/statuses/user_timeline/14847510.rss'
PAGE = r'D:\Inetpub\ExpressionEngineDevelopment\templates\includes\twitter_feed.php'


feed = feedparser.parse(FEED)

if feed.get('items'):

	file = open(PAGE, "w")
	file.write('<ul>\n')
	
	for item in feed['items'][:3]:
		
		file.write((u'<li>%s <span class="time"><a href="%s">%s</a></span></li>\n' % (
			item["title"],
			item["link"],
			item["date"],
		)).encode("utf-8"))

	file.write('</ul>\n')
	file.close()



# url matching: http://daringfireball.net/2010/07/improved_regex_for_matching_urls

