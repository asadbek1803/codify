from django.shortcuts import render
import os
from django.http import FileResponse, Http404
from django.conf import settings
# Create your views here.


def download_apk(request, file_path):
    file_path = os.path.join(settings.MEDIA_ROOT, file_path)

    # Fayl mavjudligini tekshirish
    if os.path.exists(file_path):
        # Faylni yuklab olish
        with open(file_path, 'rb') as fh:
            response = FileResponse(fh)
            response['Content-Disposition'] = 'attachment; filename=' + os.path.basename(file_path)
            return response
    else:
        # Agar fayl topilmasa, xatolik qaytarish
        return Http404('Apk yuklashda xatolik!')

