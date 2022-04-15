#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 16:44:43 2022

@author: woutervandermeij
"""

import pandas as pd

df=pd.read_csv('/Users/woutervandermeij/documents/Python/project-ecommerce/project-ecommerce/Collection_Results.csv')



dfSimple=df[['request.search_term',
       'result.search_results.title', 'result.search_results.asin',
       'result.search_results.link', 'result.search_results.image',
       'result.search_results.rating', 'result.search_results.ratings_total'
       ,'result.search_results.price.value']]



def MakeHighestReviewDF(dfSimple):
    
    dfa=pd.DataFrame()
    #some code for the first line
    i=0
    dHighestNumber=dfSimple.iloc[0,5]
    for i in range(1,len(dfSimple)):
        
        if(dfSimple.iloc[i,0]==dfSimple.iloc[i-1,0]):
            
            if(dfSimple.iloc[i,5]>dHighestNumber):
                dHighestNumber=dfSimple.iloc[i,5]
                IndexHighestNumber=i
                
            if i==len(dfSimple)-1:
                NewLine=dfSimple.iloc[IndexHighestNumber]
                dfa=dfa.append(NewLine, ignore_index=True)
            
        else:
            NewLine=dfSimple.iloc[IndexHighestNumber]
            dfa=dfa.append(NewLine, ignore_index=True)
                      
            dHighestNumber=dfSimple.iloc[i,5]
            IndexHighestNumber=i
            
    print("Newline =",dfa)
    return dfa 

def MakeHMostReviewDF(dfSimple):
    
    dfa=pd.DataFrame()
    #some code for the first line
    i=0
    dHighestNumber=dfSimple.iloc[0,6]
    for i in range(1,len(dfSimple)):
        
        if(dfSimple.iloc[i,0]==dfSimple.iloc[i-1,0]):
            
            if(dfSimple.iloc[i,6]>dHighestNumber):
                dHighestNumber=dfSimple.iloc[i,6]
                IndexHighestNumber=i
                
            if i==len(dfSimple)-1:
                NewLine=dfSimple.iloc[IndexHighestNumber]
                dfa=dfa.append(NewLine, ignore_index=True)
            
        else:
            NewLine=dfSimple.iloc[IndexHighestNumber]
            dfa=dfa.append(NewLine, ignore_index=True)
                      
            dHighestNumber=dfSimple.iloc[i,5]
            IndexHighestNumber=i
            
    print("Newline =",dfa)
    return dfa 

            
dfHighestReview=MakeHighestReviewDF(dfSimple)
dfMostReview=MakeHMostReviewDF(dfSimple)
    

dfHighestReview.to_csv('HighestReviewed.csv')
dfMostReview.to_csv('MostReviewed.csv')



