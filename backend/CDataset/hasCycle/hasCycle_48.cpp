class Solution {
public:
    bool hasCycle(ListNode *head) {
        if(!head)   return false;
        ListNode *slowptr = head;
        ListNode *fastptr = head;
        do{
            slowptr = slowptr->next;
            fastptr = fastptr->next;
            if(fastptr)
                fastptr = fastptr->next;
        }while(fastptr && slowptr!=fastptr);
        return fastptr ? true : false;
    }
};
