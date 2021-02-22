from django.shortcuts import render, redirect
from paynow import Paynow
from django.contrib.auth.models import User

paynow = Paynow('', '', 'http://return.url', 'https://crowdlearn.co.zw')


def index(request):
    return render(request, 'pindex.html')


def algopurchase(request):
    return render(request, 'algo.html')


def download_course(request):
    return render(request, 'getcourse.html')


def download_flowchart_course(request):
    return render(request,'flowchartcourse.html')


def start_payment(request):
    data = request.POST
    payment = paynow.create_payment('Client', request.POST['email'])
    payment.add('Course', float(request.POST['amount']))
    response = paynow.send(payment)

    if response.status:
        return redirect(response.redirect_url)


def pay_algorithm_course(request):
    data = request.POST
    payment = paynow.create_payment('Algorithm FPC', request.POST['email'])
    payment.add('Algorithm Flowcharts and Psuedocode Course', float(request.POST['amount']))
    response = paynow.send(payment)

    if response.status:
        return redirect(response.redirect_url)
