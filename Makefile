#############################################################
#           After Grad Project by Konnor Mascara
#                IM-assist | File: Github Setup
# 
# Note: Parts have the code has been influenced by similar 
# projects this may also include similar styles and blocks 
# of code copied from the imported files. This is a side 
# project and should not be taken professionally.
#
# Description: Quick commands for the file.
#
# Done   Name     Description
# ----   ----     ----------- 
# Yes | Start | Quick start of the program
# Yes | Build | Get rid of API, commit, put API back.
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
	@git commit -m "Auto Update"
	@git push origin master
	@echo Uploaded!

	@echo Creating
	@python -c "from MK_manage import setup; setup.create('')"
	@python -c "from MK_manage import setup; setup.convo()"