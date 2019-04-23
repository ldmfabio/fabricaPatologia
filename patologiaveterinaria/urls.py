"""patologiaveterinaria URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from patologiaveterinaria import view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', view.LoginUserView.as_view(), name="login_user"),
    path('login', view.LoginView.as_view(), name='login'),
    path('logout', view.LogoutView.as_view(), name='logout'),
    path('cadastro/usuario/', view.CadastroUsuarioView.as_view(), name='cadastro_usuario'),
    path('principal/', view.PaginaPrincipal.as_view(), name='principal'),
    path('cadastro/animal/', view.CadastrarAnimal.as_view(), name='cadastrar_animal'),
    path('cadastro/laudo/', view.CadastrarLaudo.as_view(), name='cadastrar_laudo'),
    path('mostra_animal', view.MostraAnimal.as_view(), name='mostra_animal'),
    path('lista_laudos', view.MostraLaudos.as_view(), name='mostra_laudos'),

]
