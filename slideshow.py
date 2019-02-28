
def export(slideshow: Slideshow):
    """ Exports a slideshow """
    raise NotImplementedError()

class Slide:
    """ Slide is either a H photo or two V photos """
    def __init__(self, photos):
        if len(photos) == 1: assert photos[0].orientation == 'H'        
        elif len(photos) == 2: assert all(p.orientation == 'V' for p in photos)
        else: raise Exception("Need one H photo or two V photos.")

    def interest_factor(self, other_slide):
        pass

class Slideshow:
    """ Slideshow contains multiple Slides """
    def __init__(self):
        self.slides = []

    def compute_score(self):
        score = 0
        last_slide = None
        for curr_slide in self.slides:
            score += last_slide.interest_factor(curr_slide)

