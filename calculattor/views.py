from django.shortcuts import render

# Create your views here.
def calc(request):
    if request.method == 'POST':
        num1 = int(request.POST.get('input_one'))
        num2 = int(request.POST.get('input_two'))
        sum = num1+num2
        print(num1,num2)
        return render(request, 'calc.html', {"result": sum})
        # print(opr)
    else:
        return render(request,'calc.html')