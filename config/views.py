
from django.shortcuts import render


def home(request):
    result = None
    category = None
    result_color = ""

    if request.method == "POST":
        feet = float(request.POST.get("feet"))
        inches = float(request.POST.get("inches"))
        weight = float(request.POST.get("weight"))

        height = (feet * 12) + inches
        height_meters = height * 0.0254

        if height_meters > 0:
            bmi = weight / (height_meters ** 2)
            result = round(bmi, 2)

            if bmi < 18.5:
             category = "Underweight"
             result_color = "underweight"
            elif bmi < 25:
             category = "Normal weight"
             result_color = "normal"
            elif bmi < 30:
             category = "Overweight"
             result_color = "overweight"
            else:
             category = "Obesity range"
            result_color = "obesity"
            

           

    return render(request, "index.html", {
    "result": result,
    "category": category,
    "result_color": result_color if result is not None else "",

    })