import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.BPLK0pu2YXKRvH7YLre3v9IQWbl3-50ggzgK4DPdUEgnXyX2TzugWD1O9N4hsBtMfREkBZVBxDh_lJN480fDIEBLm4bTqgc1XU7qZEF9ylFr2zI2__IJKQ-bYktBWJ6px2LJNIVD_BN1'
    transferData = TransferData(access_token)

    file_from = input("Enter the file path that you want to tranfer:")
    file_to = input("Enter the path of dropbox:")  # The full path to upload the file to, including the file name

    # API v2
    transferData.upload_file(file_from, file_to)

main()