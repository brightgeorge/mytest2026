from django.urls import path, include

from . import admin_branch1
from . import admin_branch1
from . import branch1
from . import reports1
from . import payment1
from . import admin_dashboard_calculations_br1
from . import accounts1
from . import branch_settings1

urlpatterns = [

    path('branch1_dashboard_ob_ch1/', branch1.branch1_dashboard_ob_ch1, name='branch1_dashboard_ob_ch1'),
    path('branch1_dashboard1/',branch1.branch1_dashboard1,name='branch1_dashboard1'),
    path('user_dashboard_calculations_ob_ch1/',branch1.user_dashboard_calculations_ob_ch1,name='user_dashboard_calculations_ob_ch1'),

    path('background_ob_ch1',branch1.background_ob_ch1,name='background_ob_ch1'),
    path('background_regi_ob_ch1',branch1.background_regi_ob_ch1,name='background_regi_ob_ch1'),
    path('custom_background_regi_ob_ch1',branch1.custom_background_regi_ob_ch1,name='custom_background_regi_ob_ch1'),

#**room creation start herea
    #path('select_branch/',admin_branch1.select_branch,name='select_branch'),
    path('branch1_room_create_regi_ob_ch1/',admin_branch1.branch1_room_create_regi_ob_ch1,name='branch1_room_create_regi_ob_ch1'),
    path('view_all_room_ob_ch1/',admin_branch1.view_all_room_ob_ch1,name='view_all_room_ob_ch1'),
    path('delete_room_ob_ch1/<id>',admin_branch1.delete_room_ob_ch1,name='delete_room_ob_ch1'),

    path('branch1_room_create_ob_ch1/',admin_branch1.branch1_room_create_ob_ch1,name='branch1_room_create_ob_ch1'),

    path('multiple_branch1_room_create_regi1/',admin_branch1.multiple_branch1_room_create_regi1,name='multiple_branch1_room_create_regi1'),

#**room creation end here

#bed creation start here

    path('pg1_bed_create_regi_ob_ch1/', admin_branch1.pg1_bed_create_regi_ob_ch1, name='pg1_bed_create_regi_ob_ch1'),
    path('pg1_view_all_beds_ob_ch1/', admin_branch1.pg1_view_all_beds_ob_ch1, name='pg1_view_all_beds_ob_ch1'),
    path('delete_bed_ob_ch1/<id>', admin_branch1.delete_bed_ob_ch1, name='delete_bed_ob_ch1'),

    path('pg1_bed_create_ob_ch1/', admin_branch1.pg1_bed_create_ob_ch1, name='pg1_bed_create_ob_ch1'),

    path('single_pg1_bed_create_regi_ob_ch1/',admin_branch1.single_pg1_bed_create_regi_ob_ch1,name='single_pg1_bed_create_regi_ob_ch1'),
    path('update_bed_basic_details_ob_ch1/<id>',admin_branch1.update_bed_basic_details_ob_ch1, name='update_bed_basic_details_ob_ch1'),

    path('multiple_single_pg1_bed_create_regi1/',admin_branch1.multiple_single_pg1_bed_create_regi1,name='multiple_single_pg1_bed_create_regi1'),

#bed creation end here


#guest
    path('br1_admit_guest_ob_ch1/<id>',branch1.br1_admit_guest_ob_ch1,name='br1_admit_guest_ob_ch1'),
    path('view_all_new_guest_ob_ch1/',branch1.view_all_new_guest_ob_ch1,name='view_all_new_guest_ob_ch1'),
    path('update_br1_admit_guest_ob_ch1/<id>',branch1.update_br1_admit_guest_ob_ch1,name='update_br1_admit_guest_ob_ch1'),
    path('vacate_br1_guest_ob_ch1/<id>',branch1.vacate_br1_guest_ob_ch1,name='vacate_br1_guest_ob_ch1'),

    path('active_guest_details_ob_ch1/<guest_code>',branch1.active_guest_details_ob_ch1,name='active_guest_details_ob_ch1'),
    path('view_all_guest_ob_ch1/',branch1.view_all_guest_ob_ch1,name='view_all_guest_ob_ch1'),
    path('shift_guest_ob_ch1/<id>',branch1.shift_guest_ob_ch1,name='shift_guest_ob_ch1'),
    path('shift_guest_regi_ob_ch1/',branch1.shift_guest_regi_ob_ch1,name='shift_guest_regi_ob_ch1'),

    #path('branch11_bed_create_update/<id>',branch1.branch11_bed_create_update,name='branch11_bed_create_update'),
    #path('admit_guest/',views.admit_guest,name='admit_guest'),
    path('update_all_rent_ob_ch1/',branch1.update_all_rent_ob_ch1,name='update_all_rent_ob_ch1'),

    path('multiple_br1_admit_guest1/<id>',branch1.multiple_br1_admit_guest1,name='multiple_br1_admit_guest1'),

#guest end here


##################################
#_ADVANCE_ob_ch1 START HERE
################################


    path('choose_months_advance_ob_ch1/',branch1.choose_months_advance_ob_ch1,name='choose_months_advance_ob_ch1'),

    path('jan_advance_ob_ch1/', branch1.jan_advance_ob_ch1, name='jan_advance_ob_ch1'),
    path('jan_make_payments_advance_ob_ch1/<id>', branch1.jan_make_payments_advance_ob_ch1,name='jan_make_payments_advance_ob_ch1'),
    path('feb_advance_ob_ch1/', branch1.feb_advance_ob_ch1, name='feb_advance_ob_ch1'),
    path('feb_make_payments_advance_ob_ch1/<id>', branch1.feb_make_payments_advance_ob_ch1,name='feb_make_payments_advance_ob_ch1'),
    path('march_advance_ob_ch1/', branch1.march_advance_ob_ch1, name='march_advance_ob_ch1'),
    path('march_make_payments_advance_ob_ch1/<id>', branch1.march_make_payments_advance_ob_ch1,name='march_make_payments_advance_ob_ch1'),
    path('april_advance_ob_ch1/', branch1.april_advance_ob_ch1, name='april_advance_ob_ch1'),
    path('april_make_payments_advance_ob_ch1/<id>', branch1.april_make_payments_advance_ob_ch1, name='april_make_payments_advance_ob_ch1'),

    path('may_advance_ob_ch1/',branch1.may_advance_ob_ch1,name='may_advance_ob_ch1'),
    path('may_make_payments_advance_ob_ch1/<id>', branch1.may_make_payments_advance_ob_ch1, name='may_make_payments_advance_ob_ch1'),
    path('june_advance_ob_ch1/',branch1.june_advance_ob_ch1,name='june_advance_ob_ch1'),
    path('june_make_payments_advance_ob_ch1/<id>', branch1.june_make_payments_advance_ob_ch1, name='june_make_payments_advance_ob_ch1'),
    path('july_advance_ob_ch1/',branch1.july_advance_ob_ch1,name='july_advance_ob_ch1'),
    path('july_make_payments_advance_ob_ch1/<id>', branch1.july_make_payments_advance_ob_ch1, name='july_make_payments_advance_ob_ch1'),
    path('auguest_advance_ob_ch1/', branch1.auguest_advance_ob_ch1, name='auguest_advance_ob_ch1'),
    path('auguest_make_payments_advance_ob_ch1/<id>', branch1.auguest_make_payments_advance_ob_ch1, name='auguest_make_payments_advance_ob_ch1'),

    path('sept_advance_ob_ch1/', branch1.sept_advance_ob_ch1, name='sept_advance_ob_ch1'),
    path('sept_make_payments_advance_ob_ch1/<id>', branch1.sept_make_payments_advance_ob_ch1,name='sept_make_payments_advance_ob_ch1'),
    path('october_advance_ob_ch1/', branch1.october_advance_ob_ch1, name='october_advance_ob_ch1'),
    path('october_make_payments_advance_ob_ch1/<id>', branch1.october_make_payments_advance_ob_ch1, name='october_make_payments_advance_ob_ch1'),
    path('nov_advance_ob_ch1/', branch1.nov_advance_ob_ch1, name='nov_advance_ob_ch1'),
    path('nov_make_payments_advance_ob_ch1/<id>', branch1.nov_make_payments_advance_ob_ch1,name='nov_make_payments_advance_ob_ch1'),
    path('dec_advance_ob_ch1/', branch1.dec_advance_ob_ch1, name='dec_advance_ob_ch1'),
    path('dec_make_payments_advance_ob_ch1/<id>', branch1.dec_make_payments_advance_ob_ch1, name='dec_make_payments_advance_ob_ch1'),



##################################
#_ADVANCE_ob_ch1 END HERE
################################



##################################
#PAYMENTS START HERE
################################

    path('choose_months_ob_ch1/',branch1.choose_months_ob_ch1,name='choose_months_ob_ch1'),

    path('jan_ob_ch1/',branch1.jan_ob_ch1,name='jan_ob_ch1'),
    path('jan_manke_payments_ob_ch1/<id>',branch1.jan_manke_payments_ob_ch1,name='jan_manke_payments_ob_ch1'),

    path('feb_ob_ch1/',branch1.feb_ob_ch1,name='feb_ob_ch1'),
    path('feb_manke_payments_ob_ch1/<id>',branch1.feb_manke_payments_ob_ch1,name='feb_manke_payments_ob_ch1'),

    path('march_ob_ch1/',branch1.march_ob_ch1,name='march_ob_ch1'),
    path('march_manke_payments_ob_ch1/<id>',branch1.march_manke_payments_ob_ch1,name='march_manke_payments_ob_ch1'),

    path('april_ob_ch1/',branch1.april_ob_ch1,name='april_ob_ch1'),
    path('april_make_payments_ob_ch1/<id>',branch1.april_make_payments_ob_ch1,name='april_make_payments_ob_ch1'),

    path('may_ob_ch1/',branch1.may_ob_ch1,name='may_ob_ch1'),
    path('may_make_payments_ob_ch1/<id>',branch1.may_make_payments_ob_ch1,name='may_make_payments_ob_ch1'),

    path('june_ob_ch1/',branch1.june_ob_ch1,name='june_ob_ch1'),
    path('june_make_payments_ob_ch1/<id>',branch1.june_make_payments_ob_ch1,name='june_make_payments_ob_ch1'),

    path('july_ob_ch1/',branch1.july_ob_ch1,name='july_ob_ch1'),
    path('july_make_payments_ob_ch1/<id>',branch1.july_make_payments_ob_ch1,name='july_make_payments_ob_ch1'),

    path('aug_ob_ch1/',branch1.aug_ob_ch1,name='aug_ob_ch1'),
    path('aug_make_payments_ob_ch1/<id>',branch1.aug_make_payments_ob_ch1,name='aug_make_payments_ob_ch1'),

    path('sept_ob_ch1/',branch1.sept_ob_ch1,name='sept_ob_ch1'),
    path('sept_make_payments_ob_ch1/<id>',branch1.sept_make_payments_ob_ch1,name='sept_make_payments_ob_ch1'),

    path('oct_ob_ch1/',branch1.oct_ob_ch1,name='oct_ob_ch1'),
    path('oct_make_payments_ob_ch1/<id>',branch1.oct_make_payments_ob_ch1,name='oct_make_payments_ob_ch1'),

    path('nov_ob_ch1/',branch1.nov_ob_ch1,name='nov_ob_ch1'),
    path('nov_make_payments_ob_ch1/<id>',branch1.nov_make_payments_ob_ch1,name='nov_make_payments_ob_ch1'),

    path('dec_ob_ch1/',branch1.dec_ob_ch1,name='dec_ob_ch1'),
    path('dec_make_payments_ob_ch1/<id>',branch1.dec_make_payments_ob_ch1,name='dec_make_payments_ob_ch1'),

##################################
#PAYMENTS END HERE
################################

##################################
#MONTHLY MANAGEMENT PAYMENTS START HERE
################################

    path('choose_user_ob_ch1/', payment1.choose_user_ob_ch1, name='choose_user_ob_ch1'),
    path('payment_user_details_ob_ch1/<id>', payment1.payment_user_details_ob_ch1, name='payment_user_details_ob_ch1'),
    path('close_choose_user_ob_ch1/<id>',payment1.close_choose_user_ob_ch1,name='close_choose_user_ob_ch1'),

    path('monthly_jan_make_payments_ob_ch1/<id>', payment1.monthly_jan_make_payments_ob_ch1, name='monthly_jan_make_payments_ob_ch1'),
    path('monthly_feb_make_payments_ob_ch1/<id>', payment1.monthly_feb_make_payments_ob_ch1, name='monthly_feb_make_payments_ob_ch1'),
    path('monthly_march_make_payments_ob_ch1/<id>', payment1.monthly_march_make_payments_ob_ch1, name='monthly_march_make_payments_ob_ch1'),
    path('monthly_april_make_payments_ob_ch1/<id>', payment1.monthly_april_make_payments_ob_ch1, name='monthly_april_make_payments_ob_ch1'),
    path('monthly_may_make_payments_ob_ch1/<id>', payment1.monthly_may_make_payments_ob_ch1, name='monthly_may_make_payments_ob_ch1'),
    path('monthly_june_make_payments_ob_ch1/<id>', payment1.monthly_june_make_payments_ob_ch1, name='monthly_june_make_payments_ob_ch1'),

    path('monthly_july_make_payments_ob_ch1/<id>', payment1.monthly_july_make_payments_ob_ch1, name='monthly_july_make_payments_ob_ch1'),
    path('monthly_aug_make_payments_ob_ch1/<id>', payment1.monthly_aug_make_payments_ob_ch1, name='monthly_aug_make_payments_ob_ch1'),
    path('monthly_sept_make_payments_ob_ch1/<id>', payment1.monthly_sept_make_payments_ob_ch1, name='monthly_sept_make_payments_ob_ch1'),
    path('monthly_oct_make_payments_ob_ch1/<id>', payment1.monthly_oct_make_payments_ob_ch1, name='monthly_oct_make_payments_ob_ch1'),
    path('monthly_nov_make_payments_ob_ch1/<id>', payment1.monthly_nov_make_payments_ob_ch1, name='monthly_nov_make_payments_ob_ch1'),
    path('monthly_dec_make_payments_ob_ch1/<id>', payment1.monthly_dec_make_payments_ob_ch1, name='monthly_dec_make_payments_ob_ch1'),

##################################
#MONTHLY MANAGEMENT PAYMENTS END HERE
################################


#*********reports start here

#unpaid rent start here

    path('unpaid_rent_choose_months_ob_ch1/',branch1.unpaid_rent_choose_months_ob_ch1,name='unpaid_rent_choose_months_ob_ch1'),

    path('jan_unpaid_rent_ob_ch1/', branch1.jan_unpaid_rent_ob_ch1, name='jan_unpaid_rent_ob_ch1'),
    path('table_jan_unpaid_rent_ob_ch1/', branch1.table_jan_unpaid_rent_ob_ch1, name='table_jan_unpaid_rent_ob_ch1'),
    path('feb_unpaid_rent_ob_ch1/', branch1.feb_unpaid_rent_ob_ch1, name='feb_unpaid_rent_ob_ch1'),
    path('table_feb_unpaid_rent_ob_ch1/', branch1.table_feb_unpaid_rent_ob_ch1, name='table_feb_unpaid_rent_ob_ch1'),
    path('mar_unpaid_rent_ob_ch1/', branch1.mar_unpaid_rent_ob_ch1, name='mar_unpaid_rent_ob_ch1'),
    path('table_mar_unpaid_rent_ob_ch1/', branch1.table_mar_unpaid_rent_ob_ch1, name='table_mar_unpaid_rent_ob_ch1'),
    path('april_unpaid_rent_ob_ch1/', branch1.april_unpaid_rent_ob_ch1, name='april_unpaid_rent_ob_ch1'),
    path('table_april_unpaid_rent_ob_ch1/', branch1.table_april_unpaid_rent_ob_ch1, name='table_april_unpaid_rent_ob_ch1'),

    path('may_unpaid_rent_ob_ch1/', branch1.may_unpaid_rent_ob_ch1, name='may_unpaid_rent_ob_ch1'),
    path('table_may_unpaid_rent_ob_ch1/', branch1.table_may_unpaid_rent_ob_ch1, name='table_may_unpaid_rent_ob_ch1'),
    path('june_unpaid_rent_ob_ch1/', branch1.june_unpaid_rent_ob_ch1, name='june_unpaid_rent_ob_ch1'),
    path('table_june_unpaid_rent_ob_ch1/', branch1.table_june_unpaid_rent_ob_ch1, name='table_june_unpaid_rent_ob_ch1'),
    path('july_unpaid_rent_ob_ch1/', branch1.july_unpaid_rent_ob_ch1, name='july_unpaid_rent_ob_ch1'),
    path('table_july_unpaid_rent_ob_ch1',branch1.table_july_unpaid_rent_ob_ch1,name='table_july_unpaid_rent_ob_ch1'),
    path('aug_unpaid_rent_ob_ch1/', branch1.aug_unpaid_rent_ob_ch1, name='aug_unpaid_rent_ob_ch1'),
    path('table_aug_unpaid_rent_ob_ch1/',branch1.table_aug_unpaid_rent_ob_ch1,name='table_aug_unpaid_rent_ob_ch1'),

    path('sept_unpaid_rent_ob_ch1/', branch1.sept_unpaid_rent_ob_ch1, name='sept_unpaid_rent_ob_ch1'),
    path('table_sept_unpaid_rent_ob_ch1/', branch1.table_sept_unpaid_rent_ob_ch1, name='table_sept_unpaid_rent_ob_ch1'),
    path('oct_unpaid_rent_ob_ch1/', branch1.oct_unpaid_rent_ob_ch1, name='oct_unpaid_rent_ob_ch1'),
    path('table_oct_unpaid_rent_ob_ch1/', branch1.table_oct_unpaid_rent_ob_ch1, name='table_oct_unpaid_rent_ob_ch1'),
    path('nov_unpaid_rent_ob_ch1/', branch1.nov_unpaid_rent_ob_ch1, name='nov_unpaid_rent_ob_ch1'),
    path('table_nov_unpaid_rent_ob_ch1/', branch1.table_nov_unpaid_rent_ob_ch1, name='table_nov_unpaid_rent_ob_ch1'),
    path('dec_unpaid_rent_ob_ch1/', branch1.dec_unpaid_rent_ob_ch1, name='dec_unpaid_rent_ob_ch1'),
    path('table_dec_unpaid_rent_ob_ch1/', branch1.table_dec_unpaid_rent_ob_ch1, name='table_dec_unpaid_rent_ob_ch1'),

    path('details_of_unpaid_guests_ob_ch1/<id>',branch1.details_of_unpaid_guests_ob_ch1,name='details_of_unpaid_guests_ob_ch1'),

#unpaid rent end here

#paid rent start here

    path('paid_rent_choose_months_ob_ch1/',branch1.paid_rent_choose_months_ob_ch1,name='paid_rent_choose_months_ob_ch1'),
    path('partially_paid_guest_choose_months_ob_ch1/',reports1.partially_paid_guest_choose_months_ob_ch1,name='partially_paid_guest_choose_months_ob_ch1'),

    path('jan_paid_rent_ob_ch1/', branch1.jan_paid_rent_ob_ch1, name='jan_paid_rent_ob_ch1'),
    path('table_jan_paid_rent_ob_ch1/', branch1.table_jan_paid_rent_ob_ch1, name='table_jan_paid_rent_ob_ch1'),
    path('jan_full_paid_guest_ob_ch1/', reports1.jan_full_paid_guest_ob_ch1, name='jan_full_paid_guest_ob_ch1'),
    path('jan_partially_paid_guest_ob_ch1/', reports1.jan_partially_paid_guest_ob_ch1, name='jan_partially_paid_guest_ob_ch1'),
    path('table_jan_partially_paid_guest_ob_ch1/', reports1.table_jan_partially_paid_guest_ob_ch1,name='table_jan_partially_paid_guest_ob_ch1'),

    path('feb_paid_rent_ob_ch1/', branch1.feb_paid_rent_ob_ch1, name='feb_paid_rent_ob_ch1'),
    path('table_feb_paid_rent_ob_ch1/', branch1.table_feb_paid_rent_ob_ch1, name='table_feb_paid_rent_ob_ch1'),
    path('feb_full_paid_guest_ob_ch1/', reports1.feb_full_paid_guest_ob_ch1, name='feb_full_paid_guest_ob_ch1'),
    path('feb_partially_paid_guest_ob_ch1/', reports1.feb_partially_paid_guest_ob_ch1, name='feb_partially_paid_guest_ob_ch1'),
    path('table_feb_partially_paid_guest_ob_ch1/', reports1.table_feb_partially_paid_guest_ob_ch1,name='table_feb_partially_paid_guest_ob_ch1'),

    path('mar_paid_rent_ob_ch1/', branch1.mar_paid_rent_ob_ch1, name='mar_paid_rent_ob_ch1'),
    path('table_mar_paid_rent_ob_ch1/', branch1.table_mar_paid_rent_ob_ch1, name='table_mar_paid_rent_ob_ch1'),
    path('march_full_paid_guest_ob_ch1/', reports1.march_full_paid_guest_ob_ch1, name='march_full_paid_guest_ob_ch1'),
    path('march_partially_paid_guest_ob_ch1/', reports1.march_partially_paid_guest_ob_ch1, name='march_partially_paid_guest_ob_ch1'),
    path('table_march_partially_paid_guest_ob_ch1/', reports1.table_march_partially_paid_guest_ob_ch1,name='table_march_partially_paid_guest_ob_ch1'),

    path('april_paid_rent_ob_ch1/', branch1.april_paid_rent_ob_ch1, name='april_paid_rent_ob_ch1'),
    path('table_april_paid_rent_ob_ch1/', branch1.table_april_paid_rent_ob_ch1, name='table_april_paid_rent_ob_ch1'),
    path('april_full_paid_guest_ob_ch1/', reports1.april_full_paid_guest_ob_ch1, name='april_full_paid_guest_ob_ch1'),
    path('april_partially_paid_guest_ob_ch1/', reports1.april_partially_paid_guest_ob_ch1, name='april_partially_paid_guest_ob_ch1'),
    path('table_april_partially_paid_guest_ob_ch1/', reports1.table_april_partially_paid_guest_ob_ch1,name='table_april_partially_paid_guest_ob_ch1'),

    path('may_paid_rent_ob_ch1/', branch1.may_paid_rent_ob_ch1, name='may_paid_rent_ob_ch1'),
    path('table_may_paid_rent_ob_ch1/', branch1.table_may_paid_rent_ob_ch1, name='table_may_paid_rent_ob_ch1'),
    path('may_full_paid_guest_ob_ch1/', reports1.may_full_paid_guest_ob_ch1, name='may_full_paid_guest_ob_ch1'),
    path('may_partially_paid_guest_ob_ch1/', reports1.may_partially_paid_guest_ob_ch1, name='may_partially_paid_guest_ob_ch1'),
    path('table_may_partially_paid_guest_ob_ch1/', reports1.table_may_partially_paid_guest_ob_ch1, name='table_may_partially_paid_guest_ob_ch1'),

    path('june_paid_rent_ob_ch1/', branch1.june_paid_rent_ob_ch1, name='june_paid_rent_ob_ch1'),
    path('table_june_paid_rent_ob_ch1/', branch1.table_june_paid_rent_ob_ch1, name='table_june_paid_rent_ob_ch1'),
    path('june_full_paid_guest_ob_ch1/', reports1.june_full_paid_guest_ob_ch1, name='june_full_paid_guest_ob_ch1'),
    path('june_partially_paid_guest_ob_ch1/', reports1.june_partially_paid_guest_ob_ch1, name='june_partially_paid_guest_ob_ch1'),
    path('table_june_partially_paid_guest_ob_ch1/', reports1.table_june_partially_paid_guest_ob_ch1, name='table_june_partially_paid_guest_ob_ch1'),

    path('july_paid_rent_ob_ch1/', branch1.july_paid_rent_ob_ch1, name='july_paid_rent_ob_ch1'),
    path('table_july_paid_rent_ob_ch1/', branch1.table_july_paid_rent_ob_ch1, name='table_july_paid_rent_ob_ch1'),
    path('july_full_paid_guest_ob_ch1/', reports1.july_full_paid_guest_ob_ch1, name='july_full_paid_guest_ob_ch1'),
    path('july_partially_paid_guest_ob_ch1/', reports1.july_partially_paid_guest_ob_ch1, name='july_partially_paid_guest_ob_ch1'),
    path('table_july_partially_paid_guest_ob_ch1/', reports1.table_july_partially_paid_guest_ob_ch1, name='table_july_partially_paid_guest_ob_ch1'),

    path('aug_paid_rent_ob_ch1/', branch1.aug_paid_rent_ob_ch1, name='aug_paid_rent_ob_ch1'),
    path('table_aug_paid_rent_ob_ch1/', branch1.table_aug_paid_rent_ob_ch1, name='table_aug_paid_rent_ob_ch1'),
    path('auguest_full_paid_guest_ob_ch1/', reports1.auguest_full_paid_guest_ob_ch1, name='auguest_full_paid_guest_ob_ch1'),
    path('auguest_partially_paid_guest_ob_ch1/', reports1.auguest_partially_paid_guest_ob_ch1,name='auguest_partially_paid_guest_ob_ch1'),
    path('table_auguest_partially_paid_guest_ob_ch1/', reports1.table_auguest_partially_paid_guest_ob_ch1,name='table_auguest_partially_paid_guest_ob_ch1'),

    path('sept_paid_rent_ob_ch1/', branch1.sept_paid_rent_ob_ch1, name='sept_paid_rent_ob_ch1'),
    path('table_sept_paid_rent_ob_ch1/', branch1.table_sept_paid_rent_ob_ch1, name='table_sept_paid_rent_ob_ch1'),
    path('sept_full_paid_guest_ob_ch1/', reports1.sept_full_paid_guest_ob_ch1, name='sept_full_paid_guest_ob_ch1'),
    path('sept_partially_paid_guest_ob_ch1/', reports1.sept_partially_paid_guest_ob_ch1, name='sept_partially_paid_guest_ob_ch1'),
    path('table_sept_partially_paid_guest_ob_ch1/', reports1.table_sept_partially_paid_guest_ob_ch1,name='table_sept_partially_paid_guest_ob_ch1'),

    path('oct_paid_rent_ob_ch1/', branch1.oct_paid_rent_ob_ch1, name='oct_paid_rent_ob_ch1'),
    path('table_oct_paid_rent_ob_ch1/', branch1.table_oct_paid_rent_ob_ch1, name='table_oct_paid_rent_ob_ch1'),
    path('october_full_paid_guest_ob_ch1/', reports1.october_full_paid_guest_ob_ch1, name='october_full_paid_guest_ob_ch1'),
    path('october_partially_paid_guest_ob_ch1/', reports1.october_partially_paid_guest_ob_ch1,name='october_partially_paid_guest_ob_ch1'),
    path('table_october_partially_paid_guest_ob_ch1/', reports1.table_october_partially_paid_guest_ob_ch1,name='table_october_partially_paid_guest_ob_ch1'),

    path('nov_paid_rent_ob_ch1/', branch1.nov_paid_rent_ob_ch1, name='nov_paid_rent_ob_ch1'),
    path('table_nov_paid_rent_ob_ch1/', branch1.table_nov_paid_rent_ob_ch1, name='table_nov_paid_rent_ob_ch1'),
    path('nov_full_paid_guest_ob_ch1/', reports1.nov_full_paid_guest_ob_ch1, name='nov_full_paid_guest_ob_ch1'),
    path('nov_partially_paid_guest_ob_ch1/', reports1.nov_partially_paid_guest_ob_ch1, name='nov_partially_paid_guest_ob_ch1'),
    path('table_nov_partially_paid_guest_ob_ch1/', reports1.table_nov_partially_paid_guest_ob_ch1,name='table_nov_partially_paid_guest_ob_ch1'),

    path('dec_paid_rent_ob_ch1/', branch1.dec_paid_rent_ob_ch1, name='dec_paid_rent_ob_ch1'),
    path('table_dec_paid_rent_ob_ch1/', branch1.table_dec_paid_rent_ob_ch1, name='table_dec_paid_rent_ob_ch1'),
    path('dec_full_paid_guest_ob_ch1/', reports1.dec_full_paid_guest_ob_ch1, name='dec_full_paid_guest_ob_ch1'),
    path('dec_partially_paid_guest_ob_ch1/', reports1.dec_partially_paid_guest_ob_ch1, name='dec_partially_paid_guest_ob_ch1'),
    path('table_dec_partially_paid_guest_ob_ch1/', reports1.table_dec_partially_paid_guest_ob_ch1,name='table_dec_partially_paid_guest_ob_ch1'),

    path('details_of_paid_guests_ob_ch1/<id>',branch1.details_of_paid_guests_ob_ch1,name='details_of_paid_guests_ob_ch1'),
    path('full_paid_guest_ob_ch1/',reports1.full_paid_guest_ob_ch1,name='full_paid_guest_ob_ch1'),

#paid rent end here

#*********reports end here


##################################
#VACATE GUEST DETAILS START HERE
################################

    path('viewall_vacate_guest_ob_ch1/',branch1.viewall_vacate_guest_ob_ch1,name='viewall_vacate_guest_ob_ch1'),
    path('details_of_vacate_guest_ob_ch1/<id>',branch1.details_of_vacate_guest_ob_ch1,name='details_of_vacate_guest_ob_ch1'),
    path('full_vacated_guest_details_ob_ch1',branch1.full_vacated_guest_details_ob_ch1,name='full_vacated_guest_details_ob_ch1'),
    path('full_vacated_guest_table_ob_ch1',branch1.full_vacated_guest_table_ob_ch1,name='full_vacated_guest_table_ob_ch1'),

#********vacate guest payments start here**********

    path('jan_manke_payments_vacate_ob_ch1/<id>', branch1.jan_manke_payments_vacate_ob_ch1, name='jan_manke_payments_vacate_ob_ch1'),
    path('feb_manke_payments_vacate_ob_ch1/<id>', branch1.feb_manke_payments_vacate_ob_ch1, name='feb_manke_payments_vacate_ob_ch1'),
    path('march_manke_payments_vacate_ob_ch1/<id>', branch1.march_manke_payments_vacate_ob_ch1, name='march_manke_payments_vacate_ob_ch1'),
    path('april_make_payments_vacate_ob_ch1/<id>', branch1.april_make_payments_vacate_ob_ch1, name='april_make_payments_vacate_ob_ch1'),

    path('may_make_payments_vacate_ob_ch1/<id>', branch1.may_make_payments_vacate_ob_ch1, name='may_make_payments_vacate_ob_ch1'),
    path('june_make_payments_vacate_ob_ch1/<id>', branch1.june_make_payments_vacate_ob_ch1, name='june_make_payments_vacate_ob_ch1'),
    path('july_make_payments_vacate_ob_ch1/<id>', branch1.july_make_payments_vacate_ob_ch1, name='july_make_payments_vacate_ob_ch1'),
    path('aug_make_payments_vacate_ob_ch1/<id>', branch1.aug_make_payments_vacate_ob_ch1, name='aug_make_payments_vacate_ob_ch1'),

    path('sept_make_payments_vacate_ob_ch1/<id>', branch1.sept_make_payments_vacate_ob_ch1, name='sept_make_payments_vacate_ob_ch1'),
    path('oct_make_payments_vacate_ob_ch1/<id>', branch1.oct_make_payments_vacate_ob_ch1, name='oct_make_payments_vacate_ob_ch1'),
    path('nov_make_payments_vacate_ob_ch1/<id>', branch1.nov_make_payments_vacate_ob_ch1, name='nov_make_payments_vacate_ob_ch1'),
    path('dec_make_payments_vacate_ob_ch1/<id>', branch1.dec_make_payments_vacate_ob_ch1, name='dec_make_payments_vacate_ob_ch1'),

#********vacate guest payments end here**********

##################################
#VACATE GUEST DETAILS END HERE
################################


##################################
#PRINT OUTS START HERE
################################

    path('detail_guest_general_ob_ch1/',branch1.detail_guest_general_ob_ch1,name='detail_guest_general_ob_ch1'),

    path('jan_print_ob_ch1/',branch1.jan_print_ob_ch1,name='jan_print_ob_ch1'),
    path('feb_print_ob_ch1/',branch1.feb_print_ob_ch1,name='feb_print_ob_ch1'),
    path('march_print_ob_ch1/',branch1.march_print_ob_ch1,name='march_print_ob_ch1'),
    path('april_print_ob_ch1/',branch1.april_print_ob_ch1,name='april_print_ob_ch1'),

    path('may_print_ob_ch1/',branch1.may_print_ob_ch1,name='may_print_ob_ch1'),
    path('june_print_ob_ch1/',branch1.june_print_ob_ch1,name='june_print_ob_ch1'),
    path('july_print_ob_ch1/', branch1.july_print_ob_ch1, name='july_print_ob_ch1'),
    path('aug_print_ob_ch1/', branch1.aug_print_ob_ch1, name='aug_print_ob_ch1'),

    path('sept_print_ob_ch1/', branch1.sept_print_ob_ch1, name='sept_print_ob_ch1'),
    path('oct_print_ob_ch1/', branch1.oct_print_ob_ch1, name='oct_print_ob_ch1'),
    path('nov_print_ob_ch1/', branch1.nov_print_ob_ch1, name='nov_print_ob_ch1'),
    path('dec_print_ob_ch1/', branch1.dec_print_ob_ch1, name='dec_print_ob_ch1'),

    path('new_year_jan_print_ob_ch1/', branch1.new_year_jan_print_ob_ch1, name='new_year_jan_print_ob_ch1'),

##################################
#PRINT OUTS END HERE
################################

    path('jan_close_ob_ch1/', branch1.jan_close_ob_ch1, name='jan_close_ob_ch1'),
    path('jan_close_decision_page_ob_ch1/', branch1.jan_close_decision_page_ob_ch1, name='jan_close_decision_page_ob_ch1'),
    path('feb_close/', branch1.feb_close_ob_ch1, name='feb_close_ob_ch1'),
    path('feb_close_decision_page_ob_ch1/', branch1.feb_close_decision_page_ob_ch1, name='feb_close_decision_page_ob_ch1'),
    path('mar_close_ob_ch1/', branch1.mar_close_ob_ch1, name='mar_close_ob_ch1'),
    path('mar_close_decision_page/', branch1.mar_close_decision_page_ob_ch1, name='mar_close_decision_page_ob_ch1'),
    path('apr_close_ob_ch1/', branch1.apr_close_ob_ch1, name='apr_close_ob_ch1'),
    path('apr_close_decision_page_ob_ch1/', branch1.apr_close_decision_page_ob_ch1, name='apr_close_decision_page_ob_ch1'),

    path('may_close_ob_ch1/', branch1.may_close_ob_ch1, name='may_close_ob_ch1'),
    path('may_close_decision_page_ob_ch1/', branch1.may_close_decision_page_ob_ch1, name='may_close_decision_page_ob_ch1'),
    path('jun_close_ob_ch1/', branch1.jun_close_ob_ch1, name='jun_close_ob_ch1'),
    path('jun_close_decision_page_ob_ch1/', branch1.jun_close_decision_page_ob_ch1, name='jun_close_decision_page_ob_ch1'),
    path('jul_close_ob_ch1/', branch1.jul_close_ob_ch1, name='jul_close_ob_ch1'),
    path('jul_close_decision_page_ob_ch1/', branch1.jul_close_decision_page_ob_ch1, name='jul_close_decision_page_ob_ch1'),
    path('aug_close_ob_ch1/', branch1.aug_close_ob_ch1, name='aug_close_ob_ch1'),
    path('aug_close_decision_page_ob_ch1/', branch1.aug_close_decision_page_ob_ch1, name='aug_close_decision_page_ob_ch1'),

    path('sep_close_ob_ch1/', branch1.sep_close_ob_ch1, name='sep_close_ob_ch1'),
    path('sep_close_decision_page_ob_ch1/', branch1.sep_close_decision_page_ob_ch1, name='sep_close_decision_page_ob_ch1'),
    path('oct_close_ob_ch1/', branch1.oct_close_ob_ch1, name='oct_close_ob_ch1'),
    path('oct_close_decision_page_ob_ch1/', branch1.oct_close_decision_page_ob_ch1, name='oct_close_decision_page_ob_ch1'),
    path('nov_close_ob_ch1/', branch1.nov_close_ob_ch1, name='nov_close_ob_ch1'),
    path('nov_close_decision_page_ob_ch1/', branch1.nov_close_decision_page_ob_ch1, name='nov_close_decision_page_ob_ch1'),


########################################
# DETAILED REPORT START HERE
###########################

    path('detailed_report_choose_months_ob_ch1/',reports1.detailed_report_choose_months_ob_ch1,name='detailed_report_choose_months_ob_ch1'),

    path('jan_details_live_ob_ch1/', reports1.jan_details_live_ob_ch1, name='jan_details_live_ob_ch1'),
    path('jan_print_live_ob_ch1/', reports1.jan_print_live_ob_ch1, name='jan_print_live_ob_ch1'),
    path('feb_details_live_ob_ch1/', reports1.feb_details_live_ob_ch1, name='feb_details_live_ob_ch1'),
    path('feb_print_live_ob_ch1/', reports1.feb_print_live_ob_ch1, name='feb_print_live_ob_ch1'),
    path('march_details_live_ob_ch1/', reports1.march_details_live_ob_ch1, name='march_details_live_ob_ch1'),
    path('march_print_live_ob_ch1/', reports1.march_print_live_ob_ch1, name='march_print_live_ob_ch1'),

    path('april_details_live_ob_ch1/', reports1.april_details_live_ob_ch1, name='april_details_live_ob_ch1'),
    path('april_print_live_ob_ch1/', reports1.april_print_live_ob_ch1, name='april_print_live_ob_ch1'),
    path('may_details_live_ob_ch1/', reports1.may_details_live_ob_ch1, name='may_details_live_ob_ch1'),
    path('may_print_live_ob_ch1/', reports1.may_print_live_ob_ch1, name='may_print_live_ob_ch1'),
    path('june_details_live_ob_ch1/',reports1.june_details_live_ob_ch1,name='june_details_live_ob_ch1'),
    path('june_print_live_ob_ch1/', reports1.june_print_live_ob_ch1, name='june_print_live_ob_ch1'),

    path('july_details_live_ob_ch1/', reports1.july_details_live_ob_ch1, name='july_details_live_ob_ch1'),
    path('july_print_live_ob_ch1/', reports1.july_print_live_ob_ch1, name='july_print_live_ob_ch1'),
    path('auguest_details_live_ob_ch1/', reports1.auguest_details_live_ob_ch1, name='auguest_details_live_ob_ch1'),
    path('auguest_print_live_ob_ch1/', reports1.auguest_print_live_ob_ch1, name='auguest_print_live_ob_ch1'),
    path('sept_details_live_ob_ch1/', reports1.sept_details_live_ob_ch1, name='sept_details_live_ob_ch1'),
    path('sept_print_live_ob_ch1/', reports1.sept_print_live_ob_ch1, name='sept_print_live_ob_ch1'),

    path('october_details_live_ob_ch1/', reports1.october_details_live_ob_ch1, name='october_details_live_ob_ch1'),
    path('october_print_live_ob_ch1/', reports1.october_print_live_ob_ch1, name='october_print_live_ob_ch1'),
    path('nov_details_live_ob_ch1/', reports1.nov_details_live_ob_ch1, name='nov_details_live_ob_ch1'),
    path('nov_print_live_ob_ch1/', reports1.nov_print_live_ob_ch1, name='nov_print_live_ob_ch1'),
    path('dec_details_live_ob_ch1/', reports1.dec_details_live_ob_ch1, name='dec_details_live_ob_ch1'),
    path('dec_print_live_ob_ch1/', reports1.dec_print_live_ob_ch1, name='dec_print_live_ob_ch1'),

########################################
#  DETAILED REPORT END HERE
###########################

    path('viewall_vaccant_room_ob_ch1/', reports1.viewall_vaccant_room_ob_ch1, name='viewall_vaccant_room_ob_ch1'),

    path('d_ob_ch1/', branch1.dynamic, name='dynamic'),

    path('manage_bed_ob_ch1/', branch1.manage_bed_ob_ch1, name='manage_bed_ob_ch1'),
    path('manage_new_guest_ob_ch1/', branch1.manage_new_guest_ob_ch1, name='manage_new_guest_ob_ch1'),
    path('manage_update_new_guest_ob_ch1/<id>', branch1.manage_update_new_guest_ob_ch1, name='manage_update_new_guest_ob_ch1'),
    path('manage_update_beds_ob_ch1/<id>', branch1.manage_update_beds_ob_ch1, name='manage_update_beds_ob_ch1'),




########################################
# DUE AMT MANAGEMENT START HERE
###########################

    path('view_all_due_amt_ob_ch1/', branch1.view_all_due_amt_ob_ch1, name='view_all_due_amt_ob_ch1'),
    path('due_amt_mgt_choose_months_ob_ch1/', branch1.due_amt_mgt_choose_months_ob_ch1, name='due_amt_mgt_choose_months_ob_ch1'),

    path('view_jan_account_details_ob_ch1/', branch1.view_jan_account_details_ob_ch1, name='view_jan_account_details_ob_ch1'),
    path('jan_account_mgt_ob_ch1/<id>',branch1.jan_account_mgt_ob_ch1,name='jan_account_mgt_ob_ch1'),
    path('view_feb_account_details_ob_ch1/', branch1.view_feb_account_details_ob_ch1, name='view_feb_account_details_ob_ch1'),
    path('feb_account_mgt_ob_ch1/<id>',branch1.feb_account_mgt_ob_ch1,name='feb_account_mgt_ob_ch1'),
    path('view_march_account_details_ob_ch1/', branch1.view_march_account_details_ob_ch1, name='view_march_account_details_ob_ch1'),
    path('march_account_mgt_ob_ch1/<id>',branch1.march_account_mgt_ob_ch1,name='march_account_mgt_ob_ch1'),
    path('view_april_account_details_ob_ch1/', branch1.view_april_account_details_ob_ch1, name='view_april_account_details_ob_ch1'),
    path('april_account_mgt_ob_ch1/<id>',branch1.april_account_mgt_ob_ch1,name='april_account_mgt_ob_ch1'),

    path('view_may_account_details_ob_ch1/',branch1.view_may_account_details_ob_ch1,name='view_may_account_details_ob_ch1'),
    path('may_account_mgt_ob_ch1/<id>', branch1.may_account_mgt_ob_ch1, name='may_account_mgt_ob_ch1'),
    path('view_june_account_details_ob_ch1/', branch1.view_june_account_details_ob_ch1, name='view_june_account_details_ob_ch1'),
    path('june_account_mgt_ob_ch1/<id>',branch1.june_account_mgt_ob_ch1,name='june_account_mgt_ob_ch1'),
    path('view_july_account_details_ob_ch1/', branch1.view_july_account_details_ob_ch1, name='view_july_account_details_ob_ch1'),
    path('july_account_mgt_ob_ch1/<id>',branch1.july_account_mgt_ob_ch1,name='july_account_mgt_ob_ch1'),
    path('view_auguest_account_details_ob_ch1/', branch1.view_auguest_account_details_ob_ch1, name='view_auguest_account_details_ob_ch1'),
    path('auguest_account_mgt_ob_ch1/<id>',branch1.auguest_account_mgt_ob_ch1,name='auguest_account_mgt_ob_ch1'),

    path('view_sept_account_details_ob_ch1/', branch1.view_sept_account_details_ob_ch1, name='view_sept_account_details_ob_ch1'),
    path('sept_account_mgt_ob_ch1/<id>',branch1.sept_account_mgt_ob_ch1,name='sept_account_mgt_ob_ch1'),
    path('view_october_account_details_ob_ch1/', branch1.view_october_account_details_ob_ch1, name='view_october_account_details_ob_ch1'),
    path('october_account_mgt_ob_ch1/<id>',branch1.october_account_mgt_ob_ch1,name='october_account_mgt_ob_ch1'),
    path('view_nov_account_details_ob_ch1/', branch1.view_nov_account_details_ob_ch1, name='view_nov_account_details_ob_ch1'),
    path('nov_account_mgt_ob_ch1/<id>',branch1.nov_account_mgt_ob_ch1,name='nov_account_mgt_ob_ch1'),
    path('view_dec_account_details_ob_ch1/', branch1.view_dec_account_details_ob_ch1, name='view_dec_account_details_ob_ch1'),
    path('dec_account_mgt_ob_ch1/<id>',branch1.dec_account_mgt_ob_ch1,name='dec_account_mgt_ob_ch1'),

########################################
# DUE AMT MANAGEMENT END HERE
###########################

########################################
# DASHBOARD REPORTS START HERE
###########################

    path('monthly_details_due_ob_ch1', admin_dashboard_calculations_br1.monthly_details_due_ob_ch1, name='monthly_details_due_ob_ch1'),
    path('monthly_collection_details_ob_ch1/', admin_dashboard_calculations_br1.monthly_collection_details_ob_ch1, name='monthly_collection_details_ob_ch1'),

########################################
# DASHBOARD REPORTS END HERE
###########################

    path('guest_all_ob_ch1/',branch1.guest_all_ob_ch1,name='guest_all_ob_ch1'),





#####********************************************************************************************************
#ACCOUNTS START HERE
####***************************************************


#########################################################
###******CREATER MASTER START HERE
###################################################################################


##******************CATERGORY CREATER START HERE

    path('view_all_category1/', accounts1.view_all_category1, name='view_all_category1'),
    path('create_new_category1/', accounts1.create_new_category1, name='create_new_category1'),
    path('regi_new_category1/', accounts1.regi_new_category1, name='regi_new_category1'),
    path('update_category1/<id>',accounts1.update_category1,name='update_category1'),

    path('delete_category1/<id>', accounts1.delete_category1, name='delete_category1'),
    path('view_all_category_delete1/', accounts1.view_all_category_delete1, name='view_all_category_delete1'),

    path('regi_multiple_new_category1/', accounts1.regi_multiple_new_category1, name='regi_multiple_new_category1'),

    ##*****************CATERY CREATER END HERE


##******************ITEM CREATER START HERE

    path('view_all_items1/', accounts1.view_all_items1, name='view_all_items1'),
    path('create_new_item1/', accounts1.create_new_item1, name='create_new_item1'),
    path('regi_new_item1/', accounts1.regi_new_item1, name='regi_new_item1'),
    path('delete_item1/<id>',accounts1.delete_item1,name='delete_item1'),
    path('update_item1/<id>', accounts1.update_item1, name='update_item1'),
    path('view_all_items_delete1/',accounts1.view_all_items_delete1,name='view_all_items_delete1'),

    path('regi_multiple_new_item1/', accounts1.regi_multiple_new_item1, name='regi_multiple_new_item1'),

    ##*****************ITEM CREATER END HERE


##******************LEDGER CREATER START HERE

    path('view_all_ledger1/', accounts1.view_all_ledger1, name='view_all_ledger1'),
    path('create_new_ledger1/', accounts1.create_new_ledger1, name='create_new_ledger1'),
    path('regi_new_ledger1/', accounts1.regi_new_ledger1, name='regi_new_ledger1'),
    path('delete_ledger1/<id>',accounts1.delete_ledger1,name='delete_ledger1'),
    path('update_ledger1/<id>',accounts1.update_ledger1,name='update_ledger1'),
    path('view_all_ledger_delete1/',accounts1.view_all_ledger_delete1,name='view_all_ledger_delete1'),

    path('regi_multiple_new_ledger1/',accounts1.regi_multiple_new_ledger1,name='regi_multiple_new_ledger1'),

##*****************LEDGER CREATER END HERE


##******************ACCOUNTS_BOOK CREATER START HERE

    path('view_all_accounts_book1/', accounts1.view_all_accounts_book1, name='view_all_accounts_book1'),
    path('create_new_accounts_book1/', accounts1.create_new_accounts_book1, name='create_new_accounts_book1'),
    path('regi_new_accounts_book1/', accounts1.regi_new_accounts_book1, name='regi_new_accounts_book1'),
    path('update_accounts_book1/<id>',accounts1.update_accounts_book1,name='update_accounts_book1'),
    path('delete_accounts_book1/<id>',accounts1.delete_accounts_book1,name='delete_accounts_book1'),
    path('view_all_accounts_book_delete1/',accounts1.view_all_accounts_book_delete1,name='view_all_accounts_book_delete1'),

    path('regi_multiple_new_accounts_book1/',accounts1.regi_multiple_new_accounts_book1,name='regi_multiple_new_accounts_book1'),

##*****************ACCOUNTS_BOOK CREATER END HERE


#########################################################
###******CREATER MASTER END HERE
###################################################################################

#########################################################
###******INCOME EXPENSE ENTRY FORM MASTER START HERE
###################################################################################

    path('get_countries1/', accounts1.get_countries1, name='get_countries1'),

    path('in_exp_items_entry1/', accounts1.in_exp_items_entry1, name='in_exp_items_entry1'),
    path('reg_in_exp_items_entry1/', accounts1.reg_in_exp_items_entry1, name='reg_in_exp_items_entry1'),
    path('delete_journal1/<id>',accounts1.delete_journal1,name='delete_journal1'),
    path('update_in_exp_items_entry1/<id>',accounts1.update_in_exp_items_entry1,name='update_in_exp_items_entry1'),
    path('detailed_journal_report1/',accounts1.detailed_journal_report1,name='detailed_journal_report1'),
    path('journal_report_deleted1/',accounts1.journal_report_deleted1,name='journal_report_deleted1'),

#########################################################
###******INCOME EXPENSE ENTRY FORM MASTER END HERE
###################################################################################
#########*******************************************************************************************************************
#########################################################
###******ALL REPORTS  START HERE
###################################################################################


###************* CATEGORY WISE REPORTS  START HERE

    path('daily_category_wise1/', accounts1.daily_category_wise1, name='daily_category_wise1'),
    path('monthly_category_based_reports1/',accounts1.monthly_category_based_reports1,name='monthly_category_based_reports1'),
    path('yearly_category_based_reports1/', accounts1.yearly_category_based_reports1,name='yearly_category_based_reports1'),


###*************CATEGORY WISE REPORTS  END HERE

###*************DAILY DETAILED REPORTS  START HERE

    path('daily_detailed1/', accounts1.daily_detailed1, name='daily_detailed1'),
    path('monthly_detailed1/',accounts1.monthly_detailed1,name='monthly_detailed1'),
    path('yearly_detailed1/',accounts1.yearly_detailed1,name='yearly_detailed1'),

###*************DAILY DETAILED REPORTS  START HERE

###*************ITEM BASED REPORTS  START HERE

    path('item_based_reports1/', accounts1.item_based_reports1, name='item_based_reports1'),
    path('daily_item_based_reports1/',accounts1.daily_item_based_reports1,name='daily_item_based_reports1'),
    path('monthly_item_based_reports1/',accounts1.monthly_item_based_reports1,name='monthly_item_based_reports1'),

###*************ITEM BASED REPORTS  START HERE

###*************LEDGER BASED REPORTS  START HERE

    path('ledger_based_reports1/', accounts1.ledger_based_reports1, name='ledger_based_reports1'),
    path('monthly_ledger_based_reports1/', accounts1.monthly_ledger_based_reports1, name='monthly_ledger_based_reports1'),
    path('daily_ledger_based_reports1/',accounts1.daily_ledger_based_reports1,name='daily_ledger_based_reports1'),

###*************LEDGER BASED REPORTS  START HERE

###*************ACCOUNTS-BOOK BASED REPORTS  START HERE

    path('accounts_book_based_reports1/', accounts1.accounts_book_based_reports1, name='accounts_book_based_reports1'),
    path('daily_accounts_book_based_reports1/',accounts1.daily_accounts_book_based_reports1,name='daily_accounts_book_based_reports1'),
    path('monthly_accounts_book_based_reports1/',accounts1.monthly_accounts_book_based_reports1,name='monthly_accounts_book_based_reports1'),

###*************ACCOUNTS-BOOK BASED REPORTS  END HERE



#########################################################
###******ALL REPORTS  END HERE
###################################################################################

    path('monthly_reports_choose_months1/', accounts1.monthly_reports_choose_months1, name='monthly_reports_choose_months1'),
    path('monthly_detailed_daily_in_exp_items_report1/<mo>',accounts1.monthly_detailed_daily_in_exp_items_report1,name='monthly_detailed_daily_in_exp_items_report1'),

    path('single_monthly_reports_choose_months1/', accounts1.single_monthly_reports_choose_months1,name='single_monthly_reports_choose_months1'),
    path('single_monthly_daily_in_exp_items_report1/<mo>',accounts1.single_monthly_daily_in_exp_items_report1,name='single_monthly_daily_in_exp_items_report1'),

    path('accounts_dash_board_ob_ch1/',accounts1.accounts_dash_board_ob_ch1,name='accounts_dash_board_ob_ch1'),
    path('accounts_dash_board1/',accounts1.accounts_dash_board1,name='accounts_dash_board1'),

    path('profit_sharing_choose_months1', accounts1.profit_sharing_choose_months1,name='profit_sharing_choose_months1'),
    path('profit_sharing1/<mo>', accounts1.profit_sharing1, name='profit_sharing1'),
    path('view_share_holders1', accounts1.view_share_holders1, name='view_share_holders1'),
    path('create_share_holders1', accounts1.create_share_holders1, name='create_share_holders1'),
    path('regi_share_holders1', accounts1.regi_share_holders1, name='regi_share_holders1'),
    path('update_share_holders1/<id>', accounts1.update_share_holders1, name='update_share_holders1'),
    path('delete_share_holders1/<id>', accounts1.delete_share_holders1, name='delete_share_holders1'),
    path('view_deleted_share_holders1', accounts1.view_deleted_share_holders1, name='view_deleted_share_holders1'),

    path('regi_multiple_share_holders1', accounts1.regi_multiple_share_holders1,name='regi_multiple_share_holders1'),


    #############BRANCH SETTINGS START HERE ########################

    path('guest_rent_update_ob_ch1/',branch_settings1.guest_rent_update_ob_ch1,name='guest_rent_update_ob_ch1'),

    ############BRANCH SETTINGS END HERE ############################


]

