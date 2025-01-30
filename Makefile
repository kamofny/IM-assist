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
# Yes  | Make | Allows for easy github updating.
#
#############################################################

start:
	@echo Starting
	@python MK_screen.py

build:
	@echo Deleting
	@python -c 'from MK_manage import setup; setup.delete()'

	@echo Uploading!
	@git add .
	@git commit -m "Incomplete Save"
	@git push origin master
	@echo Uploaded!

	@echo Creating
	@python -c "from MK_manage import setup; setup.create('')"