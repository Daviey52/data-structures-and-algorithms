from hashtable.hashtable import Hashtable

def left_join(hashtable1 , hashtable2):
    hashtable1 = Hashtable()
    hashtable2 = Hashtable()

    values=[hashtable1,]

    for i in hashtable1.bucket:
        for j in hashtable2.bucket:
            if i[0] == j[0]:
                values.append(j[1])
                j =+1
        i +=1

    return values
