from import_export import resources
from .models import Voter

class VotersResource(resources.ModelResource):
    class Meta:
        model = Voter
        import_id_fields = ['idNumber']