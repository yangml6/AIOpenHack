from PIL import Image, ImageOps
import os

im_pth = "/Users/yml/Desktop/gear_images/gear_images"
out_pth = "/Users/yml/Desktop/gear_images/gear_images_a"


def travel(orgpth, outpth):
	fs = os.listdir(orgpth)  
	for f in fs:
		tmp_path = os.path.join(orgpth, f)
		if not os.path.isdir(tmp_path):  
			print('do with file: %s'%tmp_path)
			img = processfile(tmp_path)
			img.save(os.path.join(outpth, f), 'JPEG')
		else:
			print('do with dir: %s'%tmp_path)
			outpth2 = os.path.join(outpth, f)
			os.mkdir(outpth2)
			travel(tmp_path, outpth2)

def processfile(im_pth):
	im = Image.open(im_pth)
	old_size = im.size  # old_size[0] is in (width, height) format
	newr = max(old_size)

	new_im = Image.new("RGB", (newr, newr), (255,255,255))
	new_im.paste(im, ((newr-old_size[0])//2, (newr-old_size[1])//2))

	im = new_im.resize((180, 180), Image.ANTIALIAS)
	im = ImageOps.autocontrast(im)

	return im

travel(im_pth, out_pth)
