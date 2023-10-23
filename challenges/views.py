from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
#from django.template.loader import render_to_string


monthly_challenges = {
    "january": "Don't eat meat for the whole month",
    "february": "Go for a 20 minute walk everyday",
    "march": "Learn Django for at least 20 minutes a day",
    "april": "Don't eat meat for the whole month",
    "may": "Go for a 20 minute walk everyday",
    "june": "Learn Django for at least 20 minutes a day",
    "july": "Don't eat meat for the whole month",
    "august": "Go for a 20 minute walk everyday",
    "september": "Learn Django for at least 20 minutes a day",
    "october": "Don't eat meat for the whole month",
    "november": "Go for a 20 minute walk everyday",
    "december": "Learn Django for at least 20 minutes a day"
}

# Create your views here.
def index(request):
    # list_items = ""
    months = list(monthly_challenges.keys())

    return render(request, "challenges/index.html", {
        "months": months
    })

    # for month in months:
    #     capitalized_month = month.capitalize()
    #     month_path = reverse("month-challenge", args=[month])
    #     list_items += f"<li><a href =\"{month_path}\">{capitalized_month}</a></li>"
    
    # response_data = f"<ul>{list_items}</ul>"

    # return HttpResponse(response_data)


def monthly_challenge_by_number(request, month):

    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Out of bounds!!")
    
    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request,"challenges/challenge.html", {
            "text": challenge_text,
            "month_name": month
        })
        # response_data = render_to_string("challenges/challenge.html")
        # return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("<h1>Month not supported</h1>")



