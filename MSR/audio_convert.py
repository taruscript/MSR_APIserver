from pydub import AudioSegment 
import sox

from pydub.utils import make_chunks
from pydub.exceptions import CouldntDecodeError


tfm = sox.Transformer()

def wavToRaw(wav_path: str):
    
    try:
        myaudio = AudioSegment.from_file(wav_path , "wav") 
    except CouldntDecodeError:
        raise(TypeError("wav形式ではないため、raw形式に変換出来ませんでした"))

    raw_audio_data = bytes(tfm.build_array(input_filepath=wav_path))
    print(raw_audio_data)

    return raw_audio_data
