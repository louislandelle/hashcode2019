
def export(slideshow):
    """ Exports a slideshow """
    raise NotImplementedError()

class Slide:
    """ Slide is either a H photo or two V photos """
    def __init__(self, *photos):
        if len(photos) == 1: assert photos[0].orientation == 'H'        
        elif len(photos) == 2: assert all(p.orientation == 'V' for p in photos)
        else: raise Exception("Need one H photo or two V photos.")
        self.photos = photos
        self.orientation = 'H' if len(photos) == 1 else 'V'

    def get_tags(self):
        if self.orientation == 'H':
            return self.photos[0].tags
        else:
            return self.photos[0].tags.union(self.photos[1].tags)

    def interest_factor(self, other_slide):
        s1 = self.get_tags().intersection(other_slide.get_tags())
        s2 = self.get_tags() - other_slide.get_tags()
        s3 = other_slide.get_tags() - self.get_tags()
        return min(len(s) for s in (s1, s2, s3))

class Slideshow:
    """ Slideshow contains multiple Slides """
    def __init__(self):
        self.slides = []

    def compute_score(self):
        score = 0
        last_slide = None
        for curr_slide in self.slides:
            score += last_slide.interest_factor(curr_slide)

