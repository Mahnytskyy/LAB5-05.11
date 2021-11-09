class Library:
    def __init__(self):
        self.bookshelf = []
    def home_add(self, data):
        data = data.split()
        self.bookshelf.append(data)
    def search_author(self,author):
        for data in self.bookshelf:
            if ' '.join(data[:2]) == author:
                return' '.join(data)
    def search_genre(self,genre):
        for data in self.bookshelf:
            if data[3].split(':')[1].strip() == genre:
                return ' '.join(data)

if __name__ == '__main__':
    data = '''Анджей Сапковський "Відьмак" жанр: фентезі
              Борис Акунін "Азазель" жанр: детектив
              Стівен Кінг "Темна вежа" жанр: фантастика'''

home = Library()
for line in data.split('\n'):
    home.home_add(line)

    print(home.search_author('Анджей Сапковський'))
        