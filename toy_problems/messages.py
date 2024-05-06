import json

dataArray = [
    {
        "id": 30,
        "username": "Ruth.Nduta",
        "email": "ruthnduta891@gmail.com",
        "messages": [
            {
                "receipient_id": 45,
                "read": False,
                "user_id": 30
            },
            {
                "receipient_id": 3,
                "read": False,
                "user_id": 30
            },
            {
                "receipient_id": 112,
                "read": False,
                "user_id": 30
            }
        ]
    },
    {
        "id": 3,
        "username": "Pascaline.Chumba",
        "email": "pjerono56@gmail.com",
        "messages": []
    },
    {
        "id": 45,
        "username": "Josephbill",
        "email": "josephbill00@gmail.com",
        "messages": [
            {
                "receipient_id": 3,
                "read": True,
                "user_id": 45
            }
        ]
    },
    {
        "id": 26,
        "username": "Simon.Thuo",
        "email": "simonthuo85@gmail.com",
        "messages": []
    },
    {
        "id": 112,
        "username": "Christine.Kiage",
        "email": "christinekiage@gmail.com",
        "messages": [
                  {
                "receipient_id": 45,
                "read": False,
                "user_id": 27
            },
            {
                "receipient_id": 3,
                "read": False,
                "user_id": 27
            },
            {
                "receipient_id": 112,
                "read": False,
                "user_id": 27
            }
            ]
    }]

def user_finder(cp_dataArray, targetid):
    user = []
    for data in cp_dataArray: # Time complexity of O(log(n)) Since it iterates a number of times till it gets first unique result. Array length reduces after each lookup
        if data["id"] == targetid:
            user.append(data)
            break
    return user[0]

def solution(dataArray, targetid):
    contacts_unread = []
    contacts_read = []

    cp_dataArray = list(dataArray)

    user_dict = user_finder(cp_dataArray, targetid) 
    
    for messages in user_dict["messages"]: # Time complexity of O(n) to Look up a value 
        recepient = user_finder(cp_dataArray, messages["receipient_id"]) # This loop within the loop introduces complexity of O(n * log(n))
        if messages["read"] == False:
            recepient.update({"tag" : "unread"})
            contacts_unread.append(recepient)
            # Remove from array copy to reduce iterations
            cp_dataArray.remove(recepient)
        else:
            recepient.update({"tag" : "read"})
            contacts_read.append(recepient)
            # Remove from array copy to reduce iterations
            cp_dataArray.remove(recepient)
        
    # user does not need to see themselves
    if user_dict in cp_dataArray:
        cp_dataArray.remove(user_dict)

    return json.dumps(contacts_unread + contacts_read + cp_dataArray, indent=2)

print(solution(dataArray, 45))

# Total time complexity is O(nlog(n)). Was unable to find O(n) or O(log(n)) time complexity

'''
 EXPECTED OUTPUT  for user 30 on listing 


let dataArray = [
      {
        "id": 45,
        "username": "Josephbill",
        "email": "josephbill00@gmail.com",
        “Tag”: “read”,
        "messages": [
            {
                "msg_id": 3,
                "read": true,
                "user_id": 45
            }
        ]
    },
    {
        "id": 112,
        "username": "Christine.Kiage",
        "email": "christinekiage@gmail.com",
        “Tag”: “unread”,
        "messages": [
                  {
                "msg_id": 45,
                "read": false,
                "user_id": 112
            },
            {
                "msg_id": 3,
                "read": false,
                "user_id": 112
            },
            {
                "msg_id": 20,
                "read": false,
                "user_id": 112
            }
            ]
    },


    {
        "id": 3,
        "username": "Pascaline.Chumba",
        "email": "pjerono56@gmail.com",
        "messages": []
        “Tag”: “read”


    },


    {
        "id": 26,
        "username": "Simon.Thuo",
        "email": "simonthuo85@gmail.com",
        “Tag”: “read”,
        "messages": []
    }
   ]

'''