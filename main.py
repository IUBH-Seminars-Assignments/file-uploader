from flask import Flask, render_template, request
from mqtt_client.publisher import MqttClient
from model.models import FileUpload, IdSearch, RecordSearch, IdPair, PatientRecord
from redis_client.client import rc
import os

page_size = 50

app = Flask(__name__,
            static_url_path='/static',
            static_folder='static',
            template_folder='templates')

app.config.update(SECRET_KEY=os.urandom(24))

upload_publisher = MqttClient(host='mqtt', port=1883, topic=FileUpload.topic)
id_search_publisher = MqttClient(host='mqtt', port=1883, topic=IdSearch.topic, s_topic=IdPair.topic)
patient_record_publisher = MqttClient(host='mqtt', port=1883, topic=RecordSearch.topic, s_topic=PatientRecord.topic)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    external_id = request.form['external_id']
    external_id_type = request.form['external_id_type']
    file_format = request.form['file_format']
    file_upload = FileUpload(file_contents=file.read(), file_format=file_format, external_id=external_id,
                             external_id_type=external_id_type)
    upload_publisher.publish(file_upload)
    return render_template('success.html', external_id=external_id, external_id_type=external_id_type)


@app.route('/search', methods=['GET'])
def search_files_view():
    page = int(request.args.get('page')) if request.args.get('page') else 1
    id_search_publisher.publish(IdSearch(page=page, page_size=page_size))
    results = IdPair.load_pair_list(rc.get_with_block(IdSearch.topic))
    return render_template('search.html', results=results)


@app.route('/files', methods=['GET'])
def search_files():
    external_id = request.args.get('external_id')
    external_id_type = request.args.get('external_id_type')
    patient_record_publisher.publish(RecordSearch(external_id=external_id, external_id_type=external_id_type))
    results = rc.get_with_block(RecordSearch.topic)
    return render_template('records.html', results=results)
