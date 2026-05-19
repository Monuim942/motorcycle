import urllib.parse  # [إضافة]: لتجهيز رسالة الواتساب وتشفير الرموز
from datetime import date, datetime, timedelta
from django.shortcuts import redirect, render  # [تعديل]: إضافة redirect لتوجيه المستخدم للواتساب

from .models import Admin, DateTime, User


def page1(request):
    x = Admin.objects.all()
    return render(request, 'pages/page1.html', {
        'x': x
    })


def Reservation(request):
    message = ''

    if request.method == 'POST':
        T_C = request.POST.get('trip_destination')
        F_N = request.POST.get('first_name')
        L_N = request.POST.get('last_name')
        PH_N = request.POST.get('phone')
        DATE = request.POST.get('date')
        TIME = request.POST.get('time')
        NO_T = request.POST.get('notes')

        if not F_N.replace(' ', '').isalpha():
            message = 'الإسم الأول لا يجب أن يحتوي على أرقام ❌'

        elif not L_N.replace(' ', '').isalpha():
            message = 'الإسم الأخير لا يجب أن يحتوي على أرقام ❌'

        elif not PH_N.isdigit():
            message = 'رقم الهاتف يجب أن يحتوي على أرقام فقط ❌'

        elif len(PH_N) != 10:
            message = 'رقم الهاتف يجب أن يحتوي على 10 أرقام ❌'

        else:
            today = date.today()
            selected_date = datetime.strptime(DATE, "%Y-%m-%d").date()

            if selected_date < today:
                message = "لا يمكنك اختيار تاريخ قديم ❌"

            elif selected_date == today:
                current_time = datetime.now().time()
                selected_time = datetime.strptime(TIME, "%H:%M").time()

                if selected_time < current_time:
                    message = "هذا الوقت قد مر ❌"

            if not message:
                if DateTime.objects.filter(date=DATE, time=TIME).exists():
                    message = "هذا الوقت محجوز من قبل ❌"
                else:
                    chosen_time_str = f"{DATE} {TIME}"
                    chosen_dt = datetime.strptime(chosen_time_str, "%Y-%m-%d %H:%M")

                    existing_bookings = DateTime.objects.filter(date=DATE)
                    conflict = False

                    for booking in existing_bookings:
                        existing_dt = datetime.combine(booking.date, booking.time)
                        diff = abs(chosen_dt - existing_dt)

                        if diff < timedelta(hours=2):
                            conflict = True
                            break

                    if conflict:
                        message = "هناك حجز قريب من هذا الوقت ❌"
                    else:
                        try:
                            dt = DateTime.objects.create(
                                date=DATE,
                                time=TIME
                            )

                            new_user = User(
                                select_your_trip=T_C,
                                first_name=F_N,
                                last_name=L_N,
                                phone_number=PH_N,
                                datetime=dt,
                                special_requests=NO_T,
                            )
                            new_user.save()

                            whatsapp_msg = f"""*تأكيد حجز جديد - MOTO RAGE* 🏍️💨
---------------------------------------
👤 *الاسم الكامل:* {F_N} {L_N}
📍 *الوجهة المحددة:* {T_C}
📅 *التاريخ:* {DATE}
⏰ *التوقيت:* {TIME}
📞 *رقم الهاتف:* {PH_N}
📝 *ملاحظات:* {NO_T if NO_T else 'لا توجد'}
---------------------------------------
مرحباً فريق MOTO RAGE، أود تأكيد هذا الحجز لمغامرتي القادمة!"""

                            # تحويل الرسالة لصيغة ويب آمنة
                            encoded_msg = urllib.parse.quote(whatsapp_msg)
                            
                            # رقم الواتساب الخاص بك بالصيغة الدولية وبدون أصفار بالبداية
                            your_whatsapp_number = "212699441179" 
                            
                            whatsapp_url = f"https://api.whatsapp.com/send?phone={your_whatsapp_number}&text={encoded_msg}"
                            
                            # توجيه تلقائي مباشر وسلس إلى شات الواتساب
                            return redirect(whatsapp_url)
                            # =============================================================

                        except Exception as e:
                            message = "حدث خطأ أثناء التسجيل ❌"

    return render(request, 'pages/Reservation.html', {
        'message': message
    })