from django.shortcuts import render
from .models import *
import re

from django.contrib.auth.decorators import login_required


from django.http import JsonResponse
from django.core.serializers import serialize
import json


# Create your views here.


def bookid(request, bookid):
    titleids = B1chapter.objects.all()

    c1 = B1chapter.objects.get(id=1)
    c1subs = c1.b1subhead_set.all()

    p = B1chapter.objects.get(id=1).b1subhead_set.all()

    c2 = B1chapter.objects.get(id=2)
    c2subs = c2.b1subhead_set.all()

    c3 = B1chapter.objects.get(id=3)
    c3subs = c3.b1subhead_set.all()

    c4 = B1chapter.objects.get(id=4)
    c4subs = c4.b1subhead_set.all()

    context = {
        "titleids": titleids,
        "c1": c1,
        "c2": c2,
        "c3": c3,
        "c4": c4,
        "c1subs": c1subs,
        "c2subs": c2subs,
        "c3subs": c3subs,
        "c4subs": c4subs,
    }
    return render(request, 'bookonline/bookid.html', context)


@login_required
def titles(request, bookid, subhead):

    bookid = B1chapter.objects.get(id=bookid)
    subheading = B1subhead.objects.get(subheads=subhead)

    peragraphs = subheading.b1pera_set.all()

    bvol = subheading.chapvolume
    bchap = bvol.chapTitle

    # serialized_data = serialize("json", peragraphs)
    # serialized_data = json.loads(serialized_data)
    # serialized_data

    # print(serialized_data)
    # print("nine one see diff")
    # print(json.dumps(serialized_data, indent = 3))

    titleids = B1chapter.objects.all()

    c1 = B1chapter.objects.get(id=1)
    c1subs = c1.b1subhead_set.all()

    c2 = B1chapter.objects.get(id=2)
    c2subs = c2.b1subhead_set.all()

    c3 = B1chapter.objects.get(id=3)
    c3subs = c3.b1subhead_set.all()

    c4 = B1chapter.objects.get(id=4)
    c4subs = c4.b1subhead_set.all()

    currentid = subheading.id

    # next = subheading.id + 1

    if currentid > 1:
        pre = subheading.id - 1
    else:
        pre = subheading.id

    if currentid < 94:
        next = subheading.id + 1
    else:
        next = subheading.id

    nexturl = B1subhead.objects.get(id=next)
    preurl = B1subhead.objects.get(id=pre)

    context = {
        "titleids": titleids,
        "bookid": bookid,
        "subheading": subheading,
        "peragraphs": peragraphs,
        "bchap": bchap,
        "bvol": bvol,
        "nexturl": nexturl,
        "preurl": preurl,
        "next": next,
        "pre": pre,
        "currentid": currentid,


        "c1": c1,
        "c2": c2,
        "c3": c3,
        "c4": c4,
        "c1subs": c1subs,
        "c2subs": c2subs,
        "c3subs": c3subs,
        "c4subs": c4subs,
    }

    return render(request, 'bookonline/titles.html', context)


def home(request):
    titles = B1chapter.objects.all()

    p = B1chapter.objects.get(id=1).b1subhead_set.all()
    book = B1chapter.objects.all()

    context = {'titles': titles, "p": p, }

    return render(request, 'bookonline/home.html', context)


def booklist(request):
    booklist = Books.objects.all()

    context = {'booklist': booklist, }
    return render(request, 'bookonline/booklist.html', context)


def chapterdisplay(request, bookid, chptitle):

    bookname = Books.objects.get(id=bookid)
    chaptertitle = B2chapter.objects.get(chapTitle=chptitle)

    peragraphs = chaptertitle.titletext

    context = {'bookname': bookname,
               "chaptertitle": chaptertitle,
               "peragraphs": peragraphs,
               }
    return render(request, 'bookonline/chapterdisplay.html', context)


def sub1display(request, bookid, chptitle, sub1):

    bookname = Books.objects.get(id=bookid)
    chaptertitle = B2chapter.objects.get(chapTitle=chptitle)
    subhead1 = B2subhead1.objects.get(id=sub1)
    peragraphs = subhead1.subhead1text
    print(sub1)

    context = {
                'bookname': bookname,
               "chaptertitle": chaptertitle,
               "peragraphs": peragraphs,
               "subhead1": subhead1,
               }
    return render(request, 'bookonline/subhead1display.html', context)


def sub2display(request, bookid, chptitle, sub1, sub2):

    bookname = Books.objects.get(id=bookid)
    chaptertitle = B2chapter.objects.get(chapTitle=chptitle)
    subhead1 = B2subhead1.objects.get(id=sub1)
    subhead2 = B2subhead2.objects.get(id=sub2)
    peragraphs = subhead2.subhead2text

    context = {
                'bookname': bookname,
               "chaptertitle": chaptertitle,
               "subhead1": subhead1,
               "subhead2": subhead2,
               "peragraphs": peragraphs,
               }

    return render(request, 'bookonline/subhead2display.html', context)


def home2(request):

    titles = B2chapter.objects.all()
    context = {'titles': titles, }
    return render(request, 'bookonline/home2.html', context)


def books(request, bookid):

    bookname = Books.objects.get(id=bookid)
    # manager not avialble to model instance only to model class see django

    # p = B1chapter.objects.get(id=1).b1subhead_set.all()
    # titles = bookname.__class__.objects.get(id=bookid).b2chapter_set.all()
    ch = B2chapter.objects.filter(Books__id=bookid)
    

    context = {'ch': ch,
               'bookname': bookname}
    
    print(type(ch))

    for chap in ch:
        print('Chapter:   ', chap.id, chap.chapTitle)

        for sub1 in chap.b2subhead1_set.all():
            print('subhead1:        ', sub1.id, sub1.subhead1titles)

            for sub2 in sub1.b2subhead2_set.all():
                print('subhead2:            ', sub2.id, sub2.subhead2titles)


    return render(request, 'bookonline/bookdetails.html', context)








def index(request, pk):
    data = 1
    plist = ['India', 'Europe', 'America']

    pera = B1pera.objects.get(id=pk)

    context = {
        "data": data,
        "plist": plist,
        "pera": pera,

    }
    return render(request, 'bookonline/index.html', context)


def findex(request):

    a = Aindex.objects.all()
    b = Bindex.objects.all()
    c = Cindex.objects.all()

    context = {
        "a": a,
        "b": b,
        "c": c,


    }
    return render(request, 'bookonline/findex.html', context)


# for chap in ch:
#     chap.chapTitle
#     for sub1 in chap.b2subhead1_set.all:
#         sub1.subhead1titles
#         for sub2 in sub1.b2subhead2_set.all:
#             sub2.subhead2titles 
            
            

        