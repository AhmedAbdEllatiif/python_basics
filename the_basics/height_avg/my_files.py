import os
from flask import send_file
from werkzeug.utils import secure_filename

def show_file(uploaded_file,as_attachment = False):
    filename, file_extension = os.path.splitext('uploaded-{}'.format( uploaded_file.filename))
    attachment_filename = 'dc-{}{}'.format(filename,file_extension)
    return send_file(secure_filename("uploaded-" + uploaded_file.filename),attachment_filename=attachment_filename,as_attachment=as_attachment,cache_timeout=-1)