from django.db import models
from django.core.validators import RegexValidator
 # Create Movie Model
class Router(models.Model):
    sapid = models.CharField(max_length=100)
    macAddress = models.CharField(
	max_length=100,
	blank=True,
	null=True,
	validators=[
	RegexValidator(
	regex=r'((?!-)[A-Za-z0-9-]{1, 63}(?<!-)\\.)+[A-Za-z]{2, 6}$',
	message="Enter the valid Mac Address."
	),
	],
	)
    hostname = models.CharField(
	max_length=100,
	blank=True,
	null=True,
	validators=[
	RegexValidator(
	regex=r'([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$',
	message="Enter the valid hostname ."
	),
	],
	)
    ipAddress = models.CharField(
	max_length=100,
	blank=True,
	null=True,
	validators=[
	RegexValidator(
	regex=r'((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$',
	message="Enter the valid ipAddress Address."
	),
	],
	)
	  
    created_at = models.DateTimeField(auto_now_add=True) # When it was create
    updated_at = models.DateTimeField(auto_now=True) # When i was update
    creator = models.ForeignKey('auth.User', related_name='movies', on_delete=models.CASCADE)
    class Meta:
     	db_table = "router"





