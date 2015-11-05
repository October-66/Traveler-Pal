from  django.utils import timezone


def getCurDateTime():
    return timezone.now()

def toJSON(self):
    fields = []
    for field in self._meta.fields:
        fields.append(field.name)

    d = {}
    for attr in fields:
        d[attr] = getattr(self, attr)

    import json
    return json.dumps(d)
