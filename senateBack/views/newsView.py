from flask_admin.contrib.sqla import ModelView
from flask_login import current_user
from .help import BlobUploadField

class NewsView(ModelView):
    form_columns = ['title', 'content', 'isFile', 'supported_doc']
    
    form_extra_fields = {'supported_doc': BlobUploadField(
        
        allowed_extensions=['pdf', 'doc', 'odt', 'csv'],
        
    )}
    
    def is_accessible(self):
        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        # redirect to login page if user doesn't have access
        return "<h3>Not Login. Go to login page by /login?api_key=<YOUR API_KEY></h3>"