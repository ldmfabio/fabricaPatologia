# Generated by Django 2.2.4 on 2019-11-19 18:27

import ckeditor.fields
from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AnimalModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, max_length=100, null=True)),
                ('idade', models.CharField(blank=True, max_length=50, null=True)),
                ('sexo', models.CharField(blank=True, max_length=5, null=True)),
                ('cor_pelagem', models.CharField(blank=True, max_length=50)),
                ('dt_cadastro', models.DateField(auto_now_add=True)),
                ('numero', models.PositiveIntegerField(default=0)),
                ('complemento', models.CharField(blank=True, max_length=300, null=True)),
            ],
            options={
                'verbose_name': 'Animal',
                'verbose_name_plural': 'Animais',
            },
        ),
        migrations.CreateModel(
            name='BairroModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_bairro', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='EspecieModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_especie', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Espécie',
                'verbose_name_plural': 'Espécies',
            },
        ),
        migrations.CreateModel(
            name='EstadoModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_estado', models.CharField(choices=[('Acre', 'Acre'), ('Alagoas', 'Alagoas'), ('Amapá', 'Amapá'), ('Amazonas', 'Amazonas'), ('Bahia', 'Bahia'), ('Ceará', 'Ceará'), ('Distrito Federal', 'Distrito Federal'), ('Espírito Santo', 'Espírito Santo'), ('Goiás', 'Goiás'), ('Maranhão', 'Maranhão'), ('Mato Grosso', 'Mato Grosso'), ('Mato Grosso do Sul', 'Mato Grosso do Sul'), ('Minas Gerais', 'Minas Gerais'), ('Pará', 'Pará'), ('Paraíba', 'Paraíba'), ('Paraná', 'Paraná'), ('Pernambuco', 'Pernambuco'), ('Piauí', 'Piauí'), ('Rio de Janeiro', 'Rio de Janeiro'), ('Rio Grande do Norte', 'Rio Grande do Norte'), ('Rio Grande do Sul', 'Rio Grande do Sul'), ('Rondônia', 'Rondônia'), ('Roraima', 'Roraima'), ('Santa Catarina', 'Santa Catarina'), ('São Paulo', 'São Paulo'), ('Sergipe', 'Sergipe'), ('Tocantins', 'Tocantins')], max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TipoLaudoModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_laudo', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='VeterinarioPatologistaModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
                ('formacao', models.CharField(max_length=150)),
                ('crmv', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='VeterinarioResponsavelModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_veterinario', models.CharField(blank=True, max_length=150, null=True)),
                ('telefone', models.CharField(blank=True, max_length=40, null=True)),
                ('crmv', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UsuarioModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_nasc', models.DateField(blank=True, verbose_name='Data Nascimento')),
                ('cpf', models.CharField(blank=True, max_length=14)),
                ('rg', models.CharField(blank=True, max_length=45)),
                ('telefone', models.CharField(blank=True, max_length=45)),
                ('celular', models.CharField(blank=True, max_length=45)),
                ('email', models.CharField(blank=True, max_length=100)),
                ('endereco', models.CharField(blank=True, max_length=300)),
                ('numero', models.IntegerField(blank=True)),
                ('bairro', models.CharField(blank=True, max_length=100)),
                ('cidade', models.CharField(blank=True, max_length=100)),
                ('estado', models.CharField(blank=True, max_length=100)),
                ('username', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RuaModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_rua', models.CharField(max_length=50)),
                ('cep', models.CharField(max_length=40)),
                ('id_bairro', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='laudosMedvet.BairroModel')),
            ],
        ),
        migrations.CreateModel(
            name='RequisicaoLaudoModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rghv', models.IntegerField(blank=True, null=True)),
                ('dt_coleta', models.DateField()),
                ('material_enviado', ckeditor.fields.RichTextField()),
                ('historico_clinico', ckeditor.fields.RichTextField()),
                ('descricao_macroscopica', ckeditor.fields.RichTextField()),
                ('scan_figura_ficha_clinica', models.ImageField(blank=True, upload_to='imagem_ficha_clinica')),
                ('responsavel_recebimento', models.CharField(blank=True, max_length=100)),
                ('dt_recebimento', models.DateField()),
                ('cod_animail', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='laudosMedvet.AnimalModel')),
                ('tipo_de_laudo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='laudosMedvet.TipoLaudoModel')),
            ],
        ),
        migrations.CreateModel(
            name='RacaModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_raca', models.CharField(max_length=100)),
                ('id_especie', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='laudosMedvet.EspecieModel')),
            ],
            options={
                'verbose_name': 'Raça',
                'verbose_name_plural': 'Raças',
            },
        ),
        migrations.CreateModel(
            name='ProprietarioModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_proprietario', models.CharField(max_length=150)),
                ('data_nasc', models.DateField(blank=True, null=True, verbose_name='Data Nascimento')),
                ('cpf', models.CharField(blank=True, max_length=14, null=True)),
                ('rg', models.CharField(blank=True, max_length=15, null=True)),
                ('telefone', models.CharField(blank=True, max_length=40, null=True)),
                ('celular', models.CharField(blank=True, max_length=40, null=True)),
                ('email', models.CharField(blank=True, max_length=80, null=True)),
                ('numero', models.IntegerField(blank=True, null=True)),
                ('complemento', models.CharField(blank=True, max_length=250, null=True)),
                ('rua', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='laudosMedvet.RuaModel')),
            ],
        ),
        migrations.CreateModel(
            name='PermissaoModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_grupo', models.ManyToManyField(to='auth.Group')),
            ],
            options={
                'permissions': (('pode_acessar_estado', 'Pode acessar estado'),),
            },
        ),
        migrations.CreateModel(
            name='LaudoModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao_microscopica', ckeditor.fields.RichTextField()),
                ('diagnostico_morfologico', ckeditor.fields.RichTextField()),
                ('sistemas', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Cardiovascular', 'Cardiovascular'), ('Pulmonar', 'Pulmonar'), ('Digestivo', 'Digestivo'), ('Endócrino', 'Endócrino'), ('Nervoso', 'Nervoso'), ('Reprodutivo', 'Reprodutivo'), ('Muscular', 'Muscular'), ('Esquelético', 'Esquelético'), ('Tegumentar', 'Tegumentar'), ('Excretor', 'Excretor')], max_length=104, null=True)),
                ('etiologia', models.CharField(blank=True, max_length=300, null=True)),
                ('diagnostico_final', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('comentarios', ckeditor.fields.RichTextField()),
                ('dt_laudo', models.DateField()),
                ('id_requisicao', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='laudosMedvet.RequisicaoLaudoModel')),
                ('veterinario_patologista', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='laudosMedvet.VeterinarioPatologistaModel')),
            ],
        ),
        migrations.CreateModel(
            name='ImagensModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_imagem', models.CharField(max_length=150)),
                ('imagem', models.ImageField(blank=True, null=True, upload_to='imagens')),
                ('id_laudo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='laudosMedvet.LaudoModel')),
            ],
        ),
        migrations.CreateModel(
            name='CidadeModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_cidade', models.CharField(max_length=100)),
                ('id_estado', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='laudosMedvet.EstadoModel')),
            ],
        ),
        migrations.AddField(
            model_name='bairromodel',
            name='id_cidade',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='laudosMedvet.CidadeModel'),
        ),
        migrations.AddField(
            model_name='animalmodel',
            name='bairro',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='laudosMedvet.BairroModel'),
        ),
        migrations.AddField(
            model_name='animalmodel',
            name='cidade',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='laudosMedvet.CidadeModel'),
        ),
        migrations.AddField(
            model_name='animalmodel',
            name='id_especie',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='laudosMedvet.EspecieModel'),
        ),
        migrations.AddField(
            model_name='animalmodel',
            name='id_estado',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='laudosMedvet.EstadoModel'),
        ),
        migrations.AddField(
            model_name='animalmodel',
            name='proprietario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='laudosMedvet.ProprietarioModel'),
        ),
        migrations.AddField(
            model_name='animalmodel',
            name='raca',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='laudosMedvet.RacaModel'),
        ),
        migrations.AddField(
            model_name='animalmodel',
            name='rua',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='laudosMedvet.RuaModel'),
        ),
        migrations.AddField(
            model_name='animalmodel',
            name='veterinario_responsavel',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='laudosMedvet.VeterinarioResponsavelModel'),
        ),
    ]
