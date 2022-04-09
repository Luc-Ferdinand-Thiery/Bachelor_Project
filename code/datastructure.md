## Transactions 

a transaction can b


Block: 

    -Created Admin Address
    -Created Admin Signature

    -index -> int
    -timestamp -> date
    -previous_hash -> str
    -nonce -> int
    
    -admins -> dict -> "Address":Pub_key
    -unverified_addresses -> dict -> "hash":prefix
    -verified_addresses -> dict -> "Address":[pub_key, token]
    -votes -> list
    
    
    
    
Blockchain:

    -unconfirmed_admins
    -unconfirmed_votes
    -unconfirmed_unverified_addresses
    -unconfirmed_verified_addresses
    -chain
    -admins
    
    
    +create_gen_block(self)
    +add_block(self, block, proof)
    +proof_of_work(block)
    +mine(self)
    +add_new_vote(self, vote)
    




[{'vote': 'Candidate', 'timestamp': 1646985418.943041, 'index': 1, 'hash': '6dbf23122cb5046cc5c0c1b245c75f8e43c59ca8ffeac292715e5078e631d0c9'},
 {'vote': 'Candidate', 'timestamp': 1646985455.5303009, 'index': 1, 'hash': '6dbf23122cb5046cc5c0c1b245c75f8e43c59ca8ffeac292715e5078e631d0c9'}, 
 {'vote': 'Candidate', 'timestamp': 1646985467.2061708, 'index': 2, 'hash': '003bd90b354b091e242c6eaf9564b17c94f78f72a40aafdfae13a37c28fec14a'}, 
 {'vote': 'Candidate', 'timestamp': 1646985573.3712661, 'index': 3, 'hash': '002c9d9ac14923baa5711640c0c8f9c825a96714721807806b9a5cb774a55416'}, 
 {'vote': 'Candidate', 'timestamp': 1646985603.83854, 'index': 3, 'hash': '002c9d9ac14923baa5711640c0c8f9c825a96714721807806b9a5cb774a55416'}, 
 {'vote': 'Candidate', 'timestamp': 1646987190.8770618, 'index': 3, 'hash': '002c9d9ac14923baa5711640c0c8f9c825a96714721807806b9a5cb774a55416'}]


