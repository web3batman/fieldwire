# forms.py

from wtforms import Form, StringField, SelectField, validators
from flask_table import Table, Col, LinkCol
from db_setup import db_session
from models import *
class AlbumForm(Form):
    media_types = [('Digital', 'Digital'),
                   ('CD', 'CD'),
                   ('Cassette Tape', 'Cassette Tape')
                   ]
    artist = StringField('Artist')
    title = StringField('Title')
    release_date = StringField('Release Date')
    publisher = StringField('Publisher')
    media_type = SelectField('Media', choices=media_types)
    search = StringField('')
    
class AttachmentsForm(Form):
    projects_types = []
    projects_types.append(tuple(("", "")))
    for x in db_session.query(Projects).all():
        projects_types.append(tuple((x.id,x.name)))
    folders_types = []
    folders_types.append(tuple(("", "")))
    for x in db_session.query(Folders).all():
        folders_types.append(tuple((x.id,x.name)))
    id = StringField('id')
    name = StringField('name')
    thumb_url = StringField('thumb_url')
    full_file_url = StringField('full_file_url')
    kind = StringField('kind')
#    project_id = StringField('project_id')
    creator_user_id = StringField('creator_user_id')
    folder_id = StringField('folder_id')
    created_at = StringField('created_at')
    updated_at = StringField('updated_at')
    device_created_at = StringField('device_created_at')
    device_updated_at = StringField('device_updated_at')
    deleted_at = StringField('deleted_at')
    project_id = SelectField('Proyecto', choices=projects_types)
    folder_id = SelectField('Folder', choices=folders_types)
class AttachmentsResults(Table):
    id = Col('Id', show=False)
    name = Col('name')
    thumb_url = Col('thumb_url')
    full_file_url = Col('full_file_url')
    kind = Col('kind')
    project_id = Col('projects.id')
    creator_user_id = Col('creator_user_id')
    folder_id = Col('folder_id')
    created_at = Col('created_at')
    updated_at = Col('updated_at')
    device_created_at = Col('device_created_at')
    device_updated_at = Col('device_updated_at')
    deleted_at = Col('deleted_at')
    edit = LinkCol('Edit', 'attachmentedit', url_kwargs=dict(id='id'))
    delete = LinkCol('Delete', 'attachmentdelete', url_kwargs=dict(id='id'))
def AttachmentsConvert(attachment, form):
    attachment.id = form.id.data
    attachment.name = form.name.data
    attachment.thumb_url = form.thumb_url.data
    attachment.full_file_url = form.full_file_url.data
    attachment.kind = form.kind.data
    attachment.project_id = form.project_id .data
    attachment.creator_user_id = form.creator_user_id.data
    attachment.folder_id = form.folder_id.data
    attachment.created_at = form.created_at.data
    attachment.updated_at = form.updated_at.data
    attachment.device_created_at = form.device_created_at.data
    attachment.device_updated_at = form.device_updated_at.data
    attachment.deleted_at = form.deleted_at.data
    return attachment
class FloorplansForm(Form):
    id = StringField('id')
    name = StringField('name')
    description = StringField('description')
    project_id = StringField('project_id')
    folder_id = StringField('folder_id')
    is_name_confirmed = StringField('is_name_confirmed')
    created_at = StringField('created_at')
    updated_at = StringField('updated_at')
    device_updated_at = StringField('device_updated_at')
    deleted_at = StringField('deleted_at')
class FloorplansResults(Table):
    id = Col('id', show=False)
    name = Col('name')
    description = Col('description')
    project_id = Col('project_id')
    folder_id = Col('folder_id')
    is_name_confirmed = Col('is_name_confirmed')
    created_at = Col('created_at')
    updated_at = Col('updated_at')
    device_updated_at = Col('device_updated_at')
    deleted_at = Col('deleted_at')
    edit = LinkCol('Edit', 'floorplanedit', url_kwargs=dict(id='id'))
    delete = LinkCol('Delete', 'floorplandelete', url_kwargs=dict(id='id'))
