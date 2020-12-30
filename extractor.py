from lxml import html


class Extractor:
    def __init__(self, config):
        self.config = config

    def __call__(self, data):
        return self.extract(data)

    def get_text(self, tree):
        return [(node.tag, node.text_content()) for node in tree.xpath('//h1|//h2|//p')]

    def extract(self, data):
        try:
            tree = html.fromstring(data)
        except Exception:
            raise
        text = self.get_text(tree)
        return text
