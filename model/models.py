import json
import base64


class FileUpload:
    topic = "file-upload"

    def __init__(self, file_contents, file_format, external_id, external_id_type):
        self.file_contents = file_contents
        self.file_format = file_format
        self.external_id = external_id
        self.external_id_type = external_id_type

    def to_payload(self):
        return json.dumps({"fileContents": base64.b64encode(self.file_contents).decode("utf-8"), "fileFormat": self.file_format,
                           "externalId": self.external_id, "externalIdType": self.external_id_type})


# Response DTO for searching external Ids
class IdPair:
    topic = "patient-id-results"

    def __init__(self, external_id, external_id_type):
        self.external_id = external_id
        self.external_id_type = external_id_type

    @staticmethod
    def load_pair_list(json_string):
        lst = json.loads(json_string)
        return [IdPair(item['external_id'], item['external_id_type']) for item in lst]


# Request DTO for searching external Ids
class IdSearch:
    topic = "patient-id-search"

    def __init__(self, page, page_size):
        self.page = page
        self.page_size = page_size

    def to_payload(self):
        return json.dumps({"page": self.page, "pageSize": self.page_size})


# Request DTO for searching patient records
class RecordSearch:
    topic = "patient-record-search"

    def __init__(self, external_id, external_id_type):
        self.external_id = external_id
        self.external_id_type = external_id_type

    def to_payload(self):
        return json.dumps({"externalId": self.external_id, "externalIdType": self.external_id_type})


# Part of the Patient Record DTO
class MedicalRecord:
    def __init__(self, file_contents, file_format, external_id, external_id_type):
        self.file_contents = json.loads(file_contents)
        self.file_format = file_format
        self.external_id = external_id
        self.external_id_type = external_id_type


# Response DTO for searching patient records
class PatientRecord:
    topic = "patient-record-results"

    def __init__(self, json_string):
        json_dict = json.loads(json_string)
        self.id = json_dict['id']
        self.records = [MedicalRecord(item['file_contents'], item['file_format'], item['external_id'],
                                      item['external_id_type']) for item in json_dict['records']]

    @staticmethod
    def load_record(json_string):
        return PatientRecord(json.loads(json_string))
