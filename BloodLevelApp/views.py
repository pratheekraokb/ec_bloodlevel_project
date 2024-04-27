from django.http import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from .models import BloodLevel
import json
from django.views.decorators.csrf import csrf_exempt


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
    
@csrf_exempt
def updateBloodLevels(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            
            for blood_category, percentage_value in data.items():
                try:
                    # Attempt to get the BloodLevel object with the given blood category
                    blood_level = BloodLevel.objects.get(blood_category=blood_category)
                    # If the BloodLevel object exists, update its percentage value
                    blood_level.percentage_value = percentage_value
                    blood_level.save()
                except BloodLevel.DoesNotExist:
                    # If BloodLevel object doesn't exist, create a new one
                    BloodLevel.objects.create(blood_category=blood_category, percentage_value=percentage_value)
            
            # Return success response
            return JsonResponse({"Msg": "Successfully Updated"})
        except Exception as e:
            # Return error response with details of the exception
            return JsonResponse({"Msg": f"Error in updating the database: {str(e)}"}, status=500)
    else:
        # Return error response if request method is not POST
        return JsonResponse({"Msg": "Invalid request method"}, status=405)