import datetime as datetime
from django.shortcuts import render
from django.contrib import messages

# from myapp.models import *pg1_new_beds
from branch1app.models import *
import datetime
from . import admin_dashboard_calculations_br1
import branch1app

def guest_rent_update_ob_ch1(request):
    #current_room_rent = request.POST.get('current_room_rent')
    updated_amount = request.POST.get('updated_amount')
    share_types = request.POST.get('share_type')
    action_type = request.POST.get('action_type')
    print('updated_amount',updated_amount)

    if updated_amount == None:
        updated_amount = 0

    #if current_room_rent == None:
    #    current_room_rent = 0

    if action_type == "Addition":
        iunb_data = pg1_new_beds.objects.all().filter(flag=2,share_type=share_types)
        iunb_data_l = []
        for i in iunb_data:
            iunb_data_l.append(i.id)
        print('iunb_datall',iunb_data_l)
        for i in range(len(iunb_data_l)):
            iunb = pg1_new_beds.objects.get(flag=2,id=iunb_data_l[i],share_type=share_types)
            #iunb.monthly_rent = float(current_room_rent) + float(updated_amount)
            iunb.monthly_rent = updated_amount
            iunb.save()

        iunb_data_n = pg1_new_guest.objects.all().filter(flag=2, share_type=share_types)
        iunb_data_n_l = []
        for i in iunb_data_n:
            iunb_data_n_l.append(i.id)
        print('iunb_datall', iunb_data_n_l)
        for i in range(len(iunb_data_l)):
            iunb = pg1_new_guest.objects.get(flag=2,id=iunb_data_n_l[i],share_type=share_types)
            #iunb.monthly_rent = float(current_room_rent) + float(updated_amount)
            iunb.monthly_rent = updated_amount
            iunb.save()


    return render(request,'branches/branch1/branch_settings/guest/guest_rent_update.html')