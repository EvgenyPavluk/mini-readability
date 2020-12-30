class Formatter:
    def __init__(self, config):
        self.config = config

    def __call__(self, data):
        return self.format(data)

    def format_line(self, line_type, line):
        words = line.split()
        if len(words) == 0:
            return ''
        lens = map(len, words)
        text = []
        current_length = 0
        first = 0
        row_words = 0
        for i, n in enumerate(lens):
            if current_length + (n + 1) + 1 > self.config['max_length']:
                text.append(' '.join(words[first:(first + row_words)] + ['\n']))
                first = i
                row_words = 1
                current_length = n
            else:
                current_length += n + 1
                row_words += 1
        if row_words > 0:
            text.append(' '.join(words[first:(first + row_words)] + ['\n']))
        text.append('\n' * self.config[line_type]['bottom'])

        return ''.join(text)

    def format(self, data):
        text = []
        for line in data:
            text.append(self.format_line(line[0], line[1]))
        return text
