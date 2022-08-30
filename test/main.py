from flask import Flask
app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path): #old: 67.228.16.104
	import sys
	try:
		worst = [1,5,7,8,10,11,12,18,22,27,30,32,36,37,41,44,50,51,52,53,57,63,65,69,105,106,107,108,111,112,114,121,123,126,131,132,139,142,144,150,151,152,157,159,160,167,168,175,184,185,187,189,190,191,197,198,200,207,211,212,214,216,218,220,224,225,227,228,230,232,233,235,241,242,243,244,248,251,253,254,255,257,258,262,265,278,280,282,288,291,292,293,297,298,304,305,306,307,308,309,310,314,315,317,326,327,330,331,332,338,339,341,346,347,350,351,353,355,357,358,361,362,363,368,369,370,371,372,374,375,376,382,383,390,391,392,393,397,399,401,402,408,413,414,422,423,427,429,432,438,440,450,459,462,463,469,472,474,476,481,483,486,487,488,496,497,499,505,510,511,513,516,522,525,529,531,532,539,544,545,550,552,553,556,557,558,559,561,562,563,573,600,601,605,612,613,621,622,623,624,627,639,648,651,652,656,660,661,662,663,664,676,683,695,699,702,712,718,721,723,727,731,735,738,739,746,748,754,759,764,766,767,768,773,774,778,782,783,790,795,798,800,802,804,805,806,808,809,828,834,835,845,857,860,861,863,872,873,877,878,880,883,892,921,925,926,933,935,938]
		max_n = 938
		import re, os, random
		
		custom = {'':max_n, 'latest':max_n, 'new':max_n, 'best':301}
		
		if path in custom:
			n = custom[path]
		elif path=='random':
			n = random.randint(1,max_n)
			while n in worst:
				n = random.randint(1,max_n)
		elif re.match('[0-9]+$', path):
			n = int(path)
		elif re.match('comic.php/[0-9]+$', path):
			n = int(path[10:])
		else:
			return page_not_found(path)
		
		if n < 0  or n > max_n:
			return page_not_found(path)
		
		filetype = '.png'
		if n < 655 or n==789:
			filetype = '.gif'
		image_name = str(n) + filetype
		
		title = open(os.path.join('temp_data', 'titles.txt')).readlines()[n].strip()
		hovertext = open(os.path.join('temp_data', 'hovertext.txt')).readlines()[n].strip()
		
		previous_n = max(n-1,0)
		next_n = min(n+1,max_n)
		rand_n = random.randint(1,max_n)
		
		while previous_n in worst and previous_n-1>0:
			previous_n-=1
		while next_n in worst and next_n+1<=max_n:
			next_n+=1
		while rand_n in worst or rand_n==n:
			rand_n = random.randint(1,max_n)
		
		previous_n, next_n, rand_n = str(previous_n), str(next_n), str(rand_n)
		
		page = '''<!DOCTYPE html>
<html>

<head>
<meta charset="UTF-8">
<title>'''+title+'''</title>
<style>
a.big
{
	display:block;
	position:absolute;
	width:50%;
	height:100%;
}
</style>
</head>

<body style="color:white; background-color:black; text-align:center;">

<a href="http://comicjk.com/'''+previous_n+'''" style="top:0%; left:0%;" class="big"></a>
<a href="http://comicjk.com/'''+next_n+'''" style="top:0%; left:50%;" class="big"></a>

<div style="display:table; width:100%;">
	<div style="display:table-cell; font-size:200px; vertical-align:middle; color:yellow;">
		&lt;
	</div>
	<div style="display:table-cell;">
		<img src="http://icse.cornell.edu/~jms875/comicjk/'''+image_name+'''"  title="'''+hovertext+'''"/>
		<br /><span style="color:#777;">('''+hovertext+''')</span>
	</div>
	<div style="display:table-cell; font-size:200px; vertical-align:middle; color:yellow;">
		&gt;
	</div>
</div>

<div style="z-index:100; position:absolute; right:50%;">
	<a href="https://www.reddit.com/r/comicjk" style="color:yellow; font-size:100px; text-decoration:none;">!</a>
</div>

<div style="z-index:100; position:absolute; left:50%;">
	<a href="http://comicjk.com/'''+rand_n+'''" style="color:yellow; font-size:100px; text-decoration:none;">?</a>
</div>

</body>

</html>'''
		return page
	except:
		result = str(sys.exc_info()[0]) + '\n' + str(sys.exc_info()[1])
		result = result.replace('<', '&lt;').replace('>', '&gt;')
		return '<html><h2>Server error:</h2><pre>' + result + '</pre><h2>Tell me at theboss@comicjk.com</h2></html>'

@app.errorhandler(404)
def page_not_found(e):
	"""Return a custom 404 error."""
	return 'Sorry, nothing at this URL.', 404
