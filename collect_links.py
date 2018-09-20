
import os
FOLDER = 'files'


class CollectLinks:

    def __init__(self):

        self.files = []
        # create list of the tiles in FOLDER
        for file_name in os.listdir(FOLDER):
            if file_name.endswith('.txt'):
                self.file_name = FOLDER + '/' + file_name
                self.files.append(self.file_name)

        for file in self.files:
            try:
                # Now we'll take only 1 file, but later if many...
                self.fo = open(file).read().split(',')
                # Readed text of the file in form of list of strings
                # that was separated by ','
            except:
                print('Info: File ', self.files[0],
                      ' cannot be opened, are you shure it exists?')
                exit()

    def get_links(self):
        """
        Take self.fo as a list of links (strings)

        """
        return self.fo


ff = CollectLinks()
ff.get_links()