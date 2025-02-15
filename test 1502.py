from main import BooksCollector
# добавляем новую книгу
def test_add_new_book_add_one():
    collector = BooksCollector()
    collector.add_new_book('Облако')
    assert len(collector.get_books_genre()) == 1

# устанавливаем книге жанр
def test_set_book_genre():
    collector = BooksCollector()
    collector.books_genre = {'Игра престолов': 'Фантастика',
                             'Еретик' : 'Ужасы',
                             'Каштановые человечки' : 'Детектив',
                             'Моана' : 'Мультфильм',
                             'Американский пирог' : 'Комедия'
                             }
    collector.set_book_genre('Моана' , 'Комедия')
    assert collector.books_genre ['Моана'] == 'Комедия'

# получаем жанр книги по её имени
def test_get_book_genre_good():
    collector = BooksCollector()
    collector.books_genre = {'Игра престолов': 'Фантастика',
                                'Еретик' : 'Ужасы',
                                'Каштановые человечки' : 'Детектив',
                                'Моана' : 'Мультфильм',
                                'Американский пирог' : 'Комедии'
                                 }
    assert collector.get_book_genre('Каштановые человечки') == collector.books_genre['Детектив']
# выводим список книг с определённым жанром
def test_get_books_with_specific_genre_valid_genre_good():
    collector = BooksCollector()
    collector.books_genre = {'Игра престолов': 'Фантастика',
                             'Еретик' : 'Ужасы',
                             'Каштановые человечки' : 'Детектив',
                             'Моана' : 'Мультфильм',
                             'Американский пирог' : 'Комедии'
                             }
    assert collector.get_books_with_specific_genre('Ужасы') == ['Еретик']


# возвращаем книги, подходящие детям
def get_books_for_children_no_added():
    collector = BooksCollector()
    collector.books_genre = {'Игра престолов': 'Фантастика',
                             'Еретик': 'Ужасы',
                             'Каштановые человечки': 'Детектив',
                             'Моана': 'Мультфильм',
                             'Американский пирог': 'Комедии'
                             }
    assert collector.get_books_for_children() == ['Моана']

# добавляем книгу в Избранное
def add_book_in_favorites_my():
    collector = BooksCollector()
    collector.books_genre = {'Каштановые человечки': 'Детектив'}
    collector.favorites = ['Каштановые человечки']
    collector.add_book_in_favorites('Каштановые человечки')
    assert collector.favorites == ['Каштановые человечки'] and len(collector.favorites) == 1

# получаем список Избранных книг
def test_get_list_of_favorites_books_true():
    collector = BooksCollector()
    collector.favorites = ['Моана', 'Игра престолов', 'Каштановые человечки']
    assert collector.get_list_of_favorites_books() == collector.favorites
# удаляем книгу из Избранного
def test_delete_book_from_favorites_valid_name_true():
    collector = BooksCollector()
    collector.favorites = ['Моана', 'Игра престолов', 'Каштановые человечки']
    collector.delete_book_from_favorites('Моана')
    assert collector.favorites == ['Игра престолов', 'Каштановые человечки']

