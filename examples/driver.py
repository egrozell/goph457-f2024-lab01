import numpy as np

def main():
    # question 1 i
    v = np.array([3294,3135,3256,3406,3347],dtype=float,)
    v_sqrt = np.sqrt(v)
    vave = np.mean(v)
    vstd = np.std(v)
    print (f"""
    1i
        mean or estimated true value      {vave} m/s

        standard deviation or uncertainty {vstd} m/s
    """
            )

if __name__ == "__main__":
    main()
