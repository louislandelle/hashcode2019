
def parse(input_fpath):
    with open(input_fpath) as fp:
        flines = fp.readlines()
    flines = [fline.replace('\n', '').split() for fline in flines]
    return int(flines[0][0]), flines[1:]

class Photo:
    """
    Photo class : represents one photo, vertical or horizontal
    photo.list_repr : list representation from dataset
    photo.orientation : 'H' or 'V' depending on Horizontal or Vertical orientation
    photo.tags : set of tags strings of this photo    
    """

    def __init__(self, list_repr):
        self.list_repr = list_repr
        self.orientation, self.n_tags = self.list_repr[:2]
        self.tags = set(self.list_repr[2:])

    def __str__(self):
        return ' | '.join((self.orientation, self.n_tags, ', '.join(self.tags)))

class Dataset:
    """
    Dataset class : represents a dataset, collection of photos
    dataset.length : amount of photos inside this dataset
    dataset.photos : list of Photo objects for each photo in the dataset
    """
    def __init__(self, input_fpath):
        self.length, lines = parse(input_fpath)
        self.photos = [Photo(line) for line in lines]
        self._h_photos = [p for p in self.photos if p.orientation == 'H']
        self._v_photos = [p for p in self.photos if p.orientation == 'V']
    
    def __str__(self):
        return '\n'.join(str(photo) for photo in self.photos)

    def n_unique_tags(self):
        return len(set.union(*(photo.tags for photo in self.photos)))

    def h_photos(self):
        return self._h_photos
    
    def v_photos(self):
        return self._v_photos

if __name__=="__main__":
    print(Dataset("inputs/a_example.txt").n_unique_tags())
    print(Dataset("inputs/b_lovely_landscapes.txt").n_unique_tags())
    #print(Dataset("inputs/c_memorable_moments.txt").n_unique_tags())
    print(Dataset("inputs/d_pet_pictures.txt").n_unique_tags())
    print(Dataset("inputs/e_shiny_selfies.txt").n_unique_tags())


