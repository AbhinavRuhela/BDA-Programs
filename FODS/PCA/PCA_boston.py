from pyforest import *
from sklearn.datasets import load_boston
from scipy.linalg import svd

boston = load_boston()
print(boston.keys())
df = pd.DataFrame(data= boston['data'], columns= boston['feature_names'])
#df.head()
print(df.shape)

#function to find svd
def find_svd(df):
    #eigen-vectors of A.A_transpose
    U = np.linalg.eig(df.dot(df.T))[1]
    eig_val_v, V = np.linalg.eig((df.T).dot(df))
    #diagonal matrix of square-root of eigen-values
    S = np.diag(np.sqrt(eig_val_v))
    temp = df.shape[0] - S.shape[0]
    temp_mat = np.zeros((temp,df.shape[1]),dtype=float)
    #increasing dimension of S
    S = np.append(S,temp_mat,axis=0)
    return(U,S,V)

U,S,V = find_svd(df)
err = []
for i in range(1,df.shape[1]+1):
    df2 = (U[:][:i].dot(S[:i][:i])).dot(V[:][:i].T)
#deviation from original matrix
print(df-df2)

#calculating u,s,v using library function
u1,s1,vt = svd(df)
print(u1)
print(U)
