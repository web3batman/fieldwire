from app import app
from db_setup import init_db, db_session
from flask import flash, render_template, request, redirect
from flask import Flask
from sqlalchemy.orm.attributes import flag_modified
from forms import *
from models import *
from datetime import datetime, timezone
import googledrive as gd
import json
#init_db()
def totimestamp(dt, epoch=datetime(1970,1,1)):
    td = dt - epoch
    # return td.total_seconds()
    return (td.microseconds + (td.seconds + td.days * 86400) * 10**6) / 10**6 
@app.route('/googledrive')
def googledrive():
    f = gd.gets()
    filesattachment = []
    filesfloorplan = []
    for x in f:
        if x['obj']['title'] == 'PLAN':
            for y in x['subfolder']:
                for z in y['files']:
                    filesfloorplan.append(z)
        if x['obj']['title'] == 'ATTACHMENT':
            for y in x['subfolder']:
                for z in y['files']:
                    filesattachment.append(z)
    kind = [(x['obj']['id'],x['obj']['title']) for x in f]
    folderplan = [[(y['obj']['id'],y['obj']['title']) for y in x['subfolder']] for x in f if x['obj']['title']=='PLAN'][0]
    folderattachment = [[(y['obj']['id'],y['obj']['title']) for y in x['subfolder']] for x in f if x['obj']['title']=='ATTACHMENT'][0]
    #datetime.fromtimestamp(1346236702)
    timestamp_now = round(datetime.utcnow().replace(tzinfo=timezone.utc).timestamp())
    for x in folderplan:
        qry = db_session.query(Folders).filter(Folders.id==x[0])
        test = qry.first()
        if test is None:
            folder = Folders()
            folder.id = x[0]
            folder.name = x[1]
            folder.kind = 'PLAN'
            folder.project_id = '54fba2df-ad0e-446f-902e-0ce86fab6aca'
            folder.created_at = timestamp_now
            folder.updated_at = timestamp_now
            folder.device_created_at = timestamp_now
            folder.device_updated_at = timestamp_now
            db_session.add(folder)
            db_session.commit()
    for x in folderattachment:
        qry = db_session.query(Folders).filter(Folders.id==x[0])
        test = qry.first()
        if test is None:
            folder = Folders()
            folder.id = x[0]
            folder.name = x[1]
            folder.kind = 'ATTACHMENT'
            folder.project_id = '54fba2df-ad0e-446f-902e-0ce86fab6aca'
            folder.created_at = timestamp_now
            folder.updated_at = timestamp_now
            folder.device_created_at = timestamp_now
            folder.device_updated_at = timestamp_now
            db_session.add(folder)
            db_session.commit()
    for x in filesattachment:
        qry = db_session.query(Attachments).filter(Attachments.id==x['id'])
        test = qry.first()
        if test is None:
            attachement = Attachments()
            attachement.id = x['id']
            attachement.name = x['title']
            attachement.thumb_url = x['thumbnailLink']
            attachement.full_file_url = x['alternateLink']
            attachement.kind = 'FILE'
            attachement.project_id = '54fba2df-ad0e-446f-902e-0ce86fab6aca'
            attachement.creator_user_id = ''
            attachement.folder_id = x['parents'][0]['id']
            attachement.created_at = timestamp_now
            attachement.updated_at = timestamp_now
            attachement.device_created_at = timestamp_now
            attachement.device_updated_at = timestamp_now
            db_session.add(attachement)
            db_session.commit()
    for x in filesfloorplan:
        qry = db_session.query(Floorplans).filter(Floorplans.id==x['id'])
        test = qry.first()
        if test is None:
            floorplan = Floorplans()
            floorplan.id = x['id']
            floorplan.name = x['title']
            floorplan.description = ''
            floorplan.project_id = '54fba2df-ad0e-446f-902e-0ce86fab6aca'
            floorplan.folder_id = x['parents'][0]['id']
            floorplan.is_name_confirmed = 1
            floorplan.created_at = timestamp_now
            floorplan.updated_at = timestamp_now
            floorplan.device_updated_at = timestamp_now
            db_session.add(floorplan)
            db_session.commit()
        qry = db_session.query(Sheets).filter(Sheets.id==x['id'])
        test = qry.first()
        if test is None:
            sheet = Sheets()
            sheet.id = x['id']
            sheet.name = x['title']
            sheet.version = 1
            sheet.description = ''
            sheet.notes = ''
            sheet.has_conflicts = 0
            sheet.has_errors = 0
            sheet.thumb_url = x['thumbnailLink']
            sheet.full_file_url = x['alternateLink']
            sheet.file_width = 2446
            sheet.file_height = 1630
            sheet.original_width = 5400
            sheet.original_height = 3600
            sheet.meters_per_pixel = 0.1
            sheet.tile_size = 513
            sheet.tiles_base_url = ''
            sheet.tiles_package_url = ''
            sheet.project_id = '54fba2df-ad0e-446f-902e-0ce86fab6aca'
            sheet.floorplan_id = x['id']
            sheet.created_at = timestamp_now
            sheet.updated_at = timestamp_now
            sheet.device_updated_at = timestamp_now
            db_session.add(sheet)
            db_session.commit()
    return json.dumps(f)

