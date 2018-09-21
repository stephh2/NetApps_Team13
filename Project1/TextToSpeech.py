#for access keys
import BridgeKeys as key

#for Watson
import os
from watson_developer_cloud import TextToSpeechV1

def sayIt( message ):
    
    text_to_speech = TextToSpeechV1(
            url=key.f.decrypt(key.encrypted_IBM_url),
            username=key.f.decrypt(key.encrypted_IBM_username),
            password=key.f.decrypt(key.encrypted_IBM_password) )   
    
    with open('Answer.wav', 'wb') as audio_file:
        audio_file.write(
            text_to_speech.synthesize(
                message, 'audio/wav', 'en-US_AllisonVoice').get_result().content)
    
    os.system('omxplayer -o both Answer.wav')