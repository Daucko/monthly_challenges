from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

monthly_challenges = {
    "january": "Eat no meat for the entire month!",
    "february": "Walk for at least 20 minutes every day!",
    "march": "Learn Django for al least 20 minutes every day!",
    "april": "Eat no meat for the entire month!",
    "may": "Walk for at least 20 minutes every day!",
    "june": "Learn Django for al least 20 minutes every day!",
    "july": "Eat no meat for the entire month!",
    "august": "Walk for at least 20 minutes every day!",
    "september": "Learn Django for al least 20 minutes every day!",
    "october": "Eat no meat for the entire month!",
    "november": "Walk for at least 20 minutes every day!",
    "december": None,
    # "december": "Learn Django for al least 20 minutes every day!",
}

# Create your views here.


def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())

    return render(request, "challenges/index.html", {
        "months": months,
    })

    # for month in months:
    #     capitalized_month = month.capitalize()
    #     month_path = reverse("month-challenge", args=[month])
    #     list_items += f"<li><a href={month_path}>{capitalized_month}</a></li>"

    # response_data = f"<ul>{list_items}</ul>"

    # return HttpResponse(response_data)


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid month")

    redirect_month = months[month-1]
    # /challenges/january
    redirect_path = reverse("month-challenge", args=[redirect_month])

    # return HttpResponseRedirect(f"/challenges/{redirect_month}")
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
    # response_data = f"<h1 style='color:red;'>{challenge_text}</h>"
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month": month,
        })
    # response_data = render_to_string("challenges/challenge.html")
    # return HttpResponse(response_data)
    except:
        raise Http404()
        # response_data = render_to_string("404.html")
        # # return HttpResponseNotFound('''<h1>This month is not <span style="color:red;">supported!</span></h1>''')
        # return HttpResponseNotFound(response_data)
