from flask_admin.contrib.sqla import ModelView
from flask_login import current_user
from .help import BlobUploadField

class SocView(ModelView):
    form_columns = ['society_name', 'contact_person_name', 'phone', 'email', 'content', 'image']
    
    form_extra_fields = {'image': BlobUploadField(
        
        allowed_extensions=['png', 'jpg', 'jpeg'],
        
    )}
    
    def is_accessible(self):
        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        # redirect to login page if user doesn't have access
        return "<h3>Not Login. Go to login page by /login?api_key=<YOUR API_KEY></h3>"