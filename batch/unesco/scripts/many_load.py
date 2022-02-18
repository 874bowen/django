import csv  # https://docs.python.org/3/library/csv.html

# https://django-extensions.readthedocs.io/en/latest/runscript.html

# python3 manage.py runscript many_load

from unesco.models import Category, State, Iso, Region, Site


def run():
    fhand = open('unesco/whc-sites-2018-clean.csv')
    reader = csv.reader(fhand)
    next(reader)  # Advance past the header

    Category.objects.all().delete()
    State.objects.all().delete()
    Iso.objects.all().delete()
    Region.objects.all().delete()
    Site.objects.all().delete()

    # Format
    # email,role,course
    # jane@tsugi.org,I,Python
    # ed@tsugi.org,L,Python
    # name	description	justification	year	longitude	latitude	area_hectares	category	state	region	iso


    for row in reader:
        print(row)

        c, created = Category.objects.get_or_create(name=row[7])
        s, created = State.objects.get_or_create(name=row[8])
        i, created = Iso.objects.get_or_create(name=row[10])
        r, created = Region.objects.get_or_create(name=row[9])
        try:
            y=int(row[3])
        except:
            y=None

        try:
            z=float(row[4])
        except:
            z=None

        try:
            l=float(row[5])
        except:
            l=None

        if row[6]=="":
            w=None
        else:
            w=float(row[6])

        try:
            j=row[2]
        except:
            j=None
        x = Site(name=row[0], description=row[1], justification=j, year=y, longitude=z, latitude=l, area_hectares=w, category=c, state=s, region=r, iso=i)

        x.save()