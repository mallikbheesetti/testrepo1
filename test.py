#!/usr/bin/python

FTP_RANGE_LOW = 30000
FTP_RANGE_HIGH = 39999
C_TYPE = "ftp"
UIDS = list()
COUNTS = dict()

if (C_TYPE == "ftp" or C_TYPE == "export"):
	PFILE = open("/GitHub/users/mallikbheesetti/testrepo1/passwd")
	for LINE in PFILE:
		COLS = LINE.split(':')
		UIDS.append(COLS[2])

UIDS = [int(NUM) for NUM in UIDS]
UIDS.sort()
print UIDS

for UID in UIDS:
	if UID not in COUNTS:
		COUNTS[UID] = 1
	else:
		COUNTS[UID] = COUNTS[UID] + 1
	print "%d\t%d" % (UID,COUNTS[UID])

for NUM in range(FTP_RANGE_LOW,FTP_RANGE_HIGH+1):
	UID = NUM
	print UID
#	print "%d" % (COUNTS[UID])
	if UID not in UIDS: break
print "New User ID : %d" % (UID)
