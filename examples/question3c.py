import numpy as np
import matplotlib.pyplot as plt

def main():
    v = np.array([1.85,2.01,2.97,3.71,2.18],dtype=float,)
    rho = np.array([2.06,2.10,2.33,2.47,3.21],dtype=float,)
    rho_log = np.log10(rho)
    v_log = np.log10(v)
    a = np.array([np.ones((len(v),)),v_log]).T
    corrcoef = np.corrcoef(v_log,rho_log)
    coefs,residuals = np.linalg.lstsq(a,rho_log)[0:2]
    mean_rho = np.mean(rho_log)
    mean_v = np.mean(v_log)
    e_rho = np.subtract(rho_log,mean_rho)
    e_v = np.subtract(v_log,mean_v)
    
    # trend line plot
    x_min = np.min(v_log)
    x_max = np.max(v_log)
    p0 = x_min*coefs[1]+coefs[0]
    p1 = x_max*coefs[1]+coefs[0]
    # uncertantity of the slope 
    var1 = np.sqrt(((np.dot(e_rho,e_rho))**2)/((len(v)-2)*(np.dot(e_v,e_v))**2))
    var2 = np.sqrt(((np.dot(e_rho,e_rho))**2*np.sum(rho_log**2))/((len(v)-2)*(np.dot(e_v,e_v))**2))
    dyr = np.sqrt(residuals[0]/(len(v_log)-2))
    r0_max = p0 + dyr*1.96
    r0_min = p0 - dyr*1.96
    r1_max = p1 + dyr*1.96
    r1_min = p1 - dyr*1.96
    # cross-validation
    predicted = []
    print(rho_log)
    for i in range (len(v_log)):
        v_log_temp = np.delete(a,i,0)
        rho_log_temp = np.delete(rho_log,i)
        coefs1 = np.linalg.lstsq(v_log_temp,rho_log_temp)[0]
        pn = v_log[i]*coefs1[1]+coefs1[0]
        predicted.append(np.abs(pn-rho_log[i]))
        # predicted.append(pn)
    # pred = np.array(predicted)
    # check = np.empty((len(v_log),2),dtype=float)
    # check = np.stack((rho_log,pred),axis=0).T
    # mean_cross = np.mean(check,axis=1)
    mean_cross = np.mean(predicted)
    std_cross = np.std(predicted)
    # print(mean_cross)
    plt.figure(1)
    plt.plot(v_log,rho_log,"ok",label="data")
    plt.plot((x_min,x_max),(p0,p1),"--k",label="trend")
    plt.plot((x_min,x_max),(r0_max,r1_max),":b",label="upper bound")
    plt.plot((x_min,x_max),(r0_min,r1_min),":b",label="lower bound")
    plt.ylabel("phi_log")
    plt.xlabel("velocity_log")
    plt.legend()
    plt.title("Log of Velocity vs Log of Density")
    plt.savefig("log_Velocity_vs_log_density_1")


    print (f"""
           coefs {coefs}

           residuals {residuals}
           
           var1 {var1}

           var2 {var2}

           Standard error {dyr:.2e}

           cross-validation 
           mean {mean_cross:.2e}
           std {std_cross:.2e}
           """)

if __name__ == "__main__":
    main()
