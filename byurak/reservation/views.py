from django.shortcuts import get_object_or_404, render, redirect
from .forms import *

#TODO profile 의 pk 연결해야 함
# pk 는 profile 의 pk

def reservation_success(request):
    return render(request, 'reservation_success.html', context=None)

def reservation_create(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    service_name = profile.user.name
    service_price = profile.service_price
    
    print(service_price)


    #TODO 분기 조건 하나 추가해야 함 if request.user != Default User이면 생성 안되게
    # 호스트가 참가하는 것을 방지하기 위함
    if request.method == "POST":
        form = ReservationForm(request.POST)

        print(form.errors)

        if form.is_valid():
            reservation = form.save()
            
            reservation.service = profile
            reservation.customer = request.user
            reservation.payment_fee = profile.service_price * reservation.customer_count
            reservation.save()

            return redirect("reservation:reservation_pay_method", reservation.pk)

        else:

            ctx = {
                "form": form,
                'profile': profile,
                'service_name' : service_name,
                'service_price' : service_price
            }

            return render(request, "reservation_create.html", ctx)


    elif request.method == "GET":
        form = ReservationForm()

        ctx = {
            "form": form,
            'profile': profile,
            'service_name' : service_name,
            'service_price' : service_price
        }

        return render(request, "reservation_create.html", ctx)


def reservation_pay_method(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk)

    if request.method == 'POST':
        form = ReservationPaymentForm(request.POST, request.FILES, instance=reservation)
        if form.is_valid():
            reservation = form.save()
            reservation.is_complete = True
            reservation.save()
            return redirect('reservation:reservation_success')
    else:
        form = ReservationPaymentForm(instance=reservation)
        context = {
            'form': form,
            'reservation':reservation,
        }

    return render(request, 'reservation_pay_method.html', context=context)



#넘어오는 pk값은 hostr의 pk
#만약 request.user가 Service Provider 일때만 해당 URL에 접속하게 하려면 
#Decorator를 검색하셔서 Validation 작업을 수행하시면 됩니다. 
def reservation_host_confirm(request, pk):
    profile = Profile.objects.get(pk = pk)

    context = {
        'reservations'  : None
    }


    #만약 예약을 해둔 것이 있다면
    if Reservation.objects.filter(service = profile, is_complete = True).exists():
        reservations = Reservation.objects.filter(service = profile, is_complete=True)
        context = {
            'reservations' : reservations
        }

    return render(request, 'reservation_host_confirm.html', context= context)

#넘어오는 pk값은 customer의 pk
def reservation_customer_confirm(request):

    customer = request.user

    context = {
        "reservations" : None
    }

    if Reservation.objects.filter(customer = customer, is_complete = True).exists():
        reservations = Reservation.objects.filter(customer = customer, is_complete = True)
        context = {
            "reservations" : reservations
        }

    return render(request, 'reservation_customer_confirm.html', context=context)