def FloorplansConvert(floorplans, form):
    floorplans.id = form.id.data
    floorplans.name = form.name.data
    floorplans.description = form.description.data
    floorplans.project_id = form.project_id.data
    floorplans.folder_id = form.folder_id.data
    floorplans.is_name_confirmed = form.is_name_confirmed.data
    floorplans.created_at = form.created_at.data
    floorplans.updated_at = form.updated_at.data
    floorplans.device_updated_at = form.device_updated_at.data
    floorplans.deleted_at = form.deleted_at.data
    return floorplans
class FoldersForm(Form):
    id = StringField('id')
    name = StringField('name')
    kind = StringField('kind')
    project_id = StringField('project_id')
    created_at = StringField('created_at')
    updated_at = StringField('updated_at')
    device_created_at = StringField('device_created_at')
    device_updated_at = StringField('device_updated_at')
    deleted_at = StringField('deleted_at')
class FoldersResults(Table):
    id = Col('id', show=False)
    name = Col('name')
    kind = Col('kind')
    project_id = Col('project_id')
    created_at = Col('created_at')
    updated_at = Col('updated_at')
    device_created_at = Col('device_created_at')
    device_updated_at = Col('device_updated_at')
    deleted_at = Col('deleted_at')
    edit = LinkCol('Edit', 'folderedit', url_kwargs=dict(id='id'))
    delete = LinkCol('Delete', 'folderdelete', url_kwargs=dict(id='id'))
def FoldersConvert(folders, form):
    folders.id = form.id.data
    folders.name = form.name.data
    folders.kind = form.kind.data
    folders.project_id = form.project_id.data
    folders.created_at = form.created_at.data
    folders.updated_at = form.updated_at.data
    folders.device_created_at = form.device_created_at.data
    folders.device_updated_at = form.device_updated_at.data
    folders.deleted_at = form.deleted_at.data
    return folders
class ProjectsForm(Form):
    id = StringField('id')
    name = StringField('name')
    address = StringField('address')
    currency = StringField('currency')
    time_zone_name = StringField('time_zone_name')
    plan_name = StringField('plan_name')
    man_power_unit = StringField('man_power_unit')
    measurement_unit = StringField('measurement_unit')
    is_premium = StringField('is_premium')
    is_forms_enabled = StringField('is_forms_enabled')
    is_email_notifications_enabled = StringField('is_email_notifications_enabled')
    is_analytics_enabled = StringField('is_analytics_enabled')
    should_prompt_effort_on_complete = StringField('hould_prompt_effort_on_complete')
    max_fresh_sheets_count = StringField('max_fresh_sheets_count')
    min_verified_at_days = StringField('min_verified_at_days')
    created_at = StringField('created_at')
    updated_at = StringField('updated_at')
    device_created_at = StringField('device_created_at')
    device_updated_at = StringField('device_updated_at')
    archived_at = StringField('archived_at')
    blocked_at = StringField('blocked_at')
    deleted_at = StringField('deleted_at')
class ProjectsResults(Table):
    id = Col('id', show=False)
    name = Col('name')
    address = Col('address')
    currency = Col('currency')
    time_zone_name = Col('time_zone_name')
    plan_name = Col('plan_name')
    man_power_unit = Col('man_power_unit')
    measurement_unit = Col('measurement_unit')
    is_premium = Col('is_premium')
    is_forms_enabled = Col('is_forms_enabled')
    is_email_notifications_enabled = Col('is_email_notifications_enabled')
    is_analytics_enabled = Col('is_analytics_enabled')
    should_prompt_effort_on_complete = Col('hould_prompt_effort_on_complete')
    max_fresh_sheets_count = Col('max_fresh_sheets_count')
    min_verified_at_days = Col('min_verified_at_days')
    created_at = Col('created_at')
    updated_at = Col('updated_at')
    device_created_at = Col('device_created_at')
    device_updated_at = Col('device_updated_at')
    archived_at = Col('archived_at')
    blocked_at = Col('blocked_at')
    deleted_at = Col('deleted_at')
    edit = LinkCol('Edit', 'projectedit', url_kwargs=dict(id='id'))
    delete = LinkCol('Delete', 'projectdelete', url_kwargs=dict(id='id'))
