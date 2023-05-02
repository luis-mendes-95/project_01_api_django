from rest_framework import serializers
from accounts.serializers import AccountSerializer
from .models import CpfCnpj


class CpfCnpjSerializer(serializers.ModelSerializer):
    account = AccountSerializer(read_only=True)
    
    class Meta:
        model = CpfCnpj
        fields = [
            "id", "cpf_cnpj", "nome_razao_social", "apelido_nome_fantasia", "tipo", "inscricao_estadual",
            "inscricao_municipal", "cep", "rua", "numero", "complemento", "bairro", "cidade", "estado",
            "telefone", "celular", "email", "site", "account" 
        ]
        # depth = 2
        # fields = "__all__"

        
