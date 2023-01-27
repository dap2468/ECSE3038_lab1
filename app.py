def parallel(r):

    size=len(r)

    if (size>=2):
        RT=0.0
        for x in r:
            RT=(1/x)+RT

        RT=1/RT
        print("%.3f"%RT,"ohms")
    else:
        print ("not enough resistors")

parallel([330,1000,2200])