#
# Example file for parsing and processing HTML
#
from html.parser import HTMLParser

metacount = 0


class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        print("Encontrei um comentario: ", data)
        pos = self.getpos()
        print("\tAt line: ", pos[0], " position ", pos[1])

    def handle_starttag(self, tag, attrs):
        global metacount
        if tag == 'meta':
            metacount += 1
        print("Encountrei uma start tag: ", tag)
        pos = self.getpos()
        print("\tAt line: ", pos[0], " position ", pos[1])

        if attrs.__len__() > 0:
            print("\tAttributes:")
            for a in attrs:
                print("\t", a[0], "=", a[1])  # atributo "name" and "value"

    def handle_endtag(self, tag):
        print("Encountrei uma end tag: ", tag)
        pos = self.getpos()
        print("\tAt line: ", pos[0], " position ", pos[1])

    def handle_data(self, data):
        if data.isspace():
            return
        print("Encountrei um dado: ", data)
        pos = self.getpos()
        print("\tAt line: ", pos[0], " position ", pos[1])


def main():
    # instantiate the parser and feed it some HTML
    parser = MyHTMLParser()
    f = open("samplehtml.html")
    if f.mode == 'r':
        conteudoarquivo = f.read()
        parser.feed(conteudoarquivo)

    print("Total de Meta tags achadas =" + str(metacount))


if __name__ == "__main__":
    main()
