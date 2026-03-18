from django.shortcuts import render
from .forms import QRCodeForm
import qrcode
import os
from django.conf import settings


def generate_qr_codes(request):
    if request.method == "POST":
        form = QRCodeForm(request.POST)
        if form.is_valid():
            res_name = form.cleaned_data['restaurant_name']
            url = form.cleaned_data['url']

            # Generate QR Code
            qr = qrcode.make(url)
            file_name = res_name.replace(" ", "_").lower() + '_menu.png'
            file_path = os.path.join(settings.MEDIA_ROOT, file_name)
            qr.save(file_path)

            # Build URL using forward slashes (NOT os.path.join — breaks on Windows)
            qr_url = settings.MEDIA_URL + file_name

            context = {
                'res_name': res_name,
                'qr_url': qr_url,
                'file_name': file_name,
            }
            return render(request, 'qr_result.html', context)

        # form is invalid — re-render form with errors
        return render(request, 'generate_qr_code.html', {'form': form})

    # GET request
    form = QRCodeForm()
    return render(request, 'generate_qr_code.html', {'form': form})