# tp3/website/views.py
from django.shortcuts import render

def index(request):
    context = {
        'title': 'TP WEB L3 Info',
        'about': get_about()
    }
    return render(request, 'website/pages/index.html', context)

def about(request):

    context = {
        'title': 'TP WEB L3 Info',
        'about': get_about()
    }
    return render(request, 'website/pages/about.html', context)

def contact(request):
    return render(request, 'website/pages/contact.html')

def get_about():
    data = {
        'section_title': 'Since 1998',
        'about_title': 'Making transportation fast and safe',
        'description': """
            Lorem Ipsum is simply dummy text of the printing and typesetting industry. 
            lorem Ipsum has been the industry standard dummy text ever since 
            the when an unknown printer took a galley of type 
            and scrambled it to make a type specimen book.
        """,
        'about_author': 'Toto Titi',
        'about_fonction': "Directeur General",
        'about_service':[
            {
                'img':'1.svg',
                'title':'Fast Deliver',
                'description':'Lorem Ipsum',
                'order':1,
            },
            {
                'img':'1.svg',
                'title':'100% Satifaction',
                'description':'Lorem Ipsum',
                'order':2,
            },
            {
                'img':'3.svg',
                'title':'24x7 Service',
                'description':'Lorem Ipsum',
                'order':3,
            },
        ]
    }
    return data

def services(request):
    return render(request,'website/pages/our-services.html')


def services_detail(request):
    # Context can be extended later to pass dynamic service data
    context = {
        'title': 'Service Details'
    }
    return render(request, 'website/pages/services-detail.html', context)


def gallery(request):
    return render(request, 'website/pages/gallery.html')


def team(request):
    return render(request, 'website/pages/team.html')


def pricing(request):
    return render(request, 'website/pages/pricing.html')


def blog(request):
    """Render the blog listing page."""
    context = {
        'title': 'Blog'
    }
    return render(request, 'website/pages/blog.html', context)


def single_blog_right(request):
    """Render single blog post with right sidebar."""
    return render(request, 'website/pages/single-blog-post-right-sidebar.html')


def single_blog_left(request):
    """Render single blog post with left sidebar."""
    return render(request, 'website/pages/single-blog-post-left-sidebar.html')


def single_blog_no_sidebar(request):
    """Render single blog post without sidebar."""
    return render(request, 'website/pages/single-blog-post-without-sidebar.html')