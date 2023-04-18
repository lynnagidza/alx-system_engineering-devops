## Learning Objectives
- What is a server
- Where servers usually live
- What is SSH
- How to create an SSH RSA key pair
- How to connect to a remote host using an SSH RSA key pair
- The advantage of using #!/usr/bin/env bash instead of /bin/bash

## Tasks Explained
Task 0:
    File 0-use_a_private_key: This file contains the private key that you will use to connect to your server using SSH.
    This script uses the ssh command to connect to the server with the given IP address and the specified private key file ~/.ssh/school. The -i flag is used to specify the private key file, and the ubuntu username is provided as an argument to ssh.

Task 1:
    File 1-create_ssh_key_pair: This file contains the public key that you will use to connect to your server using SSH.
    This script uses the ssh-keygen command to generate a new RSA key pair with 4096 bits. The -t flag is used to specify the key type, which is rsa in this case. The -b flag is used to specify the number of bits, which is 4096. The -f flag is used to specify the filename of the private key, which is ~/.ssh/school. The -N flag is used to specify the passphrase for the key, which is betty.

    After running this script, there should be two new files in the ~/.ssh directory: school (the private key) and school.pub (the public key).

Task 2:
    File 2-ssh_config: This file contains the SSH client configuration.
    This script uses the ssh command to connect to the server with the given IP address and the specified private key file ~/.ssh/school. The -i flag is used to specify the private key file, and the ubuntu username is provided as an argument to ssh.