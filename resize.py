from PIL import Image
import os, sys
import exifread
'''
def rename(dir, pattern, titlePattern):
    for pathAndFilename in glob.iglob(os.path.join(dir, pattern)):
        title, ext = os.path.splitext(os.path.basename(pathAndFilename))
        os.rename(pathAndFilename, os.path.join(dir, titlePattern % title + ext))


def rename_images(dir, file_type, file_pattern):
    for file in os.listdir(dir):
        if file_name.endswith(file_type):
            pass
'''




def resize_image(infile, output_dir='', size=(1024, 768)):
    # create outfile name
    outfile = os.path.splitext(infile)[0] + '_resized'

    # get file extension (I dont think this is nessisary)
    extension = os.path.splitext(infile)[1]

    print(f'full: {os.path.splitext(infile)}')
    print(f'outfile: {outfile}')
    print(f'extension: {extension}')

    basewidth = 300

    # Open open image with pillow
    img = Image.open(infile)

    # Open image file for reading (binary mode) in exifread
    img_exif = open(infile, 'rb')

    # Return Exif tags
    tags = exifread.process_file(f)
    print(tags)

    width_percent = basewidth / img.size[0]

    print(f'width_percent: {width_percent}')
    print('here')

# hsize = int((float(img.size[1]) * float(wpercent)))

# img = img.resize((basewidth, hsize), PIL.Image.ANTIALIAS)

# img.save(‘resized_image.jpg')


if __name__=='__main__':
    # get current working directory
    dir = os.getcwd()

    # make new folder to store marked images
    output_dir = 'resized'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # for each file in the dir, if it is a jpeg, resize_image
    for file in os.listdir(dir):
        if file.endswith('.jpg'):
            resize_image(file, output_dir)
