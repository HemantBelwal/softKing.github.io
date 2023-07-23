from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.

#def index(request):
#    return HttpResponse('''"Hello hemant" <a href = "https://www.facebook.com/"><br>Code with hemant</br></a>''')

def index(request):
    params = {'name': 'Hemant'}
    return render(request, 'index.html', params)

def home(request):
    params = {'name': 'Home Page'}
    return render(request, 'index.html', params)

def navigator(request):
    return HttpResponse('''<a href = "https://www.facebook.com/">Facebook</a><br><a href = "https://www.google.com/">Google</a>''')


def items(request):
    # initialize variable
    abcd = request.POST.get('text', 'default')
    analysed_text = request.POST.get('analysed', 'off')
    cap_letter = request.POST.get('capLetter', 'off')
    char_count = request.POST.get('charCount', 'off')
    index = 0
    # punc list
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    # Check checkbox return is on or not
    if analysed_text == 'on' and analysed_text == 'on' and char_count == 'on':
        analysed_value = ''
        for char in abcd:
            if char not in punctuations:
                analysed_value = analysed_value + char.upper()
                index+=1
        analysed_value = analysed_value + '\nTotal-count:' + str(index)
        params = {'analysed_data_type': 'All included', 'analysed': analysed_value}
        return render(request, 'analyse.html', params)
    elif analysed_text == 'on':
        analysed_value = ''
        for char in abcd:
            if char not in punctuations:
                analysed_value = analysed_value + char
        params = {'analysed_data_type': 'Ignore special character', 'analysed': analysed_value}
        return render(request, 'analyse.html', params)
    elif cap_letter == 'on':
        cap_values=''
        for char in abcd:
            if char not in punctuations:
                cap_values = cap_values + char.upper()
        params = {'analysed_data_type': 'Capital letters', 'analysed': cap_values}
        return render(request, 'analyse.html', params)
    elif char_count == 'on':
        for char in abcd:
                index += 1
        params = {'analysed_data_type': 'Total Number no of characters', 'analysed': index}
        return render(request, 'analyse.html', params)
    #return HttpResponse('''"Want to see item list click on me" <a href ="https://www.amazon.com/"><br>Item list</br></a>
    #            If you want to go back please click on me"<form>
    #         <input type="button" value="Go back!" onclick="history.go(-1)">
    #        </form>''')
def about(request):
    return HttpResponse("How can I help you?")