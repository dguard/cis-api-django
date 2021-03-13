from graphene_django import DjangoObjectType
import graphene
from valutes.models import Valute as ValuteModel


class Valute(DjangoObjectType):
    class Meta:
        model = ValuteModel

class Query(graphene.ObjectType):
    valutes = graphene.List(Valute)

    def resolve_valutes(self, info):
        return ValuteModel.objects.all()

schema = graphene.Schema(query=Query)
