#############################################################
#           After Grad Project by Konnor Mascara
#                IM-assist | File: Github Setup
# 
# Note: Parts have the code has been influenced by similar 
# projects this may also include similar styles and blocks 
# of code copied from the imported files. This is a side 
# project and should not be taken professionally.
#
# Description: Delete json, upload, create json
#
# Done   Name     Description
# ----   ----     ----------- 
# Yes  | Make | Allow make for easy sending.
#
#############################################################

build:
	@echo Deleting
	python MK-reset.py

	@echo Uploading!
	git add .
	git commit -m "Auto Update"
	git push origin master
	@echo Uploaded!

	@echo Creating
	python MK-create.py