from django.shortcuts import render
import boto3
import psutil
import requests
from django.http import JsonResponse

def get_instance_info():
    """Fetch AWS instance details, system usage, and public IP"""
    try:
        instance_metadata_url = "http://169.254.169.254/latest/meta-data/"
        az = requests.get(instance_metadata_url + "placement/availability-zone").text
        instance_id = requests.get(instance_metadata_url + "instance-id").text
        public_ip = requests.get(instance_metadata_url + "public-ipv4").text  # Fetch Public IP
        region = az[:-1]  # Extract region from AZ (e.g., us-east-1a → us-east-1)
        
        cpu_usage = psutil.cpu_percent(interval=1)
        memory = psutil.virtual_memory()

        return {
            "Instance ID": instance_id,
            "Public IP": public_ip,
            "Region": region,
            "Availability Zone": az,
            "CPU Usage (%)": cpu_usage,
            "Memory Used (MB)": memory.used // (1024 ** 2),
            "Total Memory (MB)": memory.total // (1024 ** 2),
        }
    except Exception as e:
        return {"error": str(e)}

def system_status(request):
    """API endpoint to show EC2 system details"""
    return JsonResponse(get_instance_info())

def home(request):
    """Simple home page displaying EC2 metadata"""
    context = get_instance_info()
    return render(request, "home.html", context)
