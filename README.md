## Blockchain Based Voting System
This project is split into three folders that together make up the system. 

### Client 
Here runs a flask web-server that connects itself to a given node. 
All necessary API of the Node-Server can be called with the web-ui from the client. 


### Node

    -) Admins.csv store all the addresses of admins I am using to run my server
    -) Admins.py consist of functions and classes to create the csv file
    -) C_Node.py is the Blockchain Network Node Script
    
    
    API:
    
    
    ------Registration------
    /register_node | POST | -> endpoint to add nodes to the network
            -node_address: ip of node that wants to connect
            -admin_address: crypto address the admin that wants to connect
            -admin_signature: a signature to proof that the admin is actually him 
            -admin_text: some text to verify the signature from
            
    /register_with | POST | -> endpoint to add yourself to a network
            -node_address: ip of node that it wants to connect to
            -admin_address: crypto address the admin that wants to connect
            -admin_signature: a signature to proof that the admin is actually him 
            -admin_text: some text to verify the signature from
            
    
    ------Adding Data------
    /add_admin | POST | -> endpoint to add admins
            -admin_address: crypto address the admin that wants to connect
            -admin_signature: a signature to proof that the admin is actually him 
            -data: dictionary with "address" and "pub_key"
                {"address":_address_
                "pub_key":_pub_key_}
                
    /add_user | POST | -> endpoint to add new users
            -admin_address: crypto address the admin that wants to connect
            -admin_signature: a signature to proof that the admin is actually him 
            -data: dictionary with "hash" and "prefix"
                {"hash":_hash_
                "prefix":_preifx_}
                
    /verify | POST | -> endpoint to "users" and decrypt their hash to add the address
            -prefix
            -password
            
    /vote | POST | -> endpoint to cast a vote
            -user_address
            -user_signature -> ballot is the data to create signature
            -ballot
            
    /add_block | POST | -> internal endpoint for add blocks to pther peer
     
     
     ------Getting Data------
     /chain | GET | -> returns copy of the blockchain
     
     /mine | GET | -> starts to mine the last added data by starting the process
     
     /pending_votes | GET | -> returns the all unmined votes
     
     
     
     