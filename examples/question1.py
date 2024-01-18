import numpy as np

def main():
    # question 1 i
    v = np.array([3294,3135,3256,3406,3347],dtype=float,)
    vave = np.mean(v)
    vstd = np.std(v,ddof=1,dtype=np.float64)
    n= np.size(v)
    vsem = vstd/np.sqrt(n)
    ii1 = vsem*.68
    ii2 = vsem*.95

# 1 iii
    v1 = np.array([3294,3135,3256,3406,3347,4300],dtype=float,)
    v1ave = np.mean(v1)
    v1std = np.std(v1,ddof=1,dtype=np.float64)
    n1= np.size(v1)
    v1sem = v1std/np.sqrt(n1)
    iii1 = v1sem*.68
    iii2 = v1sem*.95


    print (f"""
    1i
        mean or estimated true value      {vave} m/s

        standard deviation or uncertainty {vstd} m/s

        Standard Error of the Mean        {vsem} m/s

        Range within 68%                  {ii1} m/s

        Range within 95%                  {ii2} m/s
    1iii
        mean or estimated true value      {v1ave} m/s

        standard deviation or uncertainty {v1std} m/s

        Standard Error of the Mean        {v1sem} m/s

        Range within 68%                  {iii1} m/s

        Range within 95%                  {iii2} m/s
    """
            )

if __name__ == "__main__":
    main()
