from gc import get_objects
from django.urls import path
from .views import ( 
    CreateBook, List_all_books,
    CreateBookstore, 
    List_all_stores, 
    List_all_owners,
    CreateBook,
    SearchBookByTitle,
    SearchBookByISBN,
    SearchBookByAuthor,
    SearchBookByPublication,
    SearchBookstoreByName,
    SearchBookstoreByTown,
    SearchBookstoreCatalog,
    ImportFromEthnikiVivliothiki,
    ImportFromPoliteia,
    ImportExcelFileEthnikiViVliothiki,
    ImportExcelFilePoliteia
)
from .models import *
from .serializers import *

urlpatterns = [
    path('books/all/', List_all_books.as_view(queryset=Book.objects.all(), serializer_class=BookSerializer) , name='list-all-books'),
    path('stores/all/', List_all_stores.as_view(queryset=Shop.objects.all(), serializer_class=ShopSerializer) , name='list-all-stores'),
    path('owners/all/',List_all_owners.as_view(queryset=User.objects.all(), serializer_class=UserSerializer), name="list-all-owners"),
    
    path('create-bookstore/', CreateBookstore.as_view(), name="create-bookstore"),
    path('create-book/', CreateBook.as_view(), name="create-book"),

    path('search/book/title/<slug:slug>/',SearchBookByTitle.as_view(),name='search-book-title'),
    path('search/book/isbn/<slug:slug>/',SearchBookByISBN.as_view(),name='search-book-isbn'),
    path('search/book/author/<slug:slug>/',SearchBookByAuthor.as_view(),name='search-book-author'),
    path('search/book/publication/<slug:slug>/',SearchBookByPublication.as_view(),name='search-book-publication'),

    path('search/bookstore/name/<slug:slug>/',SearchBookstoreByName.as_view(),name='search-bookstore-name'),
    path('search/bookstore/town/<slug:slug>/',SearchBookstoreByTown.as_view(),name='search-bookstore-town'),
    path('search/bookstore/name/<slug:slug>/catalog/',SearchBookstoreCatalog.as_view(),name='search-bookstore-catalog'),

    path('import/file/nlg/', ImportExcelFileEthnikiViVliothiki, name='import-excel-file-ethniki-vivliothiki'),
    path('import/isbn/nlg/', ImportFromEthnikiVivliothiki, name="import-from-ethniki-vivliothiki"),
    path('import/isbn/politeia/', ImportFromPoliteia, name="import-from-politeia"),
]