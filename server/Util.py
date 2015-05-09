from datetime import datetime
import random

def returnRId(basic):
	now = datetime.now()
	sec = (now - datetime(1970, 1, 1)).total_seconds()
	random.seed(sec)
	return basic+str(random.random())
