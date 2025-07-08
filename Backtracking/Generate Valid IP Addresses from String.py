def findIP(s, res):

    if dot == 0:
        res.append(curr)
        return
    curr = ""


def find_path(s):
    if len(s)>12:
        return []
    else:
        res = []
        dot = 4
        findIP(s,res,4)
        return res