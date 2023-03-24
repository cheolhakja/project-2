def convert(rating: str) -> int:
    criterion_list = [("width: 20%;", 0),("width: 40%;", 0),("width: 60%;", 0),("width: 80%;", 1),("width: 100%;", 1)]
    for i in criterion_list:
        if(i[0]==rating):
            return i[1]
            break
