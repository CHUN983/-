list_1 = list(map(int ,input() .split())) 
"""讓輸入者輸入一串整數，
並利用.split()將空白鍵視為分割點。"""
print(list_1) 
"""先列印出原本的串列 """

def quick(data ,left ,right):
    '''建立一個區域變數，需要輸入者
    輸入的串列，與他們的最左邊與最右邊的數值'''
    if left >= right:
        return 
        '''當左邊的數值大於右邊的數值就跳出這個區域變數'''

    
    i = left 
    j = right
    key = data[left]
    '''key為快速排序的基準點數值'''
    
    while i < j : 
        '''確保在比對時不會造成無限迴圈'''
        while key < data[j] and i < j:
            j -=1
            '''當基準點的數比最右邊的元素小時，便把最右邊的索引-1，依序比對到有比基準點小的。
               遇到同數值時，將其視為比基準點大的部分'''
        while key >= data[i] and i < j:
            i +=1
            '''與上同理，但是把最左邊的依序+1比對，直到有比基準點還大的。
               而這裡加上等於是要讓基準點的數值不會因字元一樣而將同質搬動'''
        if i < j :
            '''確認i跟j變動完後是否導致i > j而造成排序錯誤'''
            temp = data[i]
            data[i] = data[j]
            data[j] = temp 
            '''此三段是將i元素與j元素做交換，達到大的數值在右邊，小的在左邊。'''
        
    temp = data[left]
    data[left] = data[i]
    data[i] = temp  
    '''最後將原在最左邊的基準數值值搬到i元素上，使那個基準數值能到達他最正確的位置'''
    
    quick(data ,left ,i-1) 
    quick(data ,i+1 ,right)
    '''將第一輪整理完的數值繼續做整理，並將其原標準值的索引做左右邊的分割'''
    





def binary (data ,search): 
    '''整理完後利用二位元組找到索引值，把原串列丟進去與欲查詢的數值'''
    quick(list_1 ,0 ,len(list_1)-1)    
    '''先將數值進行快速排序的整理'''
    print(list_1) 
    '''列印出整理完後的數值，主要確認是否整理錯誤'''
    
    low = 0 
    '''最左邊的索引'''
    up = len(data)-1
    '''最右邊的索引'''
    
    while low < up:
        '''形成重複比對的迴圈，而設置low < up是防止最後如果找不到資料不會造成迴圈'''
    
        mid = (low + up)//2
        '''取串列的索引中間值'''
        
        if search > data[mid] :
            low = mid +1
            
        elif search < data[mid] :
            up = mid -1
            '''此兩個條件是要看欲查詢的值是比中間值大還是小，並進而將範圍縮小。'''
        else:
            return mid
            '''若都不是就回傳'''
        
    return -1
    '''代表找不到輸入者所查詢的值'''

search = int(input()) 
'''讓輸入者輸入欲查詢的值'''

total = binary (list_1 ,search)
'''先帶入二元搜尋，再從中排序'''

if total == -1:
    print("查無資料")
else :
    print("此索引值為%d"%total)
      
