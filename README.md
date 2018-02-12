# ravendog
Watch dog for RVN miner

# If GPU Load falls under 15% and stays there for 3 seconds RavenDog will restart the miner
# Set miner name in minerList 
  ---your.bat will need title %~n0 as the first line (check RVN_miner.bat)
  ---RavenDog will search all folders in the directory and folders under(for "minerList:" name)
# Set GPU_checkNR 
  ---If you wish to check GPU load on second or third GPU
# Set how many seconds to check after
# Explorer info is taken from http://threeeyed.info/ API
# Log file will be created in the same directory everytime RavenDog is started (i.e. when PC freezes and restarts)
# Set "sendEmail:" to True ,to receive notifications , or False to disable it
  ---Create new Gmail account or use old (not recommended)
  ---You now have to allow “less secure apps” on your account. Otherwise, you won’t be able to connect to it with RavenDog (https://www.google.com/settings/security/lesssecureapps)
  ---Set "sender@gmail.com","recipient@gmail.com","senderGmailPassword" fot it to work

  
  ________           _      ____     ___ __________ ___      ___________      ____       ____   
`MMMMMMMb.        dM.     `Mb(     )d' `MMMMMMMMM `MM\     `M'`MMMMMMMb.   6MMMMb     6MMMMb/ 
 MM    `Mb       ,MMb      YM.     ,P   MM      \  MMM\     M  MM    `Mb  8P    Y8   8P    YM 
 MM     MM       d'YM.     `Mb     d'   MM         M\MM\    M  MM     MM 6M      Mb 6M      Y 
 MM     MM      ,P `Mb      YM.   ,P    MM    ,    M \MM\   M  MM     MM MM      MM MM        
 MM    .M9      d'  YM.     `Mb   d'    MMMMMMM    M  \MM\  M  MM     MM MM      MM MM        
 MMMMMMM9'     ,P   `Mb      YM. ,P     MM    `    M   \MM\ M  MM     MM MM      MM MM     ___
 MM  \M\       d'    YM.     `Mb d'     MM         M    \MM\M  MM     MM MM      MM MM     `M'
 MM   \M\     ,MMMMMMMMb      YM,P      MM         M     \MMM  MM     MM YM      M9 YM      M 
 MM    \M\    d'      YM.     `MM'      MM      /  M      \MM  MM    .M9  8b    d8   8b    d9 
_MM_    \M\__dM_     _dMM_     YP      _MMMMMMMMM _M_      \M _MMMMMMM9'   YMMMM9     YMMMM9 

RVN Cheese is welcome & appreciated, KAAAW ! RTEsqHCxn2HvMjstsr3VRqLuurjZseNCrE
