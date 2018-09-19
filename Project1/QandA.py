import subprocess
#subprocess.check_output(['ls','-l']) #all that is technically needed...
import os

def sayIt( message ):
    #print subprocess.check_output(['git commit', '-m Initial Files'])
    
    os.system("git add .")
    os.system("git commit -m 'Initial Commit'")
    os.system("git push")
"""    curl -X POST -u "{username}":"{password}" \
    --header "Content-Type: application/json" \
    --header "Accept: audio/wav" \
    --data '{"text": "hello world"}' \
    --output hello_world.wav \
    "{url}/v1/synthesize" """



def main():
    #TODO: Recieve Tweet
    
    #TODO: Isolate Question:
    
    #TODO: Ask WoframAlpha for the Answer
    
    #TODO: Ask Watson to say the Answer
    sayIt("TEST");

    #TODO: Send success message to client




if __name__ =="__main__":
    main();