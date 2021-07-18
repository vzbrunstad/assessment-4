from django.shortcuts import render,redirect, HttpResponse
from .models import Category, Post
from .forms import CategoryForm, PostForm

def category_list(request):
    category_list = Category.objects.all()
    return render(request, 'craigslist/category_list.html', {'category_list': category_list})


def category_new(request):
    if request.method == 'POST':
        category_form = CategoryForm(request.POST)
        if category_form.is_valid():
            category_form.save()
            return redirect('categories:category_list')
    else:
        category_form = CategoryForm()
        context = {'category_form': category_form, 'type_of_request': 'New'}

    return render(request, 'craigslist/category_form.html', context)


def category_detail(request, category_id):

    category = Category.objects.get(id=category_id)
    posts = category.post_category.all()

# no such column: craigslist_app_post.post_category_id
    return render(request, 'craigslist/category_detail.html', {'category': category , 'posts': posts})

def category_edit(request, category_id):
    category = Category.objects.get(id=category_id)

    if request.method == 'POST':
        category_form = CategoryForm(request.POST, instance=category)
        if category_form.is_valid():
            category_form.save()
            return redirect('categories:category_detail', category_id=category_id)
    else:
        category_form = CategoryForm(instance=category)
        context = {'category_form': category_form, 'type_of_request': 'Edit'}

    return render(request, 'craigslist/category_form.html', context)


def category_delete(request,category_id):
    category = Category.objects.get(id=category_id)
    category.delete()
    return redirect('categories:category_list')


def post_detail(request,category_id, post_id):
    category = Category.objects.get(id=category_id)
    post = category.post_category.get(id=post_id)

    return render(request, 'craigslist/post_detail.html', {'category': category , 'post': post})
    pass

def post_new(request, category_id):
    category = Category.objects.get(id=category_id)
    if request.method == 'POST':
        post_form = PostForm(request.POST)
        if post_form.is_valid():
            post_new = post_form.save(commit=False)
            post_new.category = category
            post_new.save()  # saves to db
            return redirect('categories:category_detail', category_id)
    else:
        post_form = PostForm()
        context = {'post_form': post_form, 'type_of_request': 'New', 'category': category}

    return render(request, 'craigslist/post_form.html', context)


def post_edit(request, category_id, post_id):
    category = Category.objects.get(id=category_id)
    post = category.post_category.get(id=post_id)
    if request.method == 'POST':
        post_form = PostForm(request.POST, instance=post)
        if post_form.is_valid():
            post_new = post_form.save(commit=False)
            post_new.category = category
            post_new.save()
            return redirect('categories:post_detail', category_id=category_id, post_id=post_new.id)
    else:
        post_form = PostForm(instance=post)
        context = {'post_form': post_form,
                'type_of_request': 'Edit', 'category': category}

    return render(request, 'craigslist/post_form.html', context)

def post_delete(request, category_id, post_id):
    category = Category.objects.get(id=category_id)
    post = category.post_category.get(id=post_id)
    post.delete()
    return redirect('categories:category_detail', category_id=category_id)