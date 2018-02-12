# ravendog
Watch dog for RVN miner

# If GPU Load falls under 15% and stays there for 3 seconds RavenDog will restart the miner
# Set miner name in minerList 
    your.bat will need title %~n0 as the first line (check RVN_miner.bat)
    RavenDog will search all folders in the directory and folders under(for "minerList:" name)
# Set GPU_checkNR 
    If you wish to check GPU load on second or third GPU
# Set how many seconds to check after
# Explorer info is taken from http://threeeyed.info/ API
# Log file will be created in the same directory everytime RavenDog is started (i.e. when PC freezes and restarts)
# Set "sendEmail:" to True ,to receive notifications , or False to disable it
    Create new Gmail account or use old one (not recommended)
    
    You now have to allow “less secure apps” on your account. Otherwise, you won’t be able to connect to it with RavenDog
    https://www.google.com/settings/security/lesssecureapps
    
    Set "sender@gmail.com","recipient@gmail.com","senderGmailPassword" fot it to work




RVN Cheese is welcome & appreciated, KAAAW ! RTEsqHCxn2HvMjstsr3VRqLuurjZseNCrE
