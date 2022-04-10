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
    /register_node | POST | -> 
    /register_with