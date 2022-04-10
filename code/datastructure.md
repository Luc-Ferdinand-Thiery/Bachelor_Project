
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
    
genesis_block=[
{
    'owner': "b'3eqLZijdad7VCLHPXfsViZJGpKFGupeQrjzz7DDD4SxTDXaS7F4g4Dv'", 
    'signature': 'b"\\xa1\\x91\\x96[\\xbb\\x8bW\\x91|/\\x86t\\x07-\\xd7\\xee\\x05\\xe7\\n\\xabk&\\xe1`{\\xa3\\x07&\\xc5\\x91\\xa6L\\xee\\xb2\\xf2\\x92tT\\xa6\\xbf\\xb8V\\xd9\\x1e\\xc1k\\xde\'\\xba\\xe0\\xac\\x9d\\xde\\xe6\\xe6\\xf0E3j#\\x82\\xe0\\x0f\\x8f\\xf9\\xce\\x81\\xda\\xf1R\\xe5\\xb1{H\\xde\\xdf\\xfa\\xd3\\n\\x83e\\x9e{\\xef\\xfd\\xe3N:\\x99*6;h\\xee\\x8coIk%[|\\xc1,\\xfbx\\xf7\\xad\\x9c\\x89\\xe5\\xc2\\x13\\xb3\\xday\\xcb\\x02&N)0\\x7f\\xec\\x93\\xf3\\x11\\xfa 8\\x8a\\x86\\r\\xd2=\\xd3\\xc1\\xf1\\xda\\x88a\\\\\\xfa\\xfeH-\\xc6\\xf90\\xbc\\x1e\\xe7\\x9d\\xc1E\\xd1km\\xb62\\xcd\\xb3\\x91\\xe4\\xb2OR\\x95\\x00\\xc7\\x1b\\x14\\xec>F\\x91\\xccy\'\\xba\\x061\\xf1E\\xb7\\x01\\x97\\x95=\\\\/\\xa2YNlD\\x018\\xdd\\xcah{\\\\\\xf0\\xf4C:4=eJ\\xf1\\\\Z&Lx\\x8bny\\x05*\\x9a\\xb0*\\x81 q\\x02}<B\\x04\\xb9\\x9f\\xc1\\xccWC\\xdb\\x9c3\\x104x0\\x04\\x8d\\x1cB\\xe8\\xb6\\x9eB\\xacVd"',
    'index': 0, 
    'timestamp': 0, 
    'previous_hash': 0, 
    'nonce': 0, 
    'admins': '{"b\'3oVTdqiUxVL7kfnF764hSEayvvSDZVqXsdfZnsocipbWgWtctZgcnfa\'": "b\'-----BEGIN RSA PRIVATE KEY-----\\\\nMIIEowIBAAKCAQEAuTn+9keE0K6BtAdjhTlyOIA8I1E9mw+dQhhGK8LL9tsKUxep\\\\nVq1Q93wptNYYlayOqaxBExY1X0QklpZkuQmnxedi2o2iVhaZdgrLjE/2tlPdOj4l\\\\nxzgUSMsWk61tTABF/uzG0n1GB5NM5fvWE73BRTwkKCS15sy/57TWg3LHuUmzWT+I\\\\nmGpXek6xmDvK8p2ZOPTNCeCsPI4/zL2KX5HQ3jeYREauz2BzQCbEkUn/1SflqbjL\\\\nwKqOciegtsUWhXaVHrq7IT57EOSqPaNoj+29YRohNQsV1tP1CbpzFQobYfxuKvso\\\\nv1CLNw8P81l9h0+qMkyBq88taFsfJGbGB2qrWQIDAQABAoIBABbjsJr5IBPUuNEJ\\\\nR7ZfMLsEN8pKgBExJwcTrlo6jo+BJn+5sRK1xMdsl8/R1ERsyE117K3B5RMSfe4B\\\\nBE3sgEffzfLBpXG7hbfVYi2C9TM3XmOT6gG6L6GGPVI/EH5fm0bDNletJPILNSnH\\\\niv8yCBf49GPkk3kDzORCj+67CKzgFaAS0chzG24ZEE3PIAGNYW5+MEnSKsbziMEZ\\\\nEpDjq1ag6HefEWwpEEHGs9ah8uPAmFBNa0jsDAD/iYP4CAGfPxb5DPQgF6pDI+Nc\\\\nF2DB930PBk5uRi30Yk4UpuR2cqAvSjYSAl00hamvvYiDcRnzGTauUQnuoHNhtAwt\\\\nmvMVgWECgYEA17Bt/RLcZC922QqiyNDw8jamUcp9pVLbgnSKOfa7PcVhGB1opgWq\\\\nSkATJcnkJ1f6TUhpnnCWZI0I8yk6RYWjfk+tpCnLxLC2AUUQluo93w0ulRkmI05w\\\\nbxwVThdW1YvkyQwCSUTJ/a07B9N+uMwhMDkiePXneBmvjU9drHQRIUkCgYEA29gX\\\\nvz4eqfWBNuOD8jvuEcRrLJwnt0q7AcqaEorb1JdPEr3NloLf2SSmhfJaueh0U/jI\\\\nuM3V+UMKCUrUCI5+0Yt0/lZEp9b8a10LxDGxF+2RLdmTCvnJduotYjcyGLOBiIS9\\\\nq3tJrzhPQXLe4czCGNfi0WzPYVnzNSfraAZxSZECgYAwlwJwPMuBll/DzW2Wp9tf\\\\n9YfKbT+Y+u2Qmgh5vme4JrsU36svm58dUwn9PVo0stEkj+ebVenLhSo6/VKvTsfi\\\\nMLkBfpj1GoomBxURqnt9wE56MEwzL/yMS1tRWFirivRjhl0NfH20tE3UGYU2xGXF\\\\no1lsvpkCqWavAu4rZ4pkYQKBgQCqRJUv0ybgr3piTpf01qGuNRhktpS0CzcHTilC\\\\nTzWvU3k0pLhD6B0DCrXGbEwETJs8JiUfrJwar+doBwJtlh92n7H/AkWuUH2zkZ75\\\\nVxs30xFsF2UhTRDR/tEjjmhIZU7fsx9LXvNUuCH6KMOi0nlJ0HqlhMahOY96De7u\\\\n5H59YQKBgFmCzgtV2yrInuaj2Kq9e1+9Vc5a5PIfFeLFgqBGpGhOysYk/p+PyyfA\\\\n3dIJehcfBPrbRHrTD0mbqJkSItjtFA/PEcQLZu/A3pQlP9Ri5S990pUCwsJXXrco\\\\nugsu3H3sZ6WBFtFFcYvuu1xJ9toBo5tUfbGxQFZcbGx8HQs3ns2x\\\\n-----END RSA PRIVATE KEY-----\'", "public_key": "b\'-----BEGIN PUBLIC KEY-----\\\\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAuTn+9keE0K6BtAdjhTly\\\\nOIA8I1E9mw+dQhhGK8LL9tsKUxepVq1Q93wptNYYlayOqaxBExY1X0QklpZkuQmn\\\\nxedi2o2iVhaZdgrLjE/2tlPdOj4lxzgUSMsWk61tTABF/uzG0n1GB5NM5fvWE73B\\\\nRTwkKCS15sy/57TWg3LHuUmzWT+ImGpXek6xmDvK8p2ZOPTNCeCsPI4/zL2KX5HQ\\\\n3jeYREauz2BzQCbEkUn/1SflqbjLwKqOciegtsUWhXaVHrq7IT57EOSqPaNoj+29\\\\nYRohNQsV1tP1CbpzFQobYfxuKvsov1CLNw8P81l9h0+qMkyBq88taFsfJGbGB2qr\\\\nWQIDAQAB\\\\n-----END PUBLIC KEY-----\'"}',
    'unverified_addresses': {}, 
    'verified_addresses': {}, 
    'votes': [], 
    'hash': 'e120ebfb3fa5256c191567a8a7fe6f3ed07ce3e78052d69609a89048f2f2e735'
    }
    ]

                                                          '}'