# Generated by Django 4.2 on 2023-05-02 14:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="CpfCnpj",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("cpf_cnpj", models.CharField(default="", max_length=14)),
                ("nome_razao_social", models.CharField(max_length=255)),
                ("apelido_nome_fantasia", models.CharField(default="", max_length=255)),
                ("tipo", models.CharField(max_length=255)),
                ("inscricao_estadual", models.CharField(default="", max_length=255)),
                ("inscricao_municipal", models.CharField(default="", max_length=255)),
                ("cep", models.CharField(default="", max_length=8)),
                ("rua", models.CharField(default="", max_length=255)),
                ("numero", models.CharField(default="", max_length=255)),
                ("complemento", models.CharField(default="", max_length=255)),
                ("bairro", models.CharField(default="", max_length=255)),
                ("cidade", models.CharField(default="", max_length=255)),
                ("estado", models.CharField(default="", max_length=2)),
                ("telefone", models.CharField(default="", max_length=255)),
                ("celular", models.CharField(default="", max_length=255)),
                ("email", models.CharField(default="", max_length=255)),
                ("site", models.CharField(default="", max_length=255)),
                (
                    "account",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="cpf_cnpj",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]