import binascii
from flask_table import Table, Col, LinkCol

#class Results(Table):
#    id = Col('Id', show=False)
#    artist = Col('Artist')
#    title = Col('Title')
#    release_date = Col('Release Date')
#    publisher = Col('Publisher')
#    media_type = Col('Media')
#    edit = LinkCol('Edit', 'edit', url_kwargs=dict(id='id'))
class Results(Table):
    id = Col('Id', show=False)
    name = Col('Name')
    thumb_url = Col('thumb_url')
    full_file_url = Col('full_file_url')
    kind = Col('kind')
   #project_id = db.Column(db.String, nullable=False, db.ForeignKey("projects.id"))
    creator_user_id = Col('creator_user_id')
    #folder_id = Col('folder_id')
    created_at = Col('created_at')
    updated_at = Col('updated_at')
    device_created_at = Col('device_created_at')
    device_updated_at = Col('device_updated_at')
    deleted_at = Col('deleted_at')
    edit = LinkCol('Edit', 'edit', url_kwargs=dict(id='id'))