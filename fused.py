class Fused_Ring(object):
    ring1 = ""
    ring2 = ""

    def __init__(self,ring1,ring2):
        self.ring1 = ring1
        self.ring2 = ring2

    def set_fused():
        self.fused = True

def create_fused_rings(rings):
    """ Finds which rings are fused given a list of rings. Returns a list of the
        fused rings

        Keyword Arguments:
        rings - The list of rings to check if there are any fused rings
    """
    fused_rings = []
    for i in range(0,len(rings)):
        outRing = rings[i].list()
        for j in range(0,len(rings)):
            inRing = rings[j].list()
            if outRing == inRing:
                continue
            if rings[i].fused:
                continue
            if rings[j].fused:
                continue
            counter = 0
            for k in range(0,len(outRing)):
                for j in range(0,len(inRing)):
                    if outRing[k] == inRing[j]:
                        counter += 1
                        if counter == 2:
                            fused_rings.append(Fused_Ring(inRing,outRing))
                            rings[i].fused = True
                            #rings[j].fused = True TODO some weird ass bug here
                        continue
    return fused_rings
