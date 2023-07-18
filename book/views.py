from django.shortcuts import render
from .models import Book,Review
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from .forms import ReviewForm,AddBookForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
    searchTerm = request.GET.get('searchBook')
    if searchTerm:
        books = Book.objects.filter(title__icontains=searchTerm)
        if books.count() ==0:
              books = Book.objects.all()
        
    else:
        books = Book.objects.all()
    
    context = {
        'searchTerm': searchTerm,
        'books': books
    }
    return render(request, 'home.html',context)


def about(request):
    return render(request, 'about.html')

def signup(request):
    email = request.GET.get('email')
    return render(request, 'signup.html',{'email':email})

def detail(request,book_id):
    book = get_object_or_404(Book, pk=book_id)
    reviews = Review.objects.filter(book = book)
    return render(request, 'detail.html', {'book':book,'reviews':reviews})

def createbook(request):
    if request.method == 'GET':
        form = AddBookForm()
      
    else:
        form = AddBookForm(request.POST,request.FILES)
        if form.is_valid():
                print('datas inside form',form.cleaned_data)
                post = form.save(commit=False)
                post.save()
                print(post.save())
                return redirect('home')
        else:
                return render(request, 'createbook.html', {'form':form, 'error':'bad data passed in'})
    return render(request, 'createbook.html', {'form':form})
    
    
    # if request.method == 'POST':
    #     form = AddBookForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('home')
    # else:
    #         form = AddBookForm()
    # return render(request, 'createbook.html', {'form':form})


@login_required
def createreview(request,book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.method == 'GET':
        form = ReviewForm()
        return render(request, 'createreview.html', {'book':book,'form':form})
    else:
        try:
            form = ReviewForm(request.POST)
            newReview = form.save(commit=False)
            newReview.user = request.user
            newReview.book = book
            newReview.save()
            return redirect('detail', newReview.book.id)
        except ValueError:
            return render(request, 'createreview.html', {'book':book,'form':form, 'error':'bad data passed in'})
        
@login_required
def updatereview(request,review_id):
    review = get_object_or_404(Review,pk = review_id, user = request.user)
    if request.method == 'GET':
        form = ReviewForm(instance = review)
        return render(request, 'updatereview.html', {'review':review,'form':form})
    else:
        try:
            form = ReviewForm(request.POST, instance = review)
            form.save()
            return redirect('detail', review.book.id)
        except ValueError:
            return render(request, 'updatereview.html', {'review':review,'form':form, 'error':'bad data passed in'})
        
@login_required
def deletereview(request,review_id):
    review = get_object_or_404(Review,pk = review_id, user = request.user)
    review.delete()
    return redirect('detail', review.book.id)