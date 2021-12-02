from django.db import models


NAPALM_MAPPING = {
    'alcatel_aos': 'alu'
}
class Device(models.Model):
    name = models.CharField(max_length=100)
    host = models.CharField(max_length=70)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100, blank=True)
    device_type = models.CharField(
        max_length=100, choices = (("router", "Router"), ("switch","Switch"),("firewall","Firewall")), blank=True
    )
    platform = models.CharField(
        max_length=100, choices = (("cisco_ios", "cisco_IOS"), ("alcatel_aos", "alcatel_AOS")), blank=True
    )

    def __str__(self) -> str:
        return self.name

    @property
    def napalm_driver(self) -> str:
        return NAPALM_MAPPING[self.platform]

    #@property
   # def napalm_driver(self) -> str:
     #   return NAPALM_MAPPING[self.platform]
# Create your models here.
