from django.http import HttpResponse, HttpRequest
from django.shortcuts import render


# Create your views here.
def hello(request):
    return HttpResponse("Hello World")


def number(request, num):
    resp = "<html><body><h1>{}</h1></body></html>".format(num)
    return HttpResponse(resp)


def numbers(request, num):
    context = {
        'num_arg': num,
    }
    return render(request, 'numbers.html', context)


def info(request):
    values = request.META.items()
    html = []
    for key, value in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (key, value))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))


def getinfo(request):
    """Renders sendinfo page"""
    assert isinstance(request, HttpRequest)
    if 'name' in request.GET and 'age' in request.GET:
        name = request.GET['name']
        age = request.GET['age']
        if name and age:
            context = {
                'name': name,
                'age': age,
            }
            return render(request, 'send_results.html', context)
        else:
            context = {
                'error': False,
            }
            return render(request, 'send_info.html', context)


def imc(request):
    """Renders IMC page"""
    assert isinstance(request, HttpRequest)
    if 'height' in request.GET and 'weight' in request.GET:
        # Cast arguments to float and validate them
        try:
            height = float(request.GET['height'])
            weight = float(request.GET['weight'])
        except ValueError as verr:
            return HttpResponse('Error')

        # Compute arguments for page
        imc = int(weight)/int(height)**2
        context = {
            'height': height,
            'weight': weight,
            'imc': imc,
            'classification': get_classification(imc)
        }

        return render(request, 'imc_results.html', context)



def get_classification(imc: float):
    if imc < 18.5:
        return "Underweight"
    elif imc < 25:
        return "Normal Weight"
    elif imc < 30:
        return "Overweight"
    elif imc < 35:
        return "Class I Obesity"
    elif imc < 40:
        return "Class II Obesity"
    return "Class III Obesity"

