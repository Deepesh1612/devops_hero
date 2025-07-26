my1=(1,2,3,4,5,"deep",{2,3})
my2=[1,2,3,4,5,"deep",{2,3}]
my3={2,3,4,5,2,3},
person = {
            'fname' :'deepesh',
            "lname" : "chandra",
            "age" : "35",
            "marks" : [
                        {
                            "maths" :5,
                            "science" :34
                         },
                        {
                            "python":23,
                            "c++" :24
                        }
                        ]  
    }
# print(person)
print(person["marks"][0],person['marks'][1]['python'])
