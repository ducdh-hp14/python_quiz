from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    cur_level = 0
    tag_dict = {}

    def handle_starttag(self, tag, attrs):
        if MyHTMLParser.cur_level in MyHTMLParser.tag_dict:
            MyHTMLParser.tag_dict[MyHTMLParser.cur_level] += [tag]
        else:
            MyHTMLParser.tag_dict[MyHTMLParser.cur_level] = [tag]
        MyHTMLParser.cur_level += 1

    def handle_endtag(self, tag):
        MyHTMLParser.cur_level -= 1


def pageComplexity(document):
    parser = MyHTMLParser()
    parser.feed(document)
    res = parser.tag_dict[max(parser.tag_dict.keys())]
    return sorted(set(res))


document = "\"<!DOCTYPE html><html>  <body>    <h1>The best heading ever</h1>    <!--Actually it isnt, but if you can use it if you want >_< -->    <p>The worst paragraph ever.</p>  </body></html>\""
print(pageComplexity(document))
