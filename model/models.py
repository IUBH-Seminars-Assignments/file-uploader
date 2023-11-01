import json

class FileUpload:

    topic = "file-upload"

    def __init__(self, file_contents, file_format, external_id, external_id_type):
        self.file_contents = json.loads(file_contents)
        self.file_format = file_format
        self.external_id = external_id
        self.external_id_type = external_id_type

    def to_payload(self):
        return json.dumps({"fileContents" : self.file_contents, "fileFormat" : self.file_format, 
             "externalId" : self.external_id, "externalIdType" : self.external_id_type})

class IdPair:

    topic = "patient-id-results"

    def __init__(self, external_id, external_id_type):
        self.external_id = external_id
        self.external_id_type = external_id_type

    def load_pair_list(json_string):
        lst = json.loads(json_string)
        return [IdPair(item['external_id'], item['external_id_type']) for item in lst]

class IdSearch:

    topic = "patient-id-search"

    def __init__(self, page, page_size):
        self.page = page
        self.page_size = page_size

    def to_payload(self):
        return json.loads({"page" : self.page, "pageSize" : self.page_size})

class RecordSearch:

    topic = "patient-record-search"
    
    def __init__(self, external_id, external_id_type):
        self.external_id = external_id
        self.external_id_type = external_id_type

    def to_payload(self):
        return json.loads({"externalId" : self.external_id, "externalIdType" : self.external_id_type})