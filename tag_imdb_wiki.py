import sys
import shutil
import os.path


def main(directory):
    with open(directory) as f:
        lines = f.readlines()
    for line in lines:
        age = line[-4:]
        age = age.translate(None, 'g\t\n ')
        age_num = int(age)
        fullpath = '/home/crystalcampos/AGE_REGRESSION_AD/imdb_crop_pico/' + \
            line[:-4]
        fullpath = fullpath.translate(None, '\t ')

        if(age_num >= 0 and age_num < 20):

            print 'directory : ', fullpath, 'age : ', age_num
            if os.path.isfile(fullpath):
                shutil.copy(
                    fullpath, "/home/crystalcampos/AGE_REGRESSION_AD/new_tagged_images/young/")

        elif(age_num >= 20 and age_num < 30):

            print 'directory : ', fullpath, 'age : ', age_num
            if os.path.isfile(fullpath):
                shutil.copy(
                    fullpath, "/home/crystalcampos/AGE_REGRESSION_AD/new_tagged_images/young_adult/")

        elif(age_num >= 30 and age_num < 60):

            print 'directory : ', fullpath, 'age : ', age_num
            if os.path.isfile(fullpath):
                shutil.copy(
                    fullpath, "/home/crystalcampos/AGE_REGRESSION_AD/new_tagged_images/adult/")

        elif(age_num >= 60):

            print 'directory : ', fullpath, 'age : ', age_num
            if os.path.isfile(fullpath):
                shutil.copy(
                    fullpath, "/home/crystalcampos/AGE_REGRESSION_AD/new_tagged_images/senior/")                        


if __name__ == "__main__":
    if(len(sys.argv) != 2):
        print "please usage: python tag_imdb_wiki.py txt_file_directory"
    else:
        main(sys.argv[1])
