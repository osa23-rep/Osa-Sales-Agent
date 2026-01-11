def main():
    print("Agent Intialized...")
    user_message= input("user:  ").lower()
    
    phone_keywords = ["upgrade" ,  "new phone", "latest model", "buy phone", "purchase phone"]
    
    plans_keywords=["change plan", "new plan", "better plan", "switch plan", "upgrade plan"]
    
    wants_phone = any(keyword in user_message for keyword in phone_keywords)
    
    wants_plan= any(keyword in user_message for keyword in plans_keywords)
     
    
    