def PrintCert(name):
	from PIL import Image, ImageFont, ImageDraw
	import os
	my_img = Image.open("Cert.PNG")

	font_i=ImageFont.truetype('tango.ttf',90)

	img_edit=ImageDraw.ImageDraw(my_img)
	img_edit.text((260,280),name,(0, 0,0),font=font_i)
	my_img.show()
	# path_save=os.getcwd

	rename=(os.getcwd()+"/s_cert/"+name+".PNG")
	my_img.save(rename)

