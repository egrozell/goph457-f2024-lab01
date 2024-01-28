import numpy as np
import matplotlib.pyplot as plt

def main():
    phi_p = np.array([12,3.7,3.7,8.1,9.1,22,22,5.6,4.4,19,4.2,10,12,3.1],dtype=float,)
    p_ratio = np.full(len(phi_p),0.01,dtype=float)
    x = np.array(np.multiply(phi_p,p_ratio),dtype=float,)
    y = np.array([21.3,176,230,61.1,45.7,11.0,8.49,118,125,14.1,130,27.2,25,342],dtype=float,)
    y_log = np.log10(y)
    x_log = np.log10(x)
    a = np.array([np.ones((len(x),)),x_log]).T
    corrcoef = np.corrcoef(x_log,y_log)
    coefs,residuals = np.linalg.lstsq(a,y_log)[0:2]
    mean_y = np.mean(y_log)
    mean_x = np.mean(x_log)
    e_y = np.subtract(y_log,mean_y)
    e_x = np.subtract(x_log,mean_x)
    
    # trend line plot
    x_min = np.min(x_log)
    x_max = np.max(x_log)
    p0 = x_min*coefs[1]+coefs[0]
    p1 = x_max*coefs[1]+coefs[0]
    # uncertantity of the slope 
    var1 = np.sqrt(((np.dot(e_y,e_y))**2)/((len(x)-2)*(np.dot(e_x,e_x))**2))
    var2 = np.sqrt(((np.dot(e_y,e_y))**2*np.sum(y_log**2))/(len(x)*(len(x)-2)*(np.dot(e_x,e_x))**2))
    dyr = np.sqrt(residuals[0]/(len(x_log)-2))
    r0_max = p0 + dyr*1.96
    r0_min = p0 - dyr*1.96
    r1_max = p1 + dyr*1.96
    r1_min = p1 - dyr*1.96
    # cross-validation
    predicted = []
    for i in range (len(x_log)):
        x_log_temp = np.delete(a,i,0)
        y_log_temp = np.delete(y_log,i)
        coefs1 = np.linalg.lstsq(x_log_temp,y_log_temp)[0]
        pn = x_log[i]*coefs1[1]+coefs1[0]
        predicted.append(np.abs(pn-y_log[i]))
        # predicted.append(pn)
    # pred = np.array(predicted)
    # check = np.empty((len(x_log),2),dtype=float)
    # check = np.stack((y_log,pred),axis=0).T
    # mean_cross = np.mean(check,axis=1)
    mean_cross = np.mean(predicted)
    std_cross = np.std(predicted)
    # print(mean_cross)

    plt.figure(1)
    plt.plot(x_log,y_log,"ok",label="data")
    plt.plot((x_min,x_max),(p0,p1),"--k",label="trend")
    plt.plot((x_min,x_max),(r0_max,r1_max),":b",label="upper bound")
    plt.plot((x_min,x_max),(r0_min,r1_min),":b",label="lower bound")
    plt.ylabel("F log")
    plt.xlabel("phi ratio log")
    plt.legend()
    plt.title("Log of phi ratio vs Log of F")
    plt.savefig("archies")

    m = coefs[1]
    print(y_log)
    print(x_log)
    y0 = y_log[0]
    x0 = x_log[0]
    x0m = np.float_power(np.abs(x0),m)*np.sign(x0)

    print (f"""
a =   {y0/(x0m):.2e}
m =   {coefs[1]:.2e}
uncertainty of the slope     {var1:.2e}
uncertainty of the intercept {var2:.2e}
Standard error {dyr:.2e}
cross-validation 
mean {mean_cross:.2e}
std {std_cross:.2e}
    """)

if __name__ == "__main__":
    main()
