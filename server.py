import flask
from flask import Flask
from MSR import audio_convert, execRecognition, wavToRaw, speakerDescription

app = Flask(__name__)


def highScoreDetail(groupId: str, wav_path: str):
	audioByte = wavToRaw(wav_path)
	result = execRecognition(groupId, audioByte)
	# 話者認識の結果
	res = result["response"]
	# スコアの高い順に並べ替え
	res_sorted = sorted(res['speaker'], key=lambda x: x['confidence'], reverse=True)
	max_conf = res_sorted[0]

	# speaker_idが存在しない場合
	if max_conf['speaker_id'] == "":
		unknown_speaker = {
			'name': 'unknown', 
			'confidence': max_conf["confidence"]
		}
		return unknown_speaker
	
	# 存在する場合
	else:
		# スコアの高いユーザーの詳細
		max＿speaker = speakerDescription(max_conf['speaker_id'])[0]
		max＿speaker["confidence"] = max_conf["confidence"]
		return max＿speaker

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in flask.request.files:
        return "ファイル未指定"
    
    fs = flask.request.files['file']
    
    app.logger.info('file_name={}'.format(fs.filename))
    app.logger.info('content_type={} content_length={}, mimetype={}, mimetype_params={}'.format(
        fs.content_type, fs.content_length, fs.mimetype, fs.mimetype_params))

    # ファイルを保存
    save_path = f"upload/{fs.filename}"
    fs.save(save_path)
    groupId = "a5cd6725e73342ad87f0bcca9912df7d"
    result = highScoreDetail(groupId, save_path)
    return result

## おまじない
if __name__ == "__main__":
    app.run(debug=True)