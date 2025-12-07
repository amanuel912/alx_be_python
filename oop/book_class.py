class Book():
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    def _str(self):
        return"{self.title} by {self.author}, published in {self.year}"
    def __repr__(self):
        return"Book(title='{self.title}', author='{self.author}', year={self.year})"
    def __del__(self):
        print(f"Deleting : {self.title}")