#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Special Functions


# In[4]:


from scipy import special 
a = special.exp10(2)          #10 Power 2
print(a)


# In[5]:


c = special.sindg(90)
print(c)


# In[7]:


d = special.cosdg(90)
print(d)


# # Integration

# In[14]:


from scipy import integrate


# In[16]:


i = lambda  x,y: x*y**2
j = lambda x:1
k = lambda x:-1
integrate.dblquad(i,0,2,j,k)


# # Fourier Transformation

# In[17]:


from scipy.fftpack import fft,ifft
import numpy as np
x=np.array([1,2,3,4])
y=fft(x)
print(y)


# In[18]:


#Inverse

x=np.array([1,2,3,4])
y=ifft(x)
print(y)


# # Linear Algebra

# In[19]:


from scipy import linalg
a=np.array([[1,2],[3,4]])
b=linalg.inv(a)
print(b)


# 

# In[ ]:





# In[ ]:





# In[ ]:




