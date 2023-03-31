"""landing_page URL Configuration

    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views 

urlpatterns = [
    #path('', views.index),
    path('', views.index.as_view(), name='index'),
   
]
