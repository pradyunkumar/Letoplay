from dejavu import Dejavu

def createDJV():
	config = {
	    "database": {
		"host": "127.0.0.1",
		"user": "root",
		"password": 'password', 
		"database": 'dejavu',
	    }
	}
	
	djv = Dejavu(config)
	return djv


