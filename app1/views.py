import django.http
from django.shortcuts import render, redirect, HttpResponse
from app1.models import Kitob, Student, Muallif, Record

def men(request):
    return django.http.HttpResponse("Ismim Muhammadqodir")

def loyiha(request):
    return django.http.HttpResponse("Bu loyiha Kutubxona tizimini boshqarish uchun xizmat qildi")

def asosiy(request):
    return render(request, "asosiy.html")

def recordlar(request):
    if request.method == 'POST':
        st = Student.objects.get(id=request.POST.get("s"))
        kt = Kitob.objects.get(id=request.POST.get("k"))
        if st.kitob_soni == 3:
            return HttpResponse("<h1>Biz sizga kitob berolmaymiz, oldingilarini qaytaring!</h1>")
        Record.objects.create(
            student=st,
            kitob=kt,
            sana=request.POST.get("sana")
        )
    s = Student.objects.all()
    k = Kitob.objects.all()
    r = Record.objects.all()
    return render(request, "recordlar.html", {"recordlar":r, "ktb":k, "stu":s})

def kitoblar(request):

    m = Muallif.objects.all()
    if request.method == 'POST':
        m = request.POST.get("m")
        muallif = Muallif.objects.get(id=m)
        Kitob.objects.create(
            nom=request.POST.get("n"),
            sana=request.POST.get("s"),
            sahifa=request.POST.get("sah"),
            janr=request.POST.get("j"),
            muallif=muallif,
        )

    soz = request.GET.get("qidirish")
    if soz == None:
        hammasi = Kitob.objects.all().order_by("nom")
    else:
        hammasi = Kitob.objects.filter(nom=soz)
    return render(request, "books.html", {"kitoblar":hammasi,"avtorlar":m})

def students(request):
    if request.method == 'POST':
        if request.POST.get("b") == "False":
            qaytarish = False
        else:
            qaytarish = True
        Student.objects.create(
            ism=request.POST.get("ismi"),
            guruh=request.POST.get("guruhi"),
            k_soni=request.POST.get("k_s"),
            bitiruvchi=qaytarish
        )
    db = request.GET.get("qidirish")
    if db == None:
        hamma = Student.objects.all().order_by("ism")
    else:
        hamma = Student.objects.filter(ism=db)
    return render(request, "studentlar.html", {"students":hamma})

def st_ochir(request, son):
    Student.objects.get(id=son).delete()
    return redirect("/students")


def mualliflar(request):
    if request.method == 'POST':
        if request.POST.get("t") == "True":
            natija = False
        else:
            natija = True
        Muallif.objects.create(
            ism=request.POST.get("ismi"),
            trik=natija,
            yosh=request.POST.get("y"),
            Kitoblar_soni=request.POST.get("k_s")
        )
        return redirect("/muallif/")
    mod = request.GET.get("Qidirish")
    if mod == None:
        m = Muallif.objects.all().order_by("ism")
    else:
        m = Muallif.objects.filter(ism=mod)
    return render(request, "muallif.html", {"avtorlar":m})

def mlf_ochir(request, son):
    Muallif.objects.get(id=son).delete()
    return redirect("/mualliflar")


def kitob_ochir(request, son):
    Kitob.objects.get(id=son).delete()
    return redirect("/kitoblar/")

def muallif_edit(request, pk):
    if request.method == 'POST':
        m1 = Muallif.objects.get(id=pk)
        m1.ism=request.POST.get("ismi")
        m1.yosh=request.POST.get("y")
        m1.kitoblar_soni=request.POST.get("k_s")
        m1.save()
        return redirect("/mualliflar")
    m = Muallif.objects.get(id=pk)
    return render(request, "muallif-edit.html", {"muallif":m})

def books_edit(request, op):
    if request.method == 'POST':
        a1 = Kitob.objects.get(id=op)
        a1.ism=request.POST.get("n")
        a1.sana=request.POST.get("s")
        a1.sahifasi=request.POST.get("sah")
        a1.save()
        return redirect("/kitoblar")
    a = Kitob.objects.get(id=op)
    return render(request, "books-edit.html", {"kitob":a})
