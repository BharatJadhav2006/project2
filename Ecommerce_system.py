""" In an e-commerce system,customer account IDs are stored in a list 
and
 you are tasked with writing a program that implements the following:
 1) LinearSearch: check if a particular customer account ID exists in 
tyhe list.
 2)Binary Search: Implement binary search to find if a customer account 
ID exists,
 improving the search efficency over the basic linear """
 ' In an e-commerce system,customer account IDs are stored in a list 
and\nyou are tasked with writing a program that implements the 
following:\n1) LinearSearch: check if a particular customer account ID 
exists in tyhe list.\n2)Binary Search: Implement binary search to find 
if a customer account ID exists,\nimproving the search efficency over 
the basic linear '
 # add customer id to list
 custids=[]
 def addcustomer(custids,custid=0):
    if(custid<0):
        print("invalid customer")
        return
    custids.append(custid)
    return
 n=int(input("Enter nos of customer to add:"))
 for i in range(0,n):   #0(n)
    cid=int(input("Enter customer id:"))
    addcustomer(custids,cid)
    
custids    
Enter nos of customer to add:8
 Enter customer id:12
 Enter customer id:13
 Enter customer id:14
 Enter customer id:15
 Enter customer id:16
 Enter customer id:27
 Enter customer id:28
 Enter customer id:46
 [12, 13, 14, 15, 16, 27, 28, 46]
 Implemnting liner search
 def linear_search(custids,key): f1=0 t=0 for i in range(0,n): #0(n) t+=1 
print("Comparing",custids[i],"with key:", key,"complexity:time(",t,")")
    if(custids[i]==key):
        f1=1
        print("-"*50,"\nCustomer id 
exists",key,"complexity:time(",t,")")
        break
        
if(f1==0):
    t+=1
    print("-"*50,"\nCoustomer id does not 
exits",key,"comlexity:time(",t,")")
 return
 print("####### LINEAR SEARCH #######") key=int(input("enter customer id to search:")) 
linear_search(custids,key)
 # Implementing BINARY SEARCH 
def binary_search(custids,key,high,low=0,t=1):
    mid=(low+high)//2
    print(low,mid,high,cust_list[mid],cust_list)
    print("Comparing",cust_list[mid],"with 
key:",key,"complexity:time(",t,")")
    
    if(cust_list[mid]==key):
        print("-"*50,"\nCustomer id 
exists",key,"complexity:time(",t,")")
        return(0)
    elif(mid==low)or(mid==high-1):  #low>high
        #t+=1
        print("-"*50,"\nCustomer id does not 
exists",key,"complexity:time(",t,")")
        return
    
    t+=1
    if(cust_list[mid]>key):  #search left
        high=mid  #mid-1
        binary_search(custids,key,high,low,t)
    else: # search right
        low=mid  #mid+1
        binary_search(custids,key,high,low,t)
        
        
        
cust_list=custids.copy()
 cust_list.sort()
 print("#### BINARY SEARCH #####")
 key=int(input("enter customer id to search:"))
 binary_search(custids,key,high=len(cust_list))
