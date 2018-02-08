import dropbox
from share_prj.settings import DROPBOX_APP_ACCESS_TOKEN, DROPBOX_APP_KEY


def upload_file():
    dbx = dropbox.Dropbox(DROPBOX_APP_ACCESS_TOKEN)
    dbx.files_upload('backup', '/media')