from django.http import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from .models import BloodLevel

def index(request):
    return render(request, 'home.html')



def get_blood_levels(request):
    try:
        blood_levels = BloodLevel.objects.all()
        
        blood_levels_dict = {}
        for level in blood_levels:
            blood_levels_dict[level.blood_category] = level.percentage_value
        
        return JsonResponse(blood_levels_dict)
    except ObjectDoesNotExist:
        return JsonResponse({"error": "No blood levels found"}, status=404)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)