def novaPuller(ip_address: str, username: str, password: str):
    '''
    This Function takes in 3 varibles:\n
    ip_address= string of the ip address of the target computer\n
    username= stirng username of the target computer\n
    password= string password of the target comptuer\n

    the return should be a dataframe of the data in the target computer
    '''
    from smb.SMBConnection import SMBConnection
    import os
    import shutil
    import pandas as pd

    # Define Connection parameters
    ip_address = ip_address
    serverName = 'Export'
    username = username
    password = password
    working_directory = os.getcwd() + '/temp'

    # Create Temp Directory
    if not os.path.exists(working_directory):
        os.mkdir(working_directory)

    # Create Empty DataFrame to store sample data
    df = pd.DataFrame()

    # Establish connection
    try:
        conn = SMBConnection(username, password, 'mac', 'windows',
                             use_ntlm_v2=True, is_direct_tcp=True)
        conn.connect(ip_address, 445)
    except:
        raise Exception('Connection Error')

    # Pull files and copy them to temp directory
    files = conn.listPath(service_name=serverName, path='/Results')
    for file in files:
        if 'SampleResults' in file.filename:
            with open(os.path.join(working_directory, file.filename), 'wb') as local_file:
                conn.retrieveFile(serverName, '/Results/' +
                                  file.filename, local_file)

    # Close connection
    conn.close()

    # Navigate though files and add to empty dataframe
    for root, dirs, files in os.walk(working_directory):
        for file in files:
            sample_df = pd.read_csv(root+'/'+file)
            df = pd.concat([df, sample_df])

    # Delete Temp Directory
    shutil.rmtree(working_directory)
    return (df)
