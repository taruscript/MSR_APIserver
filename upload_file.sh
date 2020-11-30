#bin/bash
FILE=example.wav
URL=http://127.0.0.1:5000/upload
INPUTNAME=file
curl -X POST -F $INPUTNAME=@$FILE $URL