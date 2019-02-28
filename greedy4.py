

from dataset import Dataset
from slideshow import Slide

def disjoint(set1, set2):
    return [(x, y) for x in set1 for y in set2 if not x == y]

def all_2v_slides(photos):
    pass

def greedy4(dataset: Dataset):
    hslides = [Slide(p) for p in dataset.h_photos()]
    vslides = [Slide(v1, v2) for v1, v2 in disjoint(dataset.v_photos(), dataset.v_photos())]
    print([hs.get_tags() for hs in hslides])
    print([vs.get_tags() for vs in vslides])
    print(hslides[2].interest_factor(hslides[3]))



if __name__=="__main__":
    ds = Dataset("inputs/f_louis.txt")
    greedy4(ds)

