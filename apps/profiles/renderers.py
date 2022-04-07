import json
from email import charset

from rest_framework.renderers import JSONRenderer


class ProfileJSONRenderer(JSONRenderer):
    charset ='utf-8'

    def render(self, data, accepted_media_types=None,renderer_context=None): # define func override jsonrender
        errors = data.get('errors', None)

        if errors is not None:
            return super(ProfileJSONRenderer, self).render(data)
        return json.dumps({"profile":data}) # we want the namespace of profile to be data
