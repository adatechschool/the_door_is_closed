from django.shortcuts import render
from django.http import HttpResponse
import codecs, cgi
from jinja2 import Template

# app = Flask(__name__)
def get_br_page():
    f = codecs.open("polls/browser.html", "r")
    form = cgi.FieldStorage()
    first_name = form.getvalue("first_name")
    print(first_name)
    open_html = f.read()
    return open_html
#
# @app.route("/")
# def browser_choose():
#     return render_template("./browser.html")

def print_submit(request):
    # print(request.POST.get("site"))
    return HttpResponse("Ayyyyyyyy lmao.")



def index(request):
    # HttpResponse(Template(get_br_page()))
    return HttpResponse(get_br_page())