def ProjectsConvert(projects, form):
    projects.id = form.id.data
    projects.name = form.name.data
    projects.address = form.address.data
    projects.currency = form.currency.data
    projects.time_zone_name = form.time_zone_name.data
    projects.plan_name = form.plan_name.data
    projects.man_power_unit = form.man_power_unit.data
    projects.measurement_unit = form.measurement_unit.data
    projects.is_premium = form.is_premium.data
    projects.is_forms_enabled = form.is_forms_enabled.data
    projects.is_email_notifications_enabled = form.is_email_notifications_enabled.data
    projects.is_analytics_enabled = form.is_analytics_enabled.data
    projects.should_prompt_effort_on_complete = form.hould_prompt_effort_on_complete.data
    projects.max_fresh_sheets_count = form.max_fresh_sheets_count.data
    projects.min_verified_at_days = form.min_verified_at_days.data
    projects.created_at = form.created_at.data
    projects.updated_at = form.updated_at.data
    projects.device_created_at = form.device_created_at.data
    projects.device_updated_at = form.device_updated_at.data
    projects.archived_at = form.archived_at.data
    projects.blocked_at = form.blocked_at.data
    projects.deleted_at = form.deleted_at.data
    return projects
class SheetsForm(Form):
    id = StringField('id')
    name = StringField('name')
    version = StringField('version ')
    description = StringField('description')
    notes = StringField('notes')
    has_conflicts = StringField('has_conflicts')
    has_errors = StringField('has_errors')
    thumb_url = StringField('thumb_url')
    full_file_url = StringField('full_file_url')
    file_width = StringField('file_width')
    file_height = StringField('file_height')
    original_width = StringField('original_width')
    original_height = StringField('original_height')
    meters_per_pixel = StringField('meters_per_pixel')
    tile_size = StringField('tile_size') 
    tiles_base_url = StringField('tiles_base_url')
    tiles_package_url = StringField('tiles_package_url')
    project_id = StringField('project_id')
    floorplan_id = StringField('floorplan_id')
    created_at = StringField('created_at')
    updated_at = StringField('updated_at')
    device_updated_at = StringField('device_updated_at')
    deleted_at = StringField('deleted_at')
class SheetsResults(Table):
    id = Col('id', show=False)
    name = Col('name')
    version = Col('version ')
    description = Col('description')
    notes = Col('notes')
    has_conflicts = Col('has_conflicts')
    has_errors = Col('has_errors')
    thumb_url = Col('thumb_url')
    full_file_url = Col('full_file_url')
    file_width = Col('file_width')
    file_height = Col('file_height')
    original_width = Col('original_width')
    original_height = Col('original_height')
    meters_per_pixel = Col('meters_per_pixel')
    tile_size = Col('tile_size') 
    tiles_base_url = Col('tiles_base_url')
    tiles_package_url = Col('tiles_package_url')
    project_id = Col('project_id')
    floorplan_id = Col('floorplan_id')
    created_at = Col('created_at')
    updated_at = Col('updated_at')
    device_updated_at = Col('device_updated_at')
    deleted_at = Col('deleted_at')
    edit = LinkCol('Edit', 'sheetedit', url_kwargs=dict(id='id'))
    delete = LinkCol('Delete', 'sheetdelete', url_kwargs=dict(id='id'))
def SheetsConvert(sheets, form):
    sheets.id = form.id.data
    sheets.name = form.name.data
    sheets.version = form.version.data
    sheets.description = form.description.data
    sheets.notes = form.notes.data
    sheets.has_conflicts = form.has_conflicts.data
    sheets.has_errors = form.has_errors.data
    sheets.thumb_url = form.thumb_url.data
    sheets.full_file_url = form.full_file_url.data
    sheets.file_width = form.file_width.data
    sheets.file_height = form.file_height.data
    sheets.original_width = form.original_width.data
    sheets.original_height = form.original_height.data
    sheets.meters_per_pixel = form.meters_per_pixel.data
    sheets.tile_size = form.tile_size.data 
    sheets.tiles_base_url = form.tiles_base_url.data
    sheets.tiles_package_url = form.tiles_package_url.data
    sheets.project_id = form.project_id.data
    sheets.floorplan_id = form.floorplan_id.data
    sheets.created_at = form.created_at.data
    sheets.updated_at = form.updated_at.data
    sheets.device_updated_at = form.device_updated_at.data
    sheets.deleted_at = form.deleted_at.data
    return sheets
