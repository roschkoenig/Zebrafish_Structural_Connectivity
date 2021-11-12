def housekeeping(base, atlas):
    
    import os
    
    F = {}
    F['base']  = base
    F['code']  = F['base'] +os.sep+ '01_Code'
    F['data']  = F['base'] +os.sep+ '02_Data'
    F['outp']  = F['base'] +os.sep+ '03_Analysis'
    
    if atlas == 'Ashourvan':
        F['atlas'] = '/Volumes/GoogleDrive/My Drive/Research/2003 Zebrafish Structure/02_Data/Atlases/Ashourvan'
    else: 
        F['atlas'] = atlas
    
    return F