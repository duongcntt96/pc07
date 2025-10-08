# example/views.py
from datetime import datetime

from django.http import HttpResponse


def index(request):
    now = datetime.now()
    html = f'''
    <html>
        <body>
            <h1>Backed for PC07 website !</h1>
            <p>The current time is { now }.</p>
            <p>Đặng Bá Dương</p>
            <p>Nguyễn Thị Huyền Trang</p>
        </body>
    </html>
    '''
    return HttpResponse(html)
