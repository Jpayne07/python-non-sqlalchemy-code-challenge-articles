class Article:
    all = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self)
    
    @property
    def title(self):
        return self._title  # Return the private attribute

    @title.setter
    def title(self, value):
        # Validate the title before setting the private attribute
        if isinstance(value, str) and 5 <= len(value) <= 50:
            self._title = value  # Set the private attribute
        else:
            raise ValueError("Title must be a string between 5 and 50 characters.")
    
   


        
class Author:
    def __init__(self, name):
        if(isinstance(name, str) and len(name) > 0):
            self._name = name
        else:
            raise Exception("Name must be an instance of a string and must be longer than 0 characters.")
        
    @property
    def name(self):
        return self._name

    def articles(self):
        articles =  []
        for article in Article.all:
            if article.author == self:
                articles.append(article)
        return articles
    
    def magazines(self):
        magazines = []
        for magazine in Magazine.all:
            if self in magazine.contributors():
                magazines.append(magazine)
        return magazines

    def add_article(self, magazine, title):
        new_article = Article(self, magazine, title)
        return new_article

    def topic_areas(self):
        list_of_categories = []
        for magazine in Magazine.all:
            if self in magazine.contributors():
                list_of_categories.append(magazine.category)
        if list_of_categories == []:
            return None
        else:
            return list(set(list_of_categories))
    
    

class Magazine:
    all = []
    def __init__(self, name, category):
        self.name = name
        self.category = category
        Magazine.all.append(self)

    @property
    def name(self):
        return self._name
        
    @name.setter
    def name(self, value):
        # Validate the title before setting the private attribute
        if isinstance(value, str) and 2 <= len(value) <= 16:
            self._name = value  # Set the private attribute
        else:
            raise ValueError("magazine category is of type str and can change")

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._category = value  # Set the private attribute
        else:
            raise ValueError("Title must be a string greater than 0 characters.")


    def articles(self):
        magazines_articles = []
        for article in Article.all:
            if article.magazine == self:
                magazines_articles.append(article)
        return magazines_articles


    def contributors(self):
        magazine_authors = []
        for article in Article.all:
            if article.magazine == self:
                magazine_authors.append(article.author)
        return list(set(magazine_authors))

    def article_titles(self):
        article_titles_list = []
        if(self.articles() == []):
            return None
        else:
            for article in self.articles():
                article_titles_list.append(article.title)
        return article_titles_list

    def contributing_authors(self):
        author_count = {}
        authors_whom_meet_criteria = []
        for article in self.articles():
            if article.author in author_count:
                author_count[article.author] +=1
            else:
                author_count[article.author] = 1
            
        for key, value in author_count.items():
            if value >=3:        
                authors_whom_meet_criteria.append(key)
            if authors_whom_meet_criteria == []:
                return None
            return authors_whom_meet_criteria


