from .models import Gallery,Team,logo,blog, MentorConnectDB,OurStartup,DemoDayPic,fishieries,FooterEditPage,SocialMediaLinks
import random
def get_vals(request,data):
    datas = []
    for i in data:
        datas.append(request.POST.get(i))
    return data

def get_images():
    images = Gallery.objects.all()
    cat = []
    temp = []
    items = []
    for i in images:
        cat.append(i.categories)
    for i in list(set(cat)):
        temp = []
        for j in images:
            if i == j.categories :
                temp.append(j)
        items.append(temp)
    return [items,images]

def get_team():
    images = Team.objects.all()
    cat = []
    temp = []
    items = []
    for i in images:
        cat.append(i.categories)
    for i in list(set(cat)):
        temp = []
        for j in images:
            if i == j.categories :
                temp.append(j)
        items.append(temp)
    return items

def reguler_datas(data=False):
    out = dict()
    try:
        logo_ = logo.objects.all()
        last_logo = logo.objects.latest("L_id")
        if data:
            out = {'logo':last_logo,'logo_collection':logo_[::-1],}
            out = dict(out,**data)
        else:
            out = {'logo':last_logo,'logo_collection':logo_[::-1]}
    except:
        print("Erorr are occers in Tools -> reguler_datas function {may be the db is empty we can't load the icons so you can see this message}")
    return dict(out,**{'FooterEditPage':FooterEditPage.objects.all()[::-1],'SocialMediaLinks':SocialMediaLinks.objects.all()[::-1]})

def freguler_datas(data=False):
    out = dict()
    try:
        logo_ = fishieries.objects.all()
        last_logo = fishieries.objects.latest("L_id")
        if data:
            out = {'logo':last_logo,'fishieries_collection':logo_[::-1]}
            out = dict(out,**data)
        else:
            out = {'logo':last_logo,'fishieries_collection':logo_[::-1]}
    except:
        print("Erorr are occers in Tools -> reguler_datas function {may be the db is empty we can't load the icons so you can see this message}")
    return out

def get_blog():
    images = blog.objects.all()
    cat = []
    temp = []
    items = []
    for i in images:
        cat.append(i.categories)
    for i in list(set(cat)):
        temp = []
        for j in images:
            if i == j.categories :
                temp.append(j)
        items.append(temp)
    for x,i in enumerate(items):
        items[x] = i[::-1]
    return items


def get_startup():
    images = OurStartup.objects.all()
    cat = []
    temp = []
    items = []
    for i in images:
        cat.append(i.categories)
    for i in list(set(cat)):
        temp = []
        for j in images:
            if i == j.categories :
                temp.append(j)
        items.append(temp)
    return items


def get_DemoDayPic():
    images = DemoDayPic.objects.all()
    cat = []
    temp = []
    items = []
    for i in images:
        cat.append(i.categories)
    for i in list(set(cat)):
        temp = []
        for j in images:
            if i == j.categories :
                temp.append(j)
        items.append(temp)
    return items