import numpy as np

def main():
    # question 1 i
    v = np.array([3294,3135,3256,3406,3347],dtype=float,)
    vave = np.mean(v)
    vstd = np.std(v,ddof=1,dtype=np.float64)
    n= np.size(v)
    vsem = vstd/np.sqrt(n)
    ii1_max = vave+vsem
    ii1_min = vave-vsem
    ii2_max = vave+vsem*1.96
    ii2_min = vave-vsem*1.96

# 1 iii
    v1 = np.array([3294,3135,3256,3406,3347,4300],dtype=float,)
    v1ave = np.mean(v1)
    v1std = np.std(v1,ddof=1,dtype=np.float64)
    n1= np.size(v1)
    v1sem = v1std/np.sqrt(n1)
    iii1_max = v1ave+v1sem
    iii1_min = v1ave-v1sem
    iii2_max = v1ave+v1sem*1.96
    iii2_min = v1ave-v1sem*1.96

    v3 = np.array([3294,3135,3256,3406,3347,(vave+vstd*5)],dtype=float,)
    v3ave = np.mean(v3)
    v3std = np.std(v3,ddof=3,dtype=np.float64)
    n3= np.size(v3)
    v3sem = v3std/np.sqrt(n3)
    iii3_max = v3ave+v3sem
    iii3_min = v3ave-v3sem
    iii4_max = v3ave+v3sem*1.96
    iii4_min = v3ave-v3sem*1.96

    print (f"""
    1i
        mean or estimated true value      {vave} m/s

        standard deviation or uncertainty {vstd} m/s

        Standard Error of the Mean        {vsem} m/s

        Range within 68%                  {ii1_min} m/s - {ii1_max} m/s

        Range within 95%                  {ii2_min} m/s - {ii2_max} m/s
    1iii a
        mean or estimated true value      {v1ave} m/s

        standard deviation or uncertainty {v1std} m/s

        Standard Error of the Mean        {v1sem} m/s

        Range within 68%                  {iii1_min} m/s - {iii1_max} m/s

        Range within 95%                  {iii2_min} m/s - {iii2_max} m/s
    1iii a
        mean or estimated true value      {v3ave} m/s

        standard deviation or uncertainty {v3std} m/s

        Standard Error of the Mean        {v3sem} m/s

        Range within 68%                  {iii3_min} m/s - {iii3_max} m/s

        Range within 95%                  {iii4_min} m/s - {iii4_max} m/s
    """
            )

if __name__ == "__main__":
    main()
