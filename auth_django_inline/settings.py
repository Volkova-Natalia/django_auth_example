import json


app_name = 'auth_django_inline'
base_url = 'auth-django-inline/'
namespace = 'auth-django-inline'


with open(app_name+"/swagger.json", "r") as swagger_file:
    swagger_paths = json.load(swagger_file)['paths']
end_point = {
    name: {
        'url': path[1:],
        'name': name,
    }
    for name in ('registration',
                 'login',
                 'logout',
                 )
    for path in swagger_paths
    if name == swagger_paths[path]['x-name']
}
