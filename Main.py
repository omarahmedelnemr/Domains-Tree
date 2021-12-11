from dt import Node,SLinkedList



list_of_domains = ['www.meet.google.com','www.cloud.google.com','www.youtube.com']#,'www.todo.google.com']
# data Parsing
i=0
while i < len(list_of_domains):
    list_of_domains[i] = list_of_domains[i].split('.')[::-1]
    i+=1

# Each Node Is Having A Uniqe Key ,and List of Children Key
Head= Node('.')

def Build(node,li,keyIndex):
    # stoping point of recursion
    if len(li) < keyIndex:
        return 1

    # if the  Uniqe Key the Current Key excited Or Not
    if (li[keyIndex-1]+str(keyIndex)) in node.keyList:

        # search for the Uniqe Key
        for i in node.childList:

            # when Found dive into it
            if i.key == (li[keyIndex-1]+str(keyIndex)):
                Build(i,li,keyIndex+1)

    # if not ,then add it and dive into it
    else:
        node.keyList.append(li[keyIndex-1]+str(keyIndex))
        node.childList.append(Node(li[keyIndex-1],keyIndex))
        Build(node.childList[-1],li,keyIndex+1)


# Start Building for each element in list of domains
for i in list_of_domains:
    Build(Head,i,1)



# Visualising The Data
def ves(node):
    text = ' '.join(node.keyList)
    sp = (len(text)//2 ) - (len(node.key)//2)
    print(sp*' ',node.key,'\n',text)
    print('--')

    for i in node.childList:
        ves(i)
ves(Head)