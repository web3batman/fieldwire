from app import db

class Attachments(db.Model):
   __tablename__ = "attachments"
   id = db.Column(db.String, nullable=False, primary_key=True)
   name = db.Column(db.String, nullable=False)
   thumb_url = db.Column(db.String)
   full_file_url = db.Column(db.String, nullable=False)
   kind = db.Column(db.String, nullable=False)
   project_id = db.Column(db.String, nullable=False)
   creator_user_id = db.Column(db.Integer, nullable=False)
   folder_id = db.Column(db.String)
   created_at = db.Column(db.Integer)
   updated_at = db.Column(db.Integer)
   device_created_at = db.Column(db.Integer, nullable=False)
   device_updated_at = db.Column(db.Integer, nullable=False)
   deleted_at = db.Column(db.Integer)
   
class Floorplans(db.Model):
   __tablename__ = "floorplans"
   id = db.Column(db.String, nullable=False, primary_key=True)
   name = db.Column(db.String, nullable=False)
   description = db.Column(db.String)
   #project_id = db.Column(db.String, nullable=False, db.ForeignKey("projects.id"))
   #folder_id = db.Column(db.String, db.ForeignKey("folders.id"))
   is_name_confirmed = db.Column(db.Integer, nullable=False)
   created_at = db.Column(db.Integer, nullable=False)
   updated_at = db.Column(db.Integer, nullable=False)
   device_updated_at = db.Column(db.Integer, nullable=False)
   deleted_at = db.Column(db.Integer)

class Folders(db.Model):
   __tablename__ = "foldels"
   id = db.Column(db.String, nullable=False, primary_key=True)
   name = db.Column(db.String, nullable=False)
   kind = db.Column(db.String, nullable=False)
   #project_id = db.Column(db.String, nullable=False, db.ForeignKey("projects.id"))
   created_at = db.Column(db.Integer)
   updated_at = db.Column(db.Integer)
   device_created_at = db.Column(db.Integer, nullable=False)
   device_updated_at = db.Column(db.Integer, nullable=False)
   deleted_at = db.Column(db.Integer)

class Projects(db.Model):
   __tablename__ = "projects"
   id = db.Column(db.String, nullable=False, primary_key=True)
   name = db.Column(db.String, nullable=False)
   address = db.Column(db.String)
   currency = db.Column(db.String, nullable=False)
   time_zone_name = db.Column(db.String, nullable=False)
   plan_name = db.Column(db.String, nullable=False)
   man_power_unit = db.Column(db.String, nullable=False)
   measurement_unit = db.Column(db.String, nullable=False)
   is_premium = db.Column(db.Integer, nullable=False)
   is_forms_enabled = db.Column(db.Integer, nullable=False)
   is_email_notifications_enabled = db.Column(db.Integer, nullable=False)
   is_analytics_enabled = db.Column(db.Integer, nullable=False)
   should_prompt_effort_on_complete = db.Column(db.Integer, nullable=False)
   max_fresh_sheets_count = db.Column(db.Integer)
   min_verified_at_days = db.Column(db.Integer, nullable=False)
   created_at = db.Column(db.Integer)
   updated_at = db.Column(db.Integer)
   device_created_at = db.Column(db.Integer, nullable=False)
   device_updated_at = db.Column(db.Integer, nullable=False)
   archived_at = db.Column(db.Integer)
   blocked_at = db.Column(db.Integer)
   deleted_at = db.Column(db.Integer)

class Sheet(db.Model):
   __tablename__ = "sheet"
   id = db.Column(db.String, nullable=False, primary_key=True)
   name = db.Column(db.String)
   version = db.Column(db.Integer, nullable=False)
   description = db.Column(db.String)
   notes = db.Column(db.String)
   has_conflicts = db.Column(db.Integer, nullable=False)
   has_errors = db.Column(db.Integer, nullable=False)
   thumb_url = db.Column(db.String)
   full_file_url = db.Column(db.String)
   file_width = db.Column(db.Integer)
   file_height = db.Column(db.Integer)
   original_width = db.Column(db.Integer)
   original_height = db.Column(db.Integer)
   meters_per_pixel = db.Column(db.Float)
   tile_size = db.Column(db.Integer)
   tiles_base_url = db.Column(db.String)
   tiles_package_url = db.Column(db.String)
   #project_id = db.Column(db.Integer, nullable=False, db.ForeignKey("projects.id"))
   floorplan_id = db.Column(db.String, db.ForeignKey("floorplans.id"))
   created_at = db.Column(db.Integer, nullable=False)
   updated_at = db.Column(db.Integer, nullable=False)
   device_updated_at = db.Column(db.Integer, nullable=False)
   deleted_at = db.Column(db.Integer)
   