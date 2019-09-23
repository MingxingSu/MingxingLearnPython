from html.parser import HTMLParser

class MyHtmlParser(HTMLParser):
    def __init__(self):
        self.reset()
        self.NEWTAGS = []
        self.NEWATTRS = []
        self.HTMLData = []

    def handle_starttag(self, tag, attrs):
        self.NEWTAGS.append(tag)
        self.NEWATTRS.append(attrs)

    def handle_data(self, data):
        self.HTMLData.append(data)

    def clean(self):
        self.NEWTAGS = []
        self.NEWATTRS = []
        self.HTMLData = []

    convert_charrefs = False

