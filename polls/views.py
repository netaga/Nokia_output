from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from napalm import get_network_driver
from netmiko import ConnectHandler


from .models import Device

NAPALM_MAPPING = {
    'alcatel_aos': 'alu'
}

def index(request: HttpRequest) -> HttpResponse:
    devices = Device.objects.all()
    context = {
        'title': 'Hello stream',
        'name': 'Aga',
        'devices': devices
    }

    return render(request, 'base.html', context)

def device(request: HttpRequest, device_id) -> HttpResponse:
    device = Device.objects.get(pk=device_id)
    if request.method == 'GET':
        #driver = get_network_driver(device.napalm_driver)
        comm_parm = {
            'device_type': device.platform,
            'ip': device.host,
            'username': 'netadmin',
            'password': 'J3g0pi3s#'
        }
        with ConnectHandler(**comm_parm) as device_conn:
            interface = device_conn.send_command("show port")
            interfaces = interface.split('\\n')
        context = {
            'device': device,
            'interfaces': interfaces
        }
        return render(request,'device.html',context)