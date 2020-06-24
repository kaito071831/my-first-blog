from django.shortcuts import render

def post_list(request):
    return rendar(request, 'blog/post_list.html', {})
