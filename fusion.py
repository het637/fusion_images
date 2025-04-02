from PIL import Image

image2=Image.open("ceciestune2eimage.jpg")
image1=Image.open("image1.jpg")


def dec_to_bin(nbr : int)->list :
    tab_bin = []
    for i in range(8) :
        tab_bin = [nbr % 2] + tab_bin
        nbr //= 2
    return tab_bin

def bin_to_dec(tab_bin : list)->int :
    nbr = 0
    for i in range(8) :
        nbr += tab_bin[i]*2**(7-i)
    return nbr



def retire_bits_faible(tab) :
    for i in range(-1,-5,-1):
        tab[i] = 0
    return tab



def bits_fort_vers_faible(tab) :
    for i in range(4):
        tab[i+4] = tab[i]
        tab[i] = 0
    return tab



def bits_faible_vers_fort(tab) :
    for i in range(4,8):
        tab[i-4] = tab[i]
        tab[i] = 0
    return tab



def fusion(image_visi,image_invisi) :
    if image_visi.size[0] >= image_invisi.size[0] :
        larg = image_invisi.size[0]
    else :
        larg = image_visi.size[0]

    if image_visi.size[1] >= image_invisi.size[1] :
        haut = image_invisi.size[1]
    else :
        haut = image_visi.size[1]

    
    image_fusion = Image.new(mode = 'RGB',size = (larg,haut))
    for x in range(larg):
        for y in range(haut):

            px_vis = image_visi.getpixel((x,y))
            px_vis = list(px_vis)
            for i in range(3):
                px_vis[i] = dec_to_bin(px_vis[i])
                px_vis[i] = retire_bits_faible(px_vis[i])

            

            px_invis = image_invisi.getpixel((x,y))
            px_invis = list(px_invis)
            for i in range(3):
                px_invis[i] = dec_to_bin(px_invis[i])
                px_invis[i] = bits_fort_vers_faible(px_invis[i])

            

            px_fus = [[],[],[]]
            for i in range(3) :
                for j in range(8):
                    px_fus[i] += [px_vis[i][j]+px_invis[i][j]]

                px_fus[i] = bin_to_dec(px_fus[i])

            image_fusion.putpixel((x,y),tuple(px_fus))
    image_fusion.show()
    image_fusion.save("image_fusion.jpg")
    return image_fusion

fusion(image1,image2)

