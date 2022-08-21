from django.shortcuts import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView
from .models import Book, Shop, User
from .serializers import BookSerializer, ShopSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .tasks import IsbnNlg
from celery.result import ResultBase

class List_all_owners(ListAPIView):
    
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def list(self, request):
        
        queryset = self.get_queryset()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

class List_all_books(ListAPIView):
    
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
    def list(self, request):
        
        queryset = self.get_queryset()
        serializer = BookSerializer(queryset, many=True)
        
        
        dictionary_of_dictionaries = {}
        for x in range(0,len(serializer.data)):
            items = list(serializer.data[x].items())
            dict = {}
            for y in items:
                if y[0] == 'id':
                    dict['id'] = f"{y[1]}"
                if y[0] == 'title':
                    dict['title'] = f"{y[1].replace('_',' ')}"
                if y[0] == 'author':
                    dict['author'] = f"{y[1].replace('_',' ')}"
                if y[0] == 'isbn':
                    dict['isbn'] = f"{y[1]}"
                if y[0] == 'publication':
                    dict['publication'] = f"{y[1].replace('_',' ')}"
                if y[0] == 'pages':
                    dict['pages'] = f"{y[1]}"
                if y[0] == 'shop':
                    dict['shop'] = f"{y[1]}"
                
            dictionary_of_dictionaries[f'{x}'] = dict
                    

        return Response(dictionary_of_dictionaries)
    

class List_all_stores(ListAPIView):
    
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
    

    def list(self, request):
        
        queryset = self.get_queryset()
        serializer = ShopSerializer(queryset, many=True)
        
        
        dictionary_of_dictionaries = {}
        for x in range(0,len(serializer.data)):
            items = list(serializer.data[x].items())

            for y in items:
                dict = {}
                if y[0] == 'bookstore_name':
                    dict['bookstore_name'] = f"{y[1].replace('_',' ')}"
                    
                if y[0] == 'address':
                    dict['address'] = f"{y[1]}"
                    
                if y[0] == 'town':
                    dict['town'] = f"{y[1].replace('_',' ')}"
                    
                if y[0] == 'owner':
                    dict['owner'] = f"{y[1]}"
                
                
            dictionary_of_dictionaries[f'{x}'] = dict
                
        return Response(dictionary_of_dictionaries)

class CreateBook(CreateAPIView):

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    
    def post(self, request, *args, **kwargs):
        
        post = request.data.copy()
        
        post["title"] = post["title"].replace(' ','_')
        post["author"] = post["author"].replace(' ','_')
        post["publication"] = post["publication"].replace(' ','_')
        
        _mutable = request.data._mutable
        request.data._mutable = True
        
        request.data["title"] = post["title"]
        request.data["author"] = post["author"]
        request.data["publication"] = post["publication"]
        
        request.data._mutable = _mutable
        
        return super().post(request,*args,**kwargs)

class CreateBookstore(CreateAPIView):
    
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
    permission_classes = [IsAuthenticated]
    
    
    def post(self, request, *args, **kwargs):
        
        post = request.data.copy()
        
        post["bookstore_name"] = post["bookstore_name"].replace(' ','_')
        post["town"] = post["town"].replace(' ','_')
        
        
        _mutable = request.data._mutable
        request.data._mutable = True
        
        request.data["bookstore_name"] = post["bookstore_name"]
        request.data["town"] = post["town"]

        request.data._mutable = _mutable
        
        return super().post(request,*args,**kwargs)

    

class SearchBookByTitle(RetrieveAPIView):
    
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get(self, request, *args, **kwargs):
        slug = self.kwargs.get('slug')
        book = Book.objects.filter(title__icontains=slug)
        serializer = BookSerializer(book,many=True)
        return Response(serializer.data)

class SearchBookByISBN(RetrieveAPIView):
    
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get(self, request, *args, **kwargs):
        slug = self.kwargs.get('slug')
        book = Book.objects.get(isbn=slug)
        serializer = BookSerializer(book,many=True)
        return Response(serializer.data)

class SearchBookByAuthor(RetrieveAPIView):
    
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get(self, request, *args, **kwargs):
        slug = self.kwargs['slug']
        book = Book.objects.filter(author__icontains=slug)
        serializer = BookSerializer(book,many=True)
        return Response(serializer.data)

class SearchBookByPublication(RetrieveAPIView):
    
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get(self, request, *args, **kwargs):
        slug = self.kwargs.get('slug')
        book = Book.objects.filter(publication__icontains=slug)
        serializer = BookSerializer(book,many=True)
        return Response(serializer.data)

class SearchBookstoreByName(RetrieveAPIView):
    
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer

    def get(self, request, *args, **kwargs):
        slug = self.kwargs.get('slug')
        shop = Shop.objects.filter(bookstore_name__icontains=slug)
        serializer = ShopSerializer(shop,many=True)
        return Response(serializer.data)

class SearchBookstoreByTown(RetrieveAPIView):
    
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer

    def get(self, request, *args, **kwargs):
        slug = self.kwargs.get('slug')
        shop = Shop.objects.filter(slug_town=slug)
        serializer = ShopSerializer(shop,many=True)
        return Response(serializer.data)

class SearchBookstoreCatalog(RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get(self, request, *args, **kwargs):
        slug = self.kwargs.get('slug')
        shop = get_object_or_404(Shop, bookstore_name=slug.replace(" ","_"))
        catalog = Book.objects.filter(shop__bookstore_name=shop.bookstore_name)
        serializer = BookSerializer(catalog,many=True)
        return Response(serializer.data)

@api_view(['GET'])
def ImportFromEthnikiVivliothiki(request):
    isbn = '9786185642112'
    print('before sending')
    info = IsbnNlg.delay(isbn)
    print('after receiving')
    collected = info.collect()
    #for x in collected:
    #    print(x)
    #[v for v in info.collect() if not isinstance(v, (ResultBase, tuple))]
    
    #book = Book.objects.create(title=collected['title'])

    #serializer = BookSerializer(book,many=True)
    return HttpResponse("<h1>Hello</h1>")

@api_view(['GET'])
def IsbnPoliteia(request):
    isbn = '9786185642112'
    print('before sending')
    info = IsbnPoliteia.delay(isbn)
    print('after receiving')
    collected = info.collect()
    
    return HttpResponse("<h1>Hello</h1>")

@api_view(['GET'])
def ImportExcelFileEthnikiViVliothiki(request):
    # TODO Set up Celery, Redis and Selenium
    # TODO Set up Pandas
    # TODO Export isbns from excel
    # TODO Connect To politeianet.gr
    # TODO Enter isbn to correct field 
    # TODO Click first entry
    # TODO Retrieve information
    pass

@api_view(['GET'])
def ImportExcelFilePoliteia(request):
    # TODO Set up Celery, Redis and Selenium
    # TODO Set up Pandas
    # TODO Export isbns from excel
    # TODO Connect To politeianet.gr
    # TODO Enter isbn to correct field 
    # TODO Click first entry
    # TODO Retrieve information
    pass