from django.shortcuts import render_to_response
from .models import Blogpost, Keyword
from .forms import ArchivesForm
from django.db.models import Q


# Create your views here.

def post(request):
    imglist = []
    blogpostlist = Blogpost.objects.order_by('-date')[:4]
    keywordlist = Keyword.objects.all()
    # savedblogs = blogpostlist
    for x in blogpostlist:
        str1,st2,str3 = x.img.url.split('/')
        imglist.append(str3)
    return render_to_response('home.html', {'blogpostlist': blogpostlist, 'keywordlist': keywordlist, 'imglist':imglist})

"""
def bookmark(request):
    blogpostlist = Blogpost.objects.order_by('-date')[:4]
    return render_to_response('home.html', {'blogpostlist': blogpostlist, 'keywordlist': keywordlist})
"""

def blog(request):
    imgblog = str()
    blogquery = request.GET.get('blogtitle')
    blogobj = Blogpost.objects.get(title=blogquery)
    str1,st2,str3 = blogobj.img.url.split('/')
    imgblog = str3
    keywords = blogobj.keywords.values_list()    
    mostrecentblogs = Blogpost.objects.order_by('-date')[:3]
    return render_to_response('blog.html', {'blogpost': blogobj, 'keywords': keywords, 'imgblog': imgblog, 'mostrecentblogs': mostrecentblogs})


def archives(request):

    ""
    query = request.GET.get('blogtitle', '')
    if query:
        qset = (Q(title__icontains=query))
        results = Blogpost.objects.filter(qset).order_by('-date')
        return render_to_response('archives.html', {'results': results, 'query': query})
    else:
        results = []
    #return render_to_response('archives.html', {'results': results, 'query': query})
   
    #def archives(request):
    
    datequery = request.GET.get('pubdate', '')
    if datequery:
        qset = (Q(date=datequery))
        results = Blogpost.objects.filter(qset)
        return render_to_response('archives.html', {'results': results, 'datequery': datequery})
    else:
        results = []
    #return render_to_response('archives.html', {'results': results, 'datequery': datequery})
    
    #def archives(request):
    
    keywordquery = request.GET.get('key', '')
    if keywordquery:
        qset = Keyword.objects.filter(keyword = keywordquery)
        if qset:
            blogpost_ids = qset.values_list('blogposts')
            results = Blogpost.objects.filter(id__in=blogpost_ids)
        else:
            results = []
        return render_to_response('archives.html', {'results': results, 'keywordquery': keywordquery})
    else:
        results = []
        return render_to_response('archives.html', {'results': results, 'keywordquery': keywordquery})
    
def about(request):
    return render_to_response('about.html',)

def contact(request):
    return render_to_response('contact.html',)