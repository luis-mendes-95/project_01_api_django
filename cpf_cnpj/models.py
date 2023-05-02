from django.db import models


class CpfCnpj(models.Model):
    cpf_cnpj = models.CharField(max_length=14, default='')
    nome_razao_social = models.CharField(max_length=255)
    apelido_nome_fantasia = models.CharField(max_length=255, default='')
    tipo = models.CharField(max_length=255)
    inscricao_estadual = models.CharField(max_length=255, default='')
    inscricao_municipal = models.CharField(max_length=255, default='')
    cep = models.CharField(max_length=8, default='')
    rua = models.CharField(max_length=255, default='')
    numero = models.CharField(max_length=255, default='')
    complemento = models.CharField(max_length=255, default='')
    bairro = models.CharField(max_length=255, default='')
    cidade = models.CharField(max_length=255, default='')
    estado = models.CharField(max_length=2, default='')
    telefone = models.CharField(max_length=255, default='')
    celular = models.CharField(max_length=255, default='')
    email = models.CharField(max_length=255, default='')
    site = models.CharField(max_length=255, default='')

    # 1:N - Account -> CpfCnpj
    account = models.ForeignKey(
        "accounts.Account",
        on_delete=models.CASCADE,
        related_name="cpf_cnpj",
    )