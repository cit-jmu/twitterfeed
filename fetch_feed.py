import feedparser
import datetime 
import re


FEED = 'http://twitter.com/statuses/user_timeline/14847510.rss'
PAGE = r'D:\Inetpub\ExpressionEngineDevelopment\templates\includes\twitter_feed.php'


def format_title(title):
	htmlCodes = (
	    ('&', '&amp;'),
	    ('<', '&lt;'),
	    ('>', '&gt;'),
	    ('"', '&quot;'),
	    ("'", '&#39;'),
	)
	for char, code in htmlCodes:
		title = title.replace(char, code)

	if title.startswith('cit_jmu: '):
		title = title[9:]

	# url matching: http://daringfireball.net/2010/07/improved_regex_for_matching_urls
	links = re.compile(r"(?i)\b((?:[a-z][\w-]+:(?:/{1,3}|[a-z0-9%])|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?]))")
	title = ' '.join('<a href="%s">%s</a>' % (piece, piece) if links.match(piece) else piece for piece in title.split())	
		
	title = re.sub('@([-_a-zA-Z]+)', r'<a href="http://twitter.com/\1">@\1</a>', title)
	
	return title
	
def format_date(date):
	d = datetime.date(*date[:3])
	return d.strftime('%b&nbsp;%d')


feed = feedparser.parse(FEED)

if feed.get('items'):

	file = open(PAGE, "w")
	file.write('<ul>\n')
	
	for item in feed['items'][:3]:
		
		file.write((u'<li>%s <a href="%s" class="date">%s</a></li>\n' % (
			format_title(item["title"]),
			item["link"],
			format_date(item["date_parsed"]),
		)).encode("utf-8"))

	file.write('</ul>\n')
	file.close()