@app.route('/', methods=['GET', 'POST'])
def index():
#    search = AttachmentsForm(request.form)
#    if request.method == 'POST':
#        return search_results(search)
    return render_template('index.html')
#**attachment***********************************************
@app.route('/attachmentlist')
def attachmentlist():
        qry = db_session.query(Attachments)
        results = qry.all()
        for x in results:
            x.created_at = datetime.fromtimestamp(x.created_at / 1e3)
            x.updated_at = datetime.fromtimestamp(x.updated_at / 1e3)
            x.device_created_at = datetime.fromtimestamp(x.device_created_at / 1e3)
            x.device_updated_at = datetime.fromtimestamp(x.device_updated_at / 1e3)
            x.deleted_at = '' if x.deleted_at is None else datetime.fromtimestamp(x.deleted_at / 1e3)
        table = AttachmentsResults(results)
        table.border = True
        return render_template('attachmentresults.html', table=table)
@app.route('/attachmentnew', methods=['GET', 'POST'])
def attachmentnew():
    form = AttachmentsForm(request.form)
    if request.method == 'POST' and form.validate():
        attachment = AttachmentsConvert(Attachments(), form)
        db_session.add(attachment)
        db_session.commit()
        flash('created successfully!')
        return redirect('/attachmentlist')
    return render_template('attachmentform.html', form=form)
@app.route('/attachmentedit/<string:id>', methods=['GET', 'POST'])
def attachmentedit(id):
    qry = db_session.query(Attachments).filter(
                Attachments.id==id)
    attachments = qry.first()
    if attachments:
        form = AttachmentsForm(formdata=request.form, obj=attachments)
        if request.method == 'POST' and form.validate():
            attachment = AttachmentsConvert(Attachments(), form)
            flag_modified(attachment,'name')
            db_session.merge(attachment)
            db_session.flush()
            db_session.commit()
            flash('updated successfully!')
            return redirect('/attachmentlist')
        return render_template('attachmentform.html', form=form)
    else:
        return 'Error loading #{id}'.format(id=id)
@app.route('/attachmentdelete/<string:id>', methods=['GET', 'POST'])
def attachmentdelete(id):
    qry = db_session.query(Attachments).filter(
                Attachments.id==id)
    attachments = qry.first()
    db_session.delete(attachments)
    db_session.commit()
    return redirect('/attachmentlist')
#**floorplan*************************************************************
@app.route('/floorplanlist')
def floorplanlist():
        qry = db_session.query(Floorplans)
        results = qry.all()
        table = FloorplansResults(results)
        table.border = True
        return render_template('floorplanresults.html', table=table)
@app.route('/floorplannew', methods=['GET', 'POST'])
def floorplannew():
    form = FloorplansForm(request.form)
    if request.method == 'POST' and form.validate():
        floorplan = FloorplansConvert(Floorplans(), form)
        db_session.add(floorplan)
        db_session.commit()
        flash('created successfully!')
        return redirect('/floorplanlist')
    return render_template('floorplanform.html', form=form)
@app.route('/floorplanedit/<string:id>', methods=['GET', 'POST'])
def floorplanedit(id):
    qry = db_session.query(Floorplans).filter(
                Floorplans.id==id)
    floorplans = qry.first()
    if floorplans:
        form = FloorplansForm(formdata=request.form, obj=floorplans)
        if request.method == 'POST' and form.validate():
            floorplan = FloorplansConvert(Floorplans(), form)
            flag_modified(floorplan,'name')
            db_session.merge(floorplan)
            db_session.flush()
            db_session.commit()
            flash('updated successfully!')
            return redirect('/floorplanlist')
        return render_template('floorplanform.html', form=form)
    else:
        return 'Error loading #{id}'.format(id=id)
@app.route('/floorplandelete/<string:id>', methods=['GET', 'POST'])
def floorplandelete(id):
    qry = db_session.query(Floorplans).filter(
                Floorplans.id==id)
    floorplan = qry.first()
    db_session.delete(floorplan)
    db_session.commit()
    return redirect('/floorplanlist')
