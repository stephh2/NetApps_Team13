#for access keys
import IBM_keys as key

#for Watson
import os
from watson_developer_cloud import TextToSpeechV1

def sayIt( message ):
    
    text_to_speech = TextToSpeechV1(
            url=key.IBM_url,
            username=key.IBM_username,
            password=key.IBM_password)    
    
    with open('Answer.wav', 'wb') as audio_file:
        audio_file.write(
            text_to_speech.synthesize(
                message, 'audio/wav', 'en-US_AllisonVoice').get_result().content)
    
    os.system('omxplayer -o both Answer.wav')
    print("Said: {}".format(message))
    
def main():
    #TODO: Recieve Tweet
    
    #TODO: Isolate Question:
    
    #TODO: Ask WoframAlpha for the Answer
    
    #TODO: Ask Watson to say the Answer
    sayIt("Hello World");

    #TODO: Send success message to client




if __name__ =="__main__":
    main();