{'length': 1, 
'chain': [{ 'index': 0, 
            'timestamp': 0, 
            'previous_hash': '0', 
            'nonce': 0, 
            'admins': '{    
                "Address":{
                    "0":"b\'3WCZL2zjR8sTbA8qbL6FuHcszCXuZsux6acmQbCUUHqaxBEDbPf7TzN\'",
                    "1":"b\'3oY4fvjTYRrJvtadWMyjPUm6igHkbiUuB3yoybg22T95Q9UyZmThbhn\'",
                    "2":"b\'3k3fXjVLCp2XU3H8jfFaXD96MCs8CujDPCkyAUvsd6PxG3TiJnKdXoa\'",
                    "3":"b\'3qquCjai1ctrYWdjhBmrWUxYDLDMMqRUG94w3VpwogqLARJkVNwaqGR\'",
                    "4":"b\'3rRCrMQsbhLC8zJExV5X6CYCUihuxeFxyK8815WBA8RerbapDrywez8\'",
                    "5":"b\'3hERPFwthWhKS69pn5SZMURBWfPCWzhbqhGru6CX9G6EXiryzqwDwhB\'",
                    "6":"b\'3oVaJ8jMjGZUe5WdsxvxxDX3pWjXwNXrafcyn59S6CBhiCXkYN8TWKj\'",
                    "7":"b\'3Yd4FT58PPYsYxbiviA4ECpevWJoj7x9T8PnQ2yX3Y3qSqcmsLHhnQA\'",
                    "8":"b\'5taKL6iC2JTA12XckxEFxw4aVsTL4kR1YRWzgmoKsK1ToSLAA8Yrsaj\'",
                    "9":"b\'62fm2QR8kgQ2rHEzjsnETHdqodZAtkon4hv9R8bmyZFYU9nqi13twB6\'"},
                "Private_key":{
                    "0":"Private RSA key at 0x7FBFCD126C10",
                    "1":"Private RSA key at 0x7FBFCD181A90",
                    "2":"Private RSA key at 0x7FBFCD181F40",
                    "3":"Private RSA key at 0x7FBFCD190190",
                    "4":"Private RSA key at 0x7FBFCD1905B0",
                    "5":"Private RSA key at 0x7FBFCD1909D0",
                    "6":"Private RSA key at 0x7FBFCD190B20",
                    "7":"Private RSA key at 0x7FBFCD190FD0",
                    "8":"Private RSA key at 0x7FBFCD1953D0",
                    "9":"Private RSA key at 0x7FBFCD1957F0"},
                "Public_key":{
                    "0":"b\'-----BEGIN PUBLIC KEY-----\\\\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAjTJIFnEzXCC1cZaVu8nQ\\\\nO7uax53kYzHbKOZBc+R68I+ojPgwYI7Zkzbj7vBZbGyvebcCArD7Czc3bq3qRvA8\\\\nEDid+o8aVlJfbAGK6R\\/NizayvzfzuYP8X7hNduyihlYRavuCL024i47aH+kp8arN\\\\nJUffR1gRfalssLbUBodOATxBUV+4HROfCtnMaXuvjhD7x07hluQiqxcfjDPo+qEV\\\\nt+t+ziymE1pAE+IotFH9eCiHOWFqqox+OkejV9sFBVkrI1D5cHplvjOjr\\/vbmm+M\\\\nqvqcZ8xVRVxcSKmc5NKOkTojLwFoMrroupwpkAxuWXa12yq2ZZbHzuMW0QfSVWT\\/\\\\nGwIDAQAB\\\\n-----END PUBLIC KEY-----\'",
                    "1":"b\'-----BEGIN PUBLIC KEY-----\\\\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAxRF1NaarrbBiRpaGqVN7\\\\nwhUZPIgND2C\\/b17pnRkCAVhDr7nhLYAukMmyaykk6Al4CFEkvDbpJI34UtrMJX68\\\\n81r\\/zfIzAiGVjQ5JREMifgyJvqmFlyU+\\/aV6LCW8dG3X6A5BKmJVXJA8eK+gQ3q0\\\\naxmWKw+uTjLU0XBkV6KqcctmFOpvNoycHwp5kcPrQWjqNiM5lGcc017dw8p3mwzE\\\\nVerkc8D9tKprZWl1XwnPnDdaSVfxrsAKu7m7s8SiEtUVa6Ymfskxqg7pZ4XOzUuT\\\\nGIWHFkUawMA4QYoRSKszvBMg4fQ\\/eD3ke7ikminZ1sbzfiofZABS3z3G3+jbNiTL\\\\nuwIDAQAB\\\\n-----END PUBLIC KEY-----\'",
                    "2":"b\'-----BEGIN PUBLIC KEY-----\\\\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAss7NUKPvlQ5\\/s50CsJe\\/\\\\nYFFwY0Ur\\/0xUk3iwSv0aJukLLAN6VtEzLdjSvs6VdZMWPSR3qTCoLOfSh+SNKYiK\\\\nmEHk6R7\\/8mpLOpPv\\/qH2lnIfuiN9s+wKCwAAqsnDp\\/Gr77jgZRR6yTAPEkxqyAz0\\\\ng4QFOo3ClKdedCr8OlYOyKytWPi99aMqerLiopjFDoPV9eIpLfajaIeO1B84WE5F\\\\nsV3s4TWKEyqqwU4K2+SOq9uCrZKop708Z\\/\\/C1u5keZHENccGGN\\/fvvrwpw7FvqhF\\\\nFZamEqIu\\/RXyVVJvF7eW5vkGVdi3GaD3WRxQdiOIO0X8X7xtPYXGYa2clWPrZJyK\\\\nLQIDAQAB\\\\n-----END PUBLIC KEY-----\'",
                    "3":"b\'-----BEGIN PUBLIC KEY-----\\\\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAlXoMkZlMaTttaiAa8HAB\\\\n2lnSoi3K8\\/9Hjxjy42rBxUmln5KwGniNt7zJpx30M1fZ0YOdb8Tc1gzpWxomVK5n\\\\ntrxzPkP87bxnnOZXVt3KTHwJbLtwmJ3i+3POIA0slu5dHyuG8LCgH\\/BB3cgpeqis\\\\nbeb++kAJogaNSDG5puT9wc4PQrzL1eqfCK3ZB\\/h\\/RN\\/N7pqN4MWcJBVD74WPDF9+\\\\nIyQqyvXUD+79T+aEwvJa45xfsKUUJ6OmMHOSL8z4dCcxetNFUFULtmOVqFlyhe\\/R\\\\n3NYzpHYZSsEbVy9yFyqthXIaXjUpOK3qbuOi6JJziOcixCFMU9nWx0YJtevYOhav\\\\nfwIDAQAB\\\\n-----END PUBLIC KEY-----\'",
                    "4":"b\'-----BEGIN PUBLIC KEY-----\\\\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAlExfb6kRMHYInw6T0ohc\\\\np+bv2z2GZzlswVt2WcOLmoc8iZpyRg\\/sLiUPTSJRXUuPF11x58vlwhNWo0WMkkXj\\\\nzj50y0OT15jIKXNDeU+DqvwoYkmiFb3vzUZbOBsizmRkMgoLdYWSdlhjwt1OUvV4\\\\nGfhqtOBTrykVpEKUCwjNeDODIqyoaHOc26VPnFkfhS47V\\/OC4\\/dQZi3L5LOdPCxt\\\\nLqcF1ePYpZqVM3eiVlwW9BFfcpAR4rYMY\\/3wVret5MoW\\/D5+nywDonE5d2OvVyuU\\\\n\\/Yp7NdoXZVLPyVU9mTbQUvBkiiPf9LVRa00KLFyjWRXlIGG4OTEjNapJ\\/MHURiZV\\\\n5QIDAQAB\\\\n-----END PUBLIC KEY-----\'",
                    "5":"b\'-----BEGIN PUBLIC KEY-----\\\\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAxQJYkUQAtx9Aa\\/BpDOAe\\\\nezvIrlu4qUVCPR1ffcKZClNI1XWVSqpHRIAaPDdPpWrI6r\\/vwE03BaYSJcsBdMb5\\\\nNWL6W9zSpMciV8TqTh54rS2+AginQwDbe+W+I9T4CfbwATCKS1eZ5D+hzwXrMHBa\\\\n+iHycQ67e+6UBU1\\/MNd0E4kr2GiMbcz2mtBCzcuFHkpl0SObAgSmGK9hTCHKWcWP\\\\nRytw18f1aV9u44iiHC49VcPQlLlSKbW5a3j6kcOfk804uHlQuaBQk9eWKXPMlMKs\\\\nXv8qLxmuwIGw4ujALIDW19jnspX0At7wd8Ek8txICUjwqm1NRDw1gsu1jzoYEm5e\\\\nlwIDAQAB\\\\n-----END PUBLIC KEY-----\'",
                    "6":"b\'-----BEGIN PUBLIC KEY-----\\\\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEArQJpxOFe\\/Zb7TSg7tq8f\\\\nAWxWW5hOk0NYa09tlMit3m5zGhXQLtjKMA4Vrw0kmIHqqpaobBgWOc\\/s4UsA4vbH\\\\n1h7jON+QIUicvJ3nrExghVrGXvayhZLvHqpZvOk1rmDoI5b\\/3h0sF\\/QV0tw5sVeA\\\\nJdobZ5zwNeJ4xpDwrHhuo291ZVwxgKPSkfumY2OI8ul7iX866ZIcIu+hZpkxoqno\\\\nKfLWo1ot7JCmqWad5mM3kcj09pCWbScNugvN8zZwqKyZyKyevekf0HugimWKnk5m\\\\nd93qTYSe5z6TT9\\/R9SdydDeiHGnn2aodRZcXA60uu4r5taPullqf8WngwyN0Rbgf\\\\nIQIDAQAB\\\\n-----END PUBLIC KEY-----\'",
                    "7":"b\'-----BEGIN PUBLIC KEY-----\\\\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAsJ6ydEJkOH2y2S\\/HitkD\\\\nCLFLJKBDinUgLl4jteUz0+2oSzChvl6pn\\/RxT4wmeKTWifUEaBjYPBob5OtW8JPv\\\\na8sFns521TKAebQzNDmLv7zz4CQeWLOLd\\/H0if3xOcsyQn\\/6hJPG5e6NYTqnaltc\\\\nsrBk7VNXRylPTt\\/38axdeVZsEQN\\/gw4WEdPITvj7hdPu2u3sQcTjXzrtj4z2r2Ob\\\\nvalwtRW1LZX\\/NYlH2A0enM0FRrGni\\/eSDfb5oZ\\/VOi0UYdG85ZmmcUn+HO2ql7Gs\\\\ndxxnsumOcIC9BXNtDpR2txouclEcGakmVnq6hH8tNMTUKb84roRTkDXxayMHkX7b\\\\n+QIDAQAB\\\\n-----END PUBLIC KEY-----\'",
                    "8":"b\'-----BEGIN PUBLIC KEY-----\\\\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEArTD5mNcV8FuFWN9HIYXo\\\\n484WjVg4ceS8tnKOW4\\/s37vOZ152lJtfFCQ3WaQ5zm568TaM9rlL+8opuLgdOssN\\\\nBJ3rte+2glfFv4axQCD6JcCyk0he3Os2QjznBG4yOljOTGqOcNMFZegRCjHi9eie\\\\nrw6v\\/3qhA33CaaWOpQ8+gMU3HfNyRaKE58sRYTmQeATXhjGZEP17\\/lM3HMt5yIW9\\\\nNOHN8iaadyEPL9HIft0m1DwPn+QI4uVUPPGJL\\/1NxQGlk0VxYHeheZLK9UHHR43T\\\\n1vpVohO67kANTl7EflzR+lIi4XZ2kjGLnO6kGnpkbSZp3br7c6Xd2bYZi4+B0pmC\\\\n0QIDAQAB\\\\n-----END PUBLIC KEY-----\'",
                    "9":"b\'-----BEGIN PUBLIC KEY-----\\\\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA46KNlQzpvMkkADHJ83s5\\\\nwTnmX5\\/8YhsDx5vHj+AEdxsXyp+5vm5CWccGBN2RPth4hu1jMWsQ2DHPU85FxzXo\\\\nRS1adKw42J6fx5pIxjzNEX+BPR6skyBLWc7UDPXZLRf+sYyBcVy0TA2e5ZxMKnPx\\\\nlEl3jpFyy\\/1YO25wxRva73K3RLYeRKyiBAG0OAA9tcma7WZqt\\/qhzGWJ3AWVOgBr\\\\ngxN3pGJ449o+0cz71BAFI6Bh9vHFcjsNzzgwGJKustXCrWVFzq5DzpgpcRtguVzY\\\\nasdCDQj\\/sBJyReH1\\/FJjUABb+FBGlwxu8ev+FfEl07ZvputD+xLqr5F2cvoDF7Lt\\\\nRQIDAQAB\\\\n-----END PUBLIC KEY-----\'"}}', 
            'ballots': [], 
            'addresses': [], 
            'transactions': [], 
            'hash': '68f6d0703281821db7b61102209a74435468509ff6ee2b0424cbe046287f8f83'}], 
            'peers': []}

curl - X POST \
    http: // 127.0.0.1: 8001 / register_with \
    - H 'Content-Type: application/json' \
    - d '{"node_address": "http://127.0.0.1:8000", \
        "admin_address": str(b'3WCZL2zjR8sTbA8qbL6FuHcszCXuZsux6acmQbCUUHqaxBEDbPf7TzN'),\
        "admin_signature: "
                                                                                  '}'