#**folder*************************************************************
@app.route('/folderlist')
def folderlist():
        qry = db_session.query(Folders)
        results = qry.all()
        table = FoldersResults(results)
        table.border = True
        return render_template('folderresults.html', table=table)
@app.route('/foldernew', methods=['GET', 'POST'])
def foldernew():
    form = FoldersForm(request.form)
    if request.method == 'POST' and form.validate():
        folder = FoldersConvert(Folders(), form)
        db_session.add(folder)
        db_session.commit()
        flash('created successfully!')
        return redirect('/folderlist')
    return render_template('folderform.html', form=form)
@app.route('/folderedit/<string:id>', methods=['GET', 'POST'])
def folderedit(id):
    qry = db_session.query(Folders).filter(
                Folders.id==id)
    folders = qry.first()
    if folders:
        form = FoldersForm(formdata=request.form, obj=folders)
        if request.method == 'POST' and form.validate():
            folder = FolderssConvert(Folders(), form)
            flag_modified(folder,'name')
            db_session.merge(folder)
            db_session.flush()
            db_session.commit()
            flash('updated successfully!')
            return redirect('/folderlist')
        return render_template('folderform.html', form=form)
    else:
        return 'Error loading #{id}'.format(id=id)
@app.route('/folderdelete/<string:id>', methods=['GET', 'POST'])
def folderdelete(id):
    qry = db_session.query(Folders).filter(
                Folders.id==id)
    folders = qry.first()
    db_session.delete(folders)
    db_session.commit()
    return redirect('/folderlist')
#**project*************************************************************
@app.route('/projectlist')
def projectlist():
        qry = db_session.query(Projects)
        results = qry.all()
        table = ProjectsResults(results)
        table.border = True
        return render_template('projectresults.html', table=table)
@app.route('/projectnew', methods=['GET', 'POST'])
def projectnew():
    form = ProjectsForm(request.form)
    if request.method == 'POST' and form.validate():
        project = ProjectsConvert(Projects(), form)
        db_session.add(project)
        db_session.commit()
        flash('created successfully!')
        return redirect('/projectlist')
    return render_template('projectform.html', form=form)
@app.route('/projectedit/<string:id>', methods=['GET', 'POST'])
def projectedit(id):
    qry = db_session.query(Projects).filter(
                Projects.id==id)
    projects = qry.first()
    if projects:
        form = ProjectsForm(formdata=request.form, obj=projects)
        if request.method == 'POST' and form.validate():
            project = ProjectsConvert(Projects(), form)
            flag_modified(project,'name')
            db_session.merge(project)
            db_session.flush()
            db_session.commit()
            flash('updated successfully!')
            return redirect('/projectlist')
        return render_template('projectform.html', form=form)
    else:
        return 'Error loading #{id}'.format(id=id)
@app.route('/projectdelete/<string:id>', methods=['GET', 'POST'])
def projectdelete(id):
    qry = db_session.query(Projects).filter(
                Projects.id==id)
    projects = qry.first()
    db_session.delete(projects)
    db_session.commit()
    return redirect('/projectlist')
#**sheet*************************************************************
@app.route('/sheetlist')
def sheetlist():
        qry = db_session.query(Sheets)
        results = qry.all()
        table = SheetsResults(results)
        table.border = True
        return render_template('sheetresults.html', table=table)
@app.route('/sheetnew', methods=['GET', 'POST'])
def sheetnew():
    form = SheetsForm(request.form)
    if request.method == 'POST' and form.validate():
        sheet = SheetsConvert(Sheets(), form)
        db_session.add(sheet)
        db_session.commit()
        flash('created successfully!')
        return redirect('/sheetlist')
    return render_template('sheetform.html', form=form)
@app.route('/sheetedit/<string:id>', methods=['GET', 'POST'])
def sheetedit(id):
    qry = db_session.query(Sheets).filter(
                Sheets.id==id)
    sheets = qry.first()
    if sheets:
        form = SheetsForm(formdata=request.form, obj=sheets)
        if request.method == 'POST' and form.validate():
            sheet = SheetsConvert(Sheets(), form)
            flag_modified(sheet,'name')
            db_session.merge(sheet)
            db_session.flush()
            db_session.commit()
            flash('updated successfully!')
            return redirect('/asheetlist')
        return render_template('sheetform.html', form=form)
    else:
        return 'Error loading #{id}'.format(id=id)
@app.route('/sheetdelete/<string:id>', methods=['GET', 'POST'])
def sheetdelete(id):
    qry = db_session.query(Sheets).filter(
                Sheets.id==id)
    sheets = qry.first()
    db_session.delete(sheets)
    db_session.commit()
    return redirect('/sheetlist')    
if __name__ == '__main__':
    app.run()
