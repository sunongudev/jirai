

if __name__=="dev.read":
    while True:
        code=input(" $ ")
        try:
            if code=="exit()":
                break
            else:
                a=code.find("<<")
                if a+1:
                   code=code.replace("<<","") 
                   code.strip()
                   code="print("+code+')'
                   exec(code)
                a=code.find(">>")
                if a+1:
                    code=code.replace(">>","")
                    var=code[a:].strip()
                    varstr=code[:a].strip()
                    if varstr:
                        exec("varstr="+varstr)
                    locals()[var]=input(varstr)
        except SyntaxError: 
            print("Load Error")
        except NameError:
            print("Name Error")
