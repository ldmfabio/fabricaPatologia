# Generated by Django 2.2 on 2019-04-23 17:41

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnimalModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=130)),
                ('idade', models.CharField(max_length=2)),
                ('raca', models.CharField(max_length=100)),
                ('pelagem', models.CharField(max_length=130)),
                ('proprietario', models.CharField(max_length=130)),
                ('telefone', models.CharField(max_length=11)),
                ('veterinario_responsavel', models.CharField(max_length=130)),
                ('telefone_vet', models.CharField(max_length=11)),
                ('endereco', models.CharField(blank=True, max_length=128)),
                ('numero_endereco', models.CharField(blank=True, max_length=10)),
                ('bairro', models.CharField(blank=True, max_length=128)),
                ('cep', models.CharField(blank=True, max_length=9)),
                ('data_cadastro_animal', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='CidadeModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='EspecieModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='EstadoModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='LaudoModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('historico_clinico', models.CharField(max_length=3000)),
                ('descricao_macroscopica', models.CharField(max_length=3000)),
                ('descricao_microscopica', models.CharField(max_length=3000)),
                ('diagnostico_morfologico', models.CharField(max_length=3000)),
                ('comentarios', models.CharField(blank=True, max_length=3000)),
                ('data_laudo', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='SexoModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='TipoLaudoModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='UsuarioModel',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'user',
                'abstract': False,
                'verbose_name_plural': 'users',